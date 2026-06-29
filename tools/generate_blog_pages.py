from __future__ import annotations

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content" / "blog"
SITE_URL = "https://sagopaint.vn"
DATE = "2026-06-13"


POSTS = {
    "01-son-nha-mien-tay-mua-mua-chong-tham.md": {
        "slug": "son-nha-mien-tay-mua-mua-chong-tham",
        "category": "Chống thấm",
        "read_time": "12 phút đọc",
        "thumbnail": "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?auto=format&fit=crop&w=1400&q=84",
        "summary": "Giải pháp chống thấm, xử lý rêu mốc và bảo vệ tường ngoài trời cho nhà miền Tây trong mùa mưa kéo dài.",
    },
    "02-mau-son-nha-cap-4-dep-2026.md": {
        "slug": "mau-son-nha-cap-4-dep-2026",
        "category": "Màu sơn",
        "read_time": "11 phút đọc",
        "thumbnail": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1400&q=84",
        "summary": "10 màu sơn nhà cấp 4 sáng, mát, bền thẩm mỹ và hợp khí hậu nóng ẩm miền Tây năm 2026.",
    },
    "03-son-nha-huong-tay-chong-nong.md": {
        "slug": "son-nha-huong-tay-chong-nong",
        "category": "Chống nóng",
        "read_time": "9 phút đọc",
        "thumbnail": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=1400&q=84",
        "summary": "Bảng màu sáng, giải pháp che nắng và hệ sơn giúp nhà hướng Tây bớt nóng dưới khí hậu miền Tây.",
    },
    "04-son-nha-moi-xay.md": {
        "slug": "son-nha-moi-xay",
        "category": "Kỹ thuật sơn",
        "read_time": "9 phút đọc",
        "thumbnail": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=1400&q=84",
        "summary": "Khi nào tường mới đủ khô để sơn, cách kiểm tra độ ẩm và quy trình sơn nhà mới tránh phồng rộp.",
    },
    "05-son-nha-hop-phong-thuy.md": {
        "slug": "son-nha-hop-phong-thuy",
        "category": "Phong thủy",
        "read_time": "10 phút đọc",
        "thumbnail": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1400&q=84",
        "summary": "Chọn màu sơn theo tuổi, mệnh và ngũ hành nhưng vẫn hợp ánh sáng, khí hậu và phong cách nhà hiện đại.",
    },
}

HOME_ARTICLES = [
    {
        "title": "Xu hướng màu sơn nhà 2026",
        "url": "xu-huong-mau-son-nha-2026.html",
        "category": "Xu hướng 2026",
        "read_time": "3 phút đọc",
        "summary": "Bảng màu warm white, be, nâu đất, xanh olive và cách phối màu thực tế cho nhà Việt.",
        "thumbnail": "https://images.unsplash.com/photo-1600210491369-e753d80a41f3?auto=format&fit=crop&w=1400&q=84",
        "featured": True,
    },
    {
        "title": "Sơn Nhà Miền Tây Mùa Mưa",
        "url": "son-nha-mien-tay-mua-mua-chong-tham.html",
        "category": "Chống thấm",
        "read_time": "12 phút đọc",
        "summary": "7 giải pháp xử lý thấm, rêu mốc và bảo vệ tường ngoài trời cho mùa mưa miền Tây.",
        "thumbnail": POSTS["01-son-nha-mien-tay-mua-mua-chong-tham.md"]["thumbnail"],
    },
    {
        "title": "Top 10 Màu Sơn Nhà Cấp 4 Đẹp 2026",
        "url": "mau-son-nha-cap-4-dep-2026.html",
        "category": "Màu sơn",
        "read_time": "11 phút đọc",
        "summary": "Những gam màu sáng, mát và dễ bảo trì cho nhà cấp 4 miền Tây.",
        "thumbnail": POSTS["02-mau-son-nha-cap-4-dep-2026.md"]["thumbnail"],
    },
    {
        "title": "Nhà Hướng Tây Sơn Màu Gì?",
        "url": "son-nha-huong-tay-chong-nong.html",
        "category": "Chống nóng",
        "read_time": "9 phút đọc",
        "summary": "Gợi ý màu sơn giảm hấp thụ nhiệt, phối ngoại thất và giải pháp che nắng.",
        "thumbnail": POSTS["03-son-nha-huong-tay-chong-nong.md"]["thumbnail"],
    },
    {
        "title": "Nhà Mới Xây Bao Lâu Thì Sơn Được?",
        "url": "son-nha-moi-xay.html",
        "category": "Kỹ thuật sơn",
        "read_time": "9 phút đọc",
        "summary": "Mốc chờ tường khô, cách kiểm tra độ ẩm và quy trình sơn nhà mới miền Tây.",
        "thumbnail": POSTS["04-son-nha-moi-xay.md"]["thumbnail"],
    },
    {
        "title": "Màu Sơn Nhà Hợp Phong Thủy 2026",
        "url": "son-nha-hop-phong-thuy.html",
        "category": "Phong thủy",
        "read_time": "10 phút đọc",
        "summary": "Chọn màu theo tuổi và mệnh, cân bằng giữa phong thủy, ánh sáng và độ bền.",
        "thumbnail": POSTS["05-son-nha-hop-phong-thuy.md"]["thumbnail"],
    },
]

