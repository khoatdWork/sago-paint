import lighthouse from 'lighthouse';
import { chromium } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';
import net from 'node:net';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { createServer } = require('./serve-static');
const { ROOT } = require('./site-files');

const arg = name => process.argv.find(x => x.startsWith(`--${name}=`))?.split('=').slice(1).join('=');
const dir = path.resolve(ROOT, arg('dir') || 'dist');
const out = path.resolve(ROOT, arg('output') || 'output/lighthouse');
const routes = (arg('routes') || '/,/son-noi-that,/blog,/son-nha-moi-xay,/phong-thuy-son-nha/,/tinh-son/').split(',');
fs.mkdirSync(out, { recursive: true });
const server = createServer(dir);
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
const debug = net.createServer();
await new Promise(resolve => debug.listen(0, '127.0.0.1', resolve));
const port = debug.address().port;
await new Promise(resolve => debug.close(resolve));
let browser;
const summary = [];
try {
  browser = await chromium.launch({ headless: true, args: [`--remote-debugging-port=${port}`] });
  for (const route of routes) {
    const url = `http://127.0.0.1:${server.address().port}${route}`;
    const result = await lighthouse(url, { port, output: 'html', logLevel: 'error',
      onlyCategories: ['performance', 'accessibility', 'best-practices', 'seo'],
      formFactor: 'mobile', throttlingMethod: 'simulate' });
    if (!result || result.lhr.runtimeError) throw new Error(result?.lhr.runtimeError?.message || 'Lighthouse returned no result');
    const name = route.replace(/[^a-z0-9-]/g, '_') || 'home';
    fs.writeFileSync(path.join(out, name + '.html'), result.report);
    fs.writeFileSync(path.join(out, name + '.json'), JSON.stringify(result.lhr, null, 2));
    const row = { route, scores: Object.fromEntries(Object.entries(result.lhr.categories).map(([key, value]) => [key, value.score])),
      lcp_ms: result.lhr.audits['largest-contentful-paint']?.numericValue,
      cls: result.lhr.audits['cumulative-layout-shift']?.numericValue,
      failedAudits: Object.values(result.lhr.audits).filter(a => a.score !== null && a.score < 1).map(a => a.id) };
    summary.push(row);
    console.log(JSON.stringify(row));
  }
} finally {
  fs.writeFileSync(path.join(out, 'summary.json'), JSON.stringify(summary, null, 2));
  if (browser) await browser.close();
  await new Promise(resolve => server.close(resolve));
}
