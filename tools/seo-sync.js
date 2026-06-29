#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const https = require("https");
const { spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const DEFAULT_DOMAIN = "https://sagopaint.vn";
const DEFAULT_PROJECT = "sagopaint";
const EXCLUDED_DIRS = new Set([
  ".git",
  ".wrangler",
  "assets",
  "seo",
  "tools",
  "__pycache__",
]);
const EXCLUDED_FILES = [/^google[a-z0-9]+\.html$/i];

const args = new Set(process.argv.slice(2));
const getArgValue = (name, fallback) => {
  const prefix = `${name}=`;
  const found = process.argv.slice(2).find((arg) => arg.startsWith(prefix));
  return found ? found.slice(prefix.length) : fallback;
};

const DOMAIN = normalizeDomain(getArgValue("--domain", DEFAULT_DOMAIN));
const PROJECT = getArgValue("--project", DEFAULT_PROJECT);
const DRY_RUN = args.has("--dry-run");
const CHECK_LIVE = args.has("--check-live");
const DEPLOY = args.has("--deploy");
const SKIP_HEAD = args.has("--skip-head");
const MIN_WORDS = 300;

function normalizeDomain(domain) {
  return domain.replace(/\/+$/, "");
}

function walkHtmlFiles(dir) {
  const files = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (EXCLUDED_DIRS.has(entry.name)) continue;

    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...walkHtmlFiles(fullPath));
      continue;
    }

    if (entry.isFile() && entry.name.endsWith(".html") && !EXCLUDED_FILES.some((re) => re.test(entry.name))) {
      files.push(fullPath);
    }
  }
  return files;
}

function routeFromFile(filePath) {
  const rel = path.relative(ROOT, filePath).replace(/\\/g, "/");

  if (rel === "index.html") return "/";
  if (rel.endsWith("/index.html")) {
    return `/${rel.slice(0, -"index.html".length)}`;
  }
  return `/${rel.replace(/\.html$/, "")}`;
}

function urlFromRoute(route) {
  return `${DOMAIN}${route}`;
}

function priorityForRoute(route) {
  if (route === "/") return "1.0";
  if (route === "/son-noi-that" || route === "/son-ngoai-that" || route === "/son-chong-tham") return "0.9";
  if (route.endsWith("/")) return "0.8";
  return "0.8";
}

function lastmodForFile(filePath) {
  const stat = fs.statSync(filePath);
  return stat.mtime.toISOString().slice(0, 10);
}

function sortPages(a, b) {
  if (a.route === "/") return -1;
  if (b.route === "/") return 1;
  return a.route.localeCompare(b.route);
}