FIGURE_IMAGES = [
    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=82",
    "https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&w=1200&q=82",
    "https://images.unsplash.com/photo-1562259949-e8e7689d7828?auto=format&fit=crop&w=1200&q=82",
    "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=82",
    "https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?auto=format&fit=crop&w=1200&q=82",
]


def esc(value: str) -> str:
    return html.escape(value or "", quote=True)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    _, raw_meta, body = text.split("---", 2)
    meta: dict[str, str] = {}
    current = None
    for line in raw_meta.splitlines():
        if not line.strip():
            continue
        if not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            current = key.strip()
            meta[current] = value.strip().strip('"')
        elif current and line.strip().startswith("- "):
            meta[current] = (meta.get(current, "") + ", " + line.strip()[2:].strip('"')).strip(", ")
    return meta, body.strip()


def inline_md(value: str) -> str:
    def link(match: re.Match[str]) -> str:
        href = match.group(2)
        if href.startswith("../../"):
            href = href[6:]
        return f'<a href="{esc(href)}">{esc(match.group(1))}</a>'

    value = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    return value


def markdown_to_html(body: str) -> tuple[str, str]:
    schema = ""
    body = re.sub(r"```json\s*(.*?)\s*```", lambda m: capture_schema(m, store := {"schema": ""}), body, flags=re.S)
    schema_match = re.search(r"@@SCHEMA:(.*?)@@", body, re.S)
    if schema_match:
        schema = schema_match.group(1).strip()
        body = body.replace(schema_match.group(0), "")

    html_parts: list[str] = []
    pending_list: list[str] = []
    figure_index = 0

    def flush_list() -> None:
        if pending_list:
            html_parts.append("<ul>" + "".join(pending_list) + "</ul>")
            pending_list.clear()

    lines = body.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            flush_list()
            i += 1
            continue
        if line.startswith("# "):
            flush_list()
            i += 1
            continue
        if line.startswith("## "):
            flush_list()
            html_parts.append(f"<h2>{inline_md(esc(line[3:].strip()))}</h2>")
        elif line.startswith("### "):
            flush_list()
            html_parts.append(f"<h3>{inline_md(esc(line[4:].strip()))}</h3>")
        elif line.startswith("!["):
            flush_list()
            match = re.match(r"!\[([^\]]+)\]\(([^)]+)\)", line)
            alt = match.group(1) if match else "Hình minh họa bài viết"
            src = FIGURE_IMAGES[figure_index % len(FIGURE_IMAGES)]
            figure_index += 1
            caption = ""
            desc = ""
            if i + 1 < len(lines) and lines[i + 1].strip().startswith("*Caption:"):
                caption = lines[i + 1].strip().strip("*").replace("Caption:", "").strip()
                i += 1
            if i + 2 < len(lines) and lines[i + 1].strip().startswith("Mô tả ảnh:"):
                desc = lines[i + 1].strip().replace("Mô tả ảnh:", "").strip()
                i += 1
            figcaption = caption or desc
            html_parts.append(
                f'<figure class="article-figure"><img src="{esc(src)}" alt="{esc(alt)}" loading="lazy" width="1200" height="675"><figcaption>{esc(figcaption)}</figcaption></figure>'
            )
        elif line.startswith("- "):
            pending_list.append(f"<li>{inline_md(esc(line[2:].strip()))}</li>")
        else:
            flush_list()
            para_lines = [line]
            while i + 1 < len(lines):
                nxt = lines[i + 1].strip()
                if not nxt or nxt.startswith(("#", "-", "![", "```")):
                    break
                if nxt.startswith("*Caption:") or nxt.startswith("Mô tả ảnh:"):
                    break
                para_lines.append(nxt)
                i += 1
            paragraph = " ".join(para_lines)
            html_parts.append(f"<p>{inline_md(esc(paragraph))}</p>")
        i += 1
    flush_list()
    return "\n".join(html_parts), schema


