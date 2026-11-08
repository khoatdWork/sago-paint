"""Read-only checks for HTML, route graph, sitemap and page context."""
import hashlib
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree
from site_content import ROOT, Page, context_path, inventory


def check():
    entries = inventory()
    baseline = json.loads((ROOT / "tests/page-contracts.json").read_text(encoding="utf-8"))
    contracts = baseline["pages"]
    pages, errors = {}, []
    for entry in entries:
        try:
            pages[(ROOT / entry["file"]).resolve()] = (entry, Page((ROOT / entry["file"]).read_text(encoding="utf-8")))
        except (ValueError, OSError) as error:
            errors.append(f"{entry['file']}: {error}")
    inbound = Counter()
    canonical_urls, titles, descriptions = [], [], []
    for file, (entry, page) in pages.items():
        label = entry["file"]
        def require(condition, message):
            if not condition:
                errors.append(f"{label}: {message}")
        source = file.read_text(encoding="utf-8")
        noindex = "noindex" in page.meta.get("robots", "")
        contract = contracts.get(label)
        require(contract is not None and contract["canonical"] == page.canonicals
                and contract["robots"] == [page.meta.get("robots", "")], "canonical/robots differ from approved route baseline")
        require(page.lang == "vi", "html lang must be vi")
        require(page.h1_count == 1, f"expected one primary H1; found {page.h1_count}")
        require(bool(page.title.strip()), "missing title")
        require(bool(page.meta.get("description")), "missing description")
        require(len(page.canonicals) == 1, "expected exactly one canonical")
        if len(page.canonicals) == 1:
            expected = "https://sagopaint.vn" + entry["route"]
            require(noindex or page.canonicals[0] == expected, "canonical does not match public route")
            require(page.meta.get("og:url") == page.canonicals[0], "og:url does not match canonical")
            if not noindex:
                canonical_urls.append(page.canonicals[0]); titles.append(page.title); descriptions.append(page.meta.get("description"))
        require("main-content" in page.ids and 'class="skip-link"' in source, "missing main/skip link")
        require(any("family=Be+Vietnam+Pro" in x and "display=swap" in x for x in page.styles), "missing Be Vietnam Pro CDN stylesheet")
        shared_css = Path(os.path.relpath(ROOT / "assets/css/site-base.css", file.parent)).as_posix()
        require(shared_css in page.styles, f"shared stylesheet must use file-safe relative href: {shared_css}")
        require(not re.search(r"font-family[^;]+(?:Inter|Playfair)|family=(?:Inter|Playfair)|\.{2}/https://", source), "obsolete font or malformed absolute asset URL")
        context = context_path(entry["route"])
        require(context.is_file(), "missing CONTEXT.md")
        if context.is_file():
            text = context.read_text(encoding="utf-8")
            require(f"`{label}`" in text and f"https://sagopaint.vn{entry['route']}" in text, "context points to wrong page")
            require(page.title.strip() in text, "context title differs from page")
        for img in page.images:
            require("alt" in img, f"image has no alt: {img.get('src')}")
        for ref in page.links + page.assets:
            url = urlsplit(ref)
            if url.scheme and not (url.scheme in ("https", "http") and url.hostname in ("sagopaint.vn", "www.sagopaint.vn")):
                continue
            if ref.startswith("//"):
                continue
            decoded = unquote(url.path)
            target = (ROOT / decoded.lstrip("/") if decoded.startswith("/") else file.parent / decoded).resolve() if decoded else file
            if not target.is_relative_to(ROOT):
                require(False, f"asset/link escapes public root: {ref}"); continue
            candidates = [target, target.with_suffix(".html"), target / "index.html"] if not target.suffix else [target]
            resolved = next((p for p in candidates if p.is_file()), None)
            require(resolved is not None, f"broken internal reference: {ref}")
            if resolved in pages:
                if resolved != file and ref in page.links:
                    inbound[resolved] += 1
                fragment = unquote(url.fragment)
                require(not fragment or fragment.lower() == "top" or fragment in pages[resolved][1].ids, f"missing anchor: {ref}")
    for file, (entry, page) in pages.items():
        if entry["route"] != "/" and "noindex" not in page.meta.get("robots", "") and inbound[file] == 0:
            errors.append(f"{entry['file']}: no inbound internal link")
    for name, values in [("title", titles), ("description", descriptions)]:
        errors.extend(f"duplicate {name}: {value}" for value, count in Counter(values).items() if count > 1)
    sitemap = ElementTree.parse(ROOT / "sitemap.xml")
    urls = [item.text for item in sitemap.findall(".//{*}loc")]
    if Counter(urls) != Counter(canonical_urls):
        errors.append("sitemap URLs differ from canonical, indexable public pages")
    if "Sitemap: https://sagopaint.vn/sitemap.xml" not in (ROOT / "robots.txt").read_text():
        errors.append("robots.txt does not reference canonical sitemap")
    if len(entries) != 54 or len(canonical_urls) != 53:
        errors.append(f"Route inventory changed: {len(entries)} content / {len(canonical_urls)} indexable; review baseline explicitly")
    verification = ROOT / baseline["verification"]["file"]
    if hashlib.sha256(verification.read_bytes()).hexdigest() != baseline["verification"]["sha256"]:
        errors.append("Google verification file changed")
    skills = ROOT / ".agents/skills"
    manifest = json.loads((skills / "sources.json").read_text(encoding="utf-8"))
    for item in manifest:
        folder = skills / item["name"]
        if not (folder / "SKILL.md").is_file() or not (folder / item["license_file"]).is_file():
            errors.append(f"skill/license missing: {item['name']}")
        if not item.get("commit") or not item.get("source"):
            errors.append(f"skill provenance missing: {item['name']}")
    summary = {"content_pages": len(entries), "indexable_pages": len(canonical_urls), "errors": errors}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(check())