function xmlEscape(value) {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function buildSitemap(pages) {
  const entries = pages
    .map((page) => `  <url>
    <loc>${xmlEscape(page.url)}</loc>
    <lastmod>${page.lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>${priorityForRoute(page.route)}</priority>
  </url>`)
    .join("\n");

  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${entries}
</urlset>
`;
}


function stripTags(html) {
  return html
    .replace(/<script\b[\s\S]*?<\/script>/gi, " ")
    .replace(/<style\b[\s\S]*?<\/style>/gi, " ")
    .replace(/<[^>]+>/g, " ");
}

function textContent(html) {
  return stripTags(html)
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/\s+/g, " ")
    .trim();
}

function matchContent(html, re) {
  const match = html.match(re);
  return match ? match[1].trim() : "";
}

function pageMeta(page) {
  const html = fs.readFileSync(page.filePath, "utf8");
  const main = matchContent(html, /<main\b[^>]*>([\s\S]*?)<\/main>/i) || html;
  const robots = matchContent(html, /<meta\b(?=[^>]*\bname=["']robots["'])[^>]*\bcontent=["']([^"']*)["'][^>]*>/i).toLowerCase();
  const canonical = matchContent(html, /<link\b(?=[^>]*\brel=["']canonical["'])[^>]*\bhref=["']([^"']*)["'][^>]*>/i);

  return {
    ...page,
    title: textContent(matchContent(html, /<title[^>]*>([\s\S]*?)<\/title>/i)),
    description: matchContent(html, /<meta\b(?=[^>]*\bname=["']description["'])[^>]*\bcontent=["']([^"']*)["'][^>]*>/i),
    h1: textContent(matchContent(html, /<h1\b[^>]*>([\s\S]*?)<\/h1>/i)),
    canonical,
    noindex: robots.includes("noindex"),
    wordCount: textContent(main).split(/\s+/).filter(Boolean).length,
  };
}

function duplicates(pages, field) {
  const seen = new Map();
  const dupes = [];
  for (const page of pages) {
    const value = page[field];
    if (!value) continue;
    if (seen.has(value)) dupes.push([value, seen.get(value), page]);
    else seen.set(value, page);
  }
  return dupes;
}

function auditPages(pages) {
  const issues = [];
  const routeSet = new Set();
  const indexablePages = pages.filter((page) => !page.noindex);
  for (const page of pages) {
    if (routeSet.has(page.route)) issues.push(`duplicate route: ${page.route}`);
    routeSet.add(page.route);
    if (page.route.length > 100) issues.push(`URL over 100 chars: ${page.route}`);
  }
  for (const page of indexablePages) {
    if (!page.title) issues.push(`missing title: ${page.route}`);
    if (!page.description) issues.push(`missing meta description: ${page.route}`);
    if (!page.h1) issues.push(`missing h1: ${page.route}`);
    if (page.canonical && page.canonical !== page.url) issues.push(`canonical mismatch: ${page.route}`);
    if (page.wordCount < MIN_WORDS) issues.push(`thin page (${page.wordCount} words): ${page.route}`);
  }

  for (const [value, first, second] of duplicates(indexablePages, "title")) {
    issues.push(`duplicate title: ${first.route} and ${second.route} (${value})`);
  }
  for (const [value, first, second] of duplicates(indexablePages, "description")) {
    issues.push(`duplicate meta description: ${first.route} and ${second.route} (${value})`);
  }

  return issues;
}
function buildRobots() {
  return `User-agent: *
Allow: /

Sitemap: ${DOMAIN}/sitemap.xml
`;
}

function writeIfChanged(filePath, content) {
  const current = fs.existsSync(filePath) ? fs.readFileSync(filePath, "utf8") : "";
  if (current === content) return false;
  if (!DRY_RUN) fs.writeFileSync(filePath, content, "utf8");
  return true;
}

function replaceOrInsertHeadTag(html, tagName, attrName, attrValue, fullTag) {
  const tagRe = new RegExp(`<${tagName}\\b(?=[^>]*\\b${attrName}=["']${escapeRegExp(attrValue)}["'])[^>]*>`, "i");
  if (tagRe.test(html)) return html.replace(tagRe, fullTag);

  const headEnd = html.search(/<\/head>/i);
  if (headEnd === -1) return html;
  return `${html.slice(0, headEnd)}    ${fullTag}\n${html.slice(headEnd)}`;
}

function insertFaviconTags(html) {
  if (html.includes('href="/assets/favicon-32x32.png"')) return html;

  const headEnd = html.search(/<\/head>/i);
  if (headEnd === -1) return html;

  const tags = [
    '<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32x32.png">',
    '<link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16x16.png">',
    '<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">',
    '<link rel="manifest" href="/assets/site.webmanifest">',
    '<link rel="shortcut icon" href="/assets/favicon.ico">',
  ].map((tag) => `    ${tag}`).join("\n");

  return `${html.slice(0, headEnd)}${tags}\n${html.slice(headEnd)}`;
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function syncHeadTags(pages) {
  let changed = 0;
  const oldDomainRe = /https:\/\/sagopaint\.(com|vn)\/([^"'<> )]+?)\.html/g;

  for (const page of pages) {
    let html = fs.readFileSync(page.filePath, "utf8");
    const before = html;
    const canonicalUrl = page.noindex && page.canonical ? page.canonical : page.url;
    const canonicalTag = `<link rel="canonical" href="${canonicalUrl}">`;
    const ogUrlTag = `<meta property="og:url" content="${canonicalUrl}">`;

    html = html.replace(oldDomainRe, "https://sagopaint.vn/$2");
    html = replaceOrInsertHeadTag(html, "link", "rel", "canonical", canonicalTag);
    html = replaceOrInsertHeadTag(html, "meta", "property", "og:url", ogUrlTag);
    html = insertFaviconTags(html);

    if (html !== before) {
      changed++;
      if (!DRY_RUN) fs.writeFileSync(page.filePath, html, "utf8");
    }
  }
  return changed;
}

function parseRedirects() {
  const redirectsPath = path.join(ROOT, "_redirects");
  if (!fs.existsSync(redirectsPath)) return [];

  return fs
    .readFileSync(redirectsPath, "utf8")
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter((line) => line && !line.startsWith("#"))
    .map((line) => {
      const [from, to, status] = line.split(/\s+/);
      return { from, to, status };
    });
}

function requestHead(url, redirectCount = 0) {
  return new Promise((resolve) => {
    const req = https.request(url, { method: "HEAD" }, (res) => {
      res.resume();
      resolve({
        url,
        status: res.statusCode,
        location: res.headers.location || "",
        redirected: redirectCount,
      });
    });

    req.on("error", (error) => {
      resolve({ url, status: 0, location: "", error: error.message, redirected: redirectCount });
    });

    req.setTimeout(15000, () => {
      req.destroy(new Error("timeout"));
    });

    req.end();
  });
}

async function checkLive(pages) {
  console.log("\nLive check");

  const sitemap = await requestHead(`${DOMAIN}/sitemap.xml`);
  const robots = await requestHead(`${DOMAIN}/robots.txt`);
  console.log(`  sitemap.xml: ${formatStatus(sitemap)}`);
  console.log(`  robots.txt:   ${formatStatus(robots)}`);

  const urlsToCheck = pages.map((page) => page.url);
  const results = [];
  for (const url of urlsToCheck) {
    results.push(await requestHead(url));
  }

  const badPages = results.filter((result) => result.status < 200 || result.status >= 400);
  console.log(`  pages checked: ${results.length}`);
  console.log(`  page errors:   ${badPages.length}`);
  for (const result of badPages.slice(0, 20)) {
    console.log(`    ${formatStatus(result)} ${result.url}`);
  }

  const redirects = parseRedirects();
  if (redirects.length) {
    const redirectResults = [];
    for (const redirect of redirects) {
      redirectResults.push({
        redirect,
        result: await requestHead(`${DOMAIN}${redirect.from}`),
      });
    }
    const badRedirects = redirectResults.filter(({ result }) => result.status !== 301 && result.status !== 302 && result.status !== 308);
    console.log(`  redirects checked: ${redirectResults.length}`);
    console.log(`  redirect errors:   ${badRedirects.length}`);
    for (const { redirect, result } of badRedirects.slice(0, 20)) {
      console.log(`    ${redirect.from} -> ${redirect.to}: ${formatStatus(result)}`);
    }
  }
}

function formatStatus(result) {
  const base = result.status || "ERR";
  const location = result.location ? ` -> ${result.location}` : "";
  const error = result.error ? ` (${result.error})` : "";
  return `${base}${location}${error}`;
}

function deploy() {
  console.log(`\nDeploying to Cloudflare Pages project: ${PROJECT}`);
  if (DRY_RUN) {
    console.log("  dry run: skipped deploy");
    return;
  }

  const result = spawnSync("npx", ["wrangler", "pages", "deploy", ".", "--project-name", PROJECT], {
    cwd: ROOT,
    stdio: "inherit",
    shell: process.platform === "win32",
  });

  if (result.status !== 0) {
    process.exit(result.status || 1);
  }
}

async function main() {
  const pages = walkHtmlFiles(ROOT)
    .map((filePath) => ({
      filePath,
      route: routeFromFile(filePath),
      lastmod: lastmodForFile(filePath),
    }))
    .map((page) => ({ ...page, url: urlFromRoute(page.route) }))
    .map(pageMeta)
    .sort(sortPages);

  const indexablePages = pages.filter((page) => !page.noindex);
  const auditIssues = auditPages(pages);

  const sitemapChanged = writeIfChanged(path.join(ROOT, "sitemap.xml"), buildSitemap(indexablePages));
  const robotsChanged = writeIfChanged(path.join(ROOT, "robots.txt"), buildRobots());
  const headChanged = SKIP_HEAD ? 0 : syncHeadTags(pages);

  console.log("SEO sync complete");
  console.log(`  domain:           ${DOMAIN}`);
  console.log(`  pages:            ${pages.length}`);
  console.log(`  indexable pages:  ${indexablePages.length}`);
  console.log(`  sitemap.xml:      ${sitemapChanged ? "updated" : "unchanged"}`);
  console.log(`  robots.txt:       ${robotsChanged ? "updated" : "unchanged"}`);
  console.log(`  head tags:        ${SKIP_HEAD ? "skipped" : `${headChanged} file(s) updated`}`);
  console.log(`  redirects:        ${parseRedirects().length}`);
  console.log(`  quality issues:   ${auditIssues.length}`);
  for (const issue of auditIssues.slice(0, 30)) {
    console.log(`    - ${issue}`);
  }
  if (auditIssues.length > 30) console.log(`    ... ${auditIssues.length - 30} more`);

  if (DEPLOY) deploy();
  if (CHECK_LIVE) await checkLive(indexablePages);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});