def capture_schema(match: re.Match[str], store: dict[str, str]) -> str:
    store["schema"] = match.group(1)
    return f"@@SCHEMA:{match.group(1)}@@"


def nav(active: str = "") -> str:
    return f"""
    <header class="site-header fixed-top">
      <nav class="navbar navbar-expand-lg" aria-label="Điều hướng chính">
        <div class="container">
          <a class="navbar-brand" href="index.html" aria-label="Sago Paint - Trang chủ"><img class="brand-logo" src="https://cdn.sagopaint.vn/assets/sago-logo.png" alt="Logo Sago Paint" width="1010" height="518"></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNavigation" aria-controls="mainNavigation" aria-expanded="false" aria-label="Mở menu"><span class="navbar-toggler-icon"></span></button>
          <div class="collapse navbar-collapse" id="mainNavigation">
            <ul class="navbar-nav ms-auto align-items-lg-center">
              <li class="nav-item"><a class="nav-link" href="index.html">Trang Chủ</a></li>
              <li class="nav-item"><a class="nav-link" href="son-noi-that.html">Nội Thất</a></li>
              <li class="nav-item"><a class="nav-link" href="son-ngoai-that.html">Ngoại Thất</a></li>
              <li class="nav-item"><a class="nav-link" href="son-chong-tham.html">Chống Thấm</a></li>
              <li class="nav-item"><a class="nav-link" href="tinh-son/index.html">Tính Sơn</a></li>
              <li class="nav-item"><a class="nav-link {'active' if active == 'blog' else ''}" href="blog.html">Bài Viết</a></li>
            </ul>
            <a class="btn btn-primary ms-lg-3 mt-3 mt-lg-0" href="tel:+842866815050">Nhận tư vấn</a>
          </div>
        </div>
      </nav>
    </header>"""


def footer() -> str:
    return """
    <footer id="lien-he" class="footer pt-5">
      <div class="container">
        <div class="row g-4 pb-5">
          <div class="col-lg-4">
            <img class="footer-logo mb-3" src="https://cdn.sagopaint.vn/assets/sago-logo.png" alt="Logo Sago Paint" width="1010" height="518">
            <h2 class="h4 text-white">Công ty Sơn Sago</h2>
            <p class="mb-0">Cung cấp sơn nội thất, sơn ngoại thất, sơn chống thấm và giải pháp sơn nhà toàn diện.</p>
          </div>
          <div class="col-sm-6 col-lg-3">
            <h3 class="h5 mb-3 text-white">Thông tin liên hệ</h3>
            <p class="mb-2">Địa chỉ: 4/19 Đường 25, Khu phố 5, Phường Hiệp Bình Chánh, TP. Thủ Đức, TP. Hồ Chí Minh</p>
            <p class="mb-2">Điện thoại: <a href="tel:+842866815050">+8428 6681 5050</a></p>
            <p class="mb-0">Email: <a href="mailto:info.sagopaint@gmail.com">info.sagopaint@gmail.com</a></p>
          </div>
          <div class="col-sm-6 col-lg-2">
            <h3 class="h5 mb-3 text-white">Danh mục</h3>
            <ul class="list-unstyled d-grid gap-2 mb-0">
              <li><a href="son-noi-that.html">Sơn nội thất</a></li>
              <li><a href="son-ngoai-that.html">Sơn ngoại thất</a></li>
              <li><a href="son-chong-tham.html">Sơn chống thấm</a></li>
              <li><a href="blog.html">Bài viết</a></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom py-4 d-flex flex-column flex-md-row justify-content-between gap-2"><span>&copy; 2026 Công ty Sơn Sago.</span><span>Đại lý sơn uy tín cho giải pháp sơn nhà chuyên nghiệp.</span></div>
      </div>
    </footer>"""


def render_post(md_name: str, config: dict[str, str]) -> None:
    raw = (CONTENT_DIR / md_name).read_text(encoding="utf-8")
    meta, body = parse_frontmatter(raw)
    title = re.search(r"^#\s+(.+)$", body, re.M).group(1)
    article_html, schema = markdown_to_html(body)
    description = meta.get("meta_description") or config["summary"]
    url = f"{SITE_URL}/{config['slug']}"
    schema_block = schema or json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "author": {"@type": "Organization", "name": "Sago Paint"},
        "publisher": {"@type": "Organization", "name": "Sago Paint"},
        "datePublished": DATE,
        "dateModified": DATE,
        "mainEntityOfPage": url,
    }, ensure_ascii=False, indent=6)
    page = f"""<!doctype html>
<html lang="vi">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(meta.get("seo_title") or title)} | Sago Paint</title>
    <meta name="description" content="{esc(description)}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{esc(url)}">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(description)}">
    <meta property="og:image" content="{esc(config["thumbnail"])}">
    <meta property="og:url" content="{esc(url)}">
    <meta property="og:locale" content="vi_VN">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(title)}">
    <meta name="twitter:description" content="{esc(description)}">
    <meta name="twitter:image" content="{esc(config["thumbnail"])}">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <link href="category-pages.css" rel="stylesheet">
    <script type="application/ld+json">
{schema_block}
    </script>
  </head>
  <body>
{nav("blog")}
    <main>
      <section class="product-hero blog-article-hero">
        <div class="container">
          <div class="row g-5 align-items-center">
            <div class="col-lg-7">
              <p class="section-kicker mb-3">{esc(config["category"])}</p>
              <h1 class="product-hero-title mb-4">{esc(title)}</h1>
              <p class="product-hero-copy mb-4">{esc(description)}</p>
              <div class="hero-summary">
                <span>{esc(config["read_time"])}</span>
                <span>Cập nhật {DATE}</span>
                <span>Chuyên đề sơn nhà miền Tây</span>
              </div>
            </div>
            <div class="col-lg-5">
              <div class="product-visual blog-article-visual"><img class="product-detail-image" src="{esc(config["thumbnail"])}" alt="{esc(title)}" width="1400" height="788" loading="eager"></div>
            </div>
          </div>
        </div>
      </section>
      <section class="section-padding bg-white">
        <div class="container">
          <div class="row g-5 justify-content-center">
            <article class="col-lg-8 article-body blog-article-body">
{article_html}
            </article>
            <aside class="col-lg-4">
              <div class="info-panel accent-panel sticky-lg-top blog-side-panel">
                <p class="section-kicker mb-2">Tư vấn nhanh</p>
                <h2 class="h4 mb-3">Cần chọn hệ sơn phù hợp?</h2>
                <p>Gửi ảnh tường, hướng nhà và khu vực thi công để được tư vấn sơn nội thất, ngoại thất, chống thấm hoặc S60 Pro theo tình trạng thực tế.</p>
                <a class="btn btn-primary mt-2" href="tel:+842866815050">Nhận tư vấn miễn phí</a>
              </div>
            </aside>
          </div>
        </div>
      </section>
    </main>
{footer()}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
  </body>
</html>
"""
    (ROOT / f"{config['slug']}.html").write_text(page, encoding="utf-8", newline="\n")


def article_card(article: dict[str, object]) -> str:
    featured = " featured" if article.get("featured") else ""
    return f"""
            <article class="trend-card{featured}">
              <a class="trend-card-link" href="{esc(str(article["url"]))}" aria-label="{esc(str(article["title"]))}">
                <div class="trend-card-media">
                  <img src="{esc(str(article["thumbnail"]))}" alt="{esc(str(article["title"]))}" loading="lazy" width="1400" height="788">
                  <span class="trend-badge">{esc(str(article["category"]))}</span>
                </div>
                <div class="trend-card-body">
                  <div class="trend-meta"><span>{esc(str(article["read_time"]))}</span></div>
                  <h3>{esc(str(article["title"]))}</h3>
                  <p>{esc(str(article["summary"]))}</p>
                  <span class="trend-cta">Khám phá bài viết →</span>
                </div>
              </a>
            </article>"""


def render_blog_index() -> None:
    cards = "\n".join(article_card(article) for article in HOME_ARTICLES)
    page = f"""<!doctype html>
<html lang="vi">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bài viết sơn nhà, chống thấm và màu sơn 2026 | Sago Paint</title>
    <meta name="description" content="Tổng hợp bài viết chuyên sâu về màu sơn nhà, chống thấm, chống nóng, phong thủy và kỹ thuật sơn cho nhà miền Tây.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{SITE_URL}/blog">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Bài viết sơn nhà Sago Paint">
    <meta property="og:description" content="Cẩm nang sơn nhà, chống thấm, chống nóng và màu sơn 2026.">
    <meta property="og:image" content="{HOME_ARTICLES[0]["thumbnail"]}">
    <meta property="og:url" content="{SITE_URL}/blog">
    <meta property="og:locale" content="vi_VN">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <link href="category-pages.css" rel="stylesheet">
  </head>
  <body>
{nav("blog")}
    <main>
      <section class="category-hero">
        <div class="container">
          <p class="section-kicker mb-3">Cẩm nang sơn nhà</p>
          <h1 class="category-title mb-4">Bài viết chuyên sâu về màu sơn, chống thấm và kỹ thuật thi công</h1>
          <p class="category-description mb-0">Nội dung thực tế cho nhà miền Tây: mùa mưa, nhà gần sông rạch, nhà hướng Tây, nhà cấp 4 và nhu cầu chọn màu sơn bền đẹp.</p>
        </div>
      </section>
      <section class="trend-section blog-index-section">
        <div class="container">
          <div class="trend-grid">
{cards}
          </div>
        </div>
      </section>
    </main>
{footer()}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
  </body>
</html>
"""
    (ROOT / "blog.html").write_text(page, encoding="utf-8", newline="\n")


def update_sitemap() -> None:
    sitemap = ROOT / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    urls = ["blog"] + [cfg["slug"] for cfg in POSTS.values()]
    insert = "".join(
        f"  <url>\n    <loc>{SITE_URL}/{slug}</loc>\n    <lastmod>{DATE}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
        for slug in urls
        if f"{SITE_URL}/{slug}" not in text
    )
    if insert:
        text = text.replace("</urlset>", insert + "</urlset>")
        sitemap.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    for md_name, config in POSTS.items():
        render_post(md_name, config)
    render_blog_index()
    update_sitemap()


if __name__ == "__main__":
    main()
