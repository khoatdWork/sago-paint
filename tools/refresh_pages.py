from __future__ import annotations

import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://sagopaint.com"


CATEGORY_META = {
    "son-noi-that.html": {
        "name": "Sơn nội thất",
        "short": "Nội thất",
        "kicker": "Danh mục sơn trong nhà",
        "title": "Sơn nội thất Sago Paint",
        "headline": "Sơn nội thất bền màu, ít mùi, dễ lau chùi cho không gian sống hiện đại",
        "description": "Danh mục sơn nội thất Sago Paint gồm sơn phủ, sơn lót và bột trét giúp hoàn thiện bề mặt tường trong nhà mịn đẹp, dễ lau chùi, ít mùi và bền màu.",
        "seo": "Sơn nội thất Sago Paint phù hợp cho phòng khách, phòng ngủ, căn hộ, văn phòng và công trình dân dụng cần bề mặt tường mịn, màu sắc ổn định, dễ vệ sinh. Danh mục gồm các dòng sơn che phủ cao, sơn lau chùi hiệu quả, sơn lót kháng kiềm và bột trét xử lý bề mặt trước khi sơn.",
        "heading": "Sản phẩm sơn nội thất nổi bật",
        "use_cases": ["Phòng khách, phòng ngủ, căn hộ", "Văn phòng, showroom, khách sạn", "Tường mới hoặc tường cải tạo cần lớp phủ mịn"],
        "benefits": ["Ít mùi, thân thiện hơn khi thi công trong nhà", "Màng sơn mịn, che phủ tốt", "Dễ lau chùi và bảo dưỡng"],
    },
    "son-ngoai-that.html": {
        "name": "Sơn ngoại thất",
        "short": "Ngoại thất",
        "kicker": "Danh mục sơn ngoài trời",
        "title": "Sơn ngoại thất Sago Paint",
        "headline": "Bảo vệ mặt tiền trước nắng mưa, rêu mốc và phai màu",
        "description": "Danh mục sơn ngoại thất Sago Paint giúp xử lý bề mặt, chống kiềm, chống rêu mốc, hạn chế phai màu và bảo vệ công trình trước điều kiện thời tiết.",
        "seo": "Sơn ngoại thất Sago Paint được thiết kế cho mặt tiền, tường bao, biệt thự, nhà phố và công trình thương mại. Các dòng sơn chú trọng khả năng chống rêu mốc, chống bám bụi, hạn chế phai màu, bảo vệ màng sơn trước nắng mưa và độ ẩm cao.",
        "heading": "Sản phẩm sơn ngoại thất nổi bật",
        "use_cases": ["Mặt tiền nhà phố, biệt thự, tường rào", "Công trình thương mại, văn phòng, khách sạn", "Khu vực ngoài trời thường xuyên chịu nắng mưa"],
        "benefits": ["Chống rêu mốc và bám bẩn", "Bền màu trong điều kiện ngoài trời", "Bảo vệ bề mặt tường lâu dài"],
    },
    "son-chong-tham.html": {
        "name": "Sơn chống thấm",
        "short": "Chống thấm",
        "kicker": "Danh mục chống thấm",
        "title": "Sơn chống thấm Sago Paint",
        "headline": "Giải pháp chống thấm cho tường, mái, sân thượng và ban công",
        "description": "Danh mục chống thấm Sago Paint cho tường, sân thượng, mái, ban công, tầng hầm và các khu vực cần bảo vệ trước nước, ẩm mốc.",
        "seo": "Sơn chống thấm Sago Paint hỗ trợ ngăn nước xâm nhập, giảm ẩm mốc và bảo vệ kết cấu cho các bề mặt bê tông, tường tô vữa, sân thượng, sê nô, ban công và mái. Danh mục gồm chống thấm màu, chống thấm pha xi măng và chống thấm lộ thiên.",
        "heading": "Sản phẩm chống thấm nổi bật",
        "use_cases": ["Sân thượng, mái, sê nô, ban công", "Tường đứng ngoài trời, tường giáp ranh", "Khu vực có nguy cơ thấm nước và ẩm mốc"],
        "benefits": ["Hạn chế nước xâm nhập", "Giảm rạn nứt và ẩm mốc", "Tăng tuổi thọ bề mặt công trình"],
    },
}


def fix_text(value: str) -> str:
    value = html.unescape(value or "")
    if any(ch in value for ch in ("Ã", "Æ", "Ä", "áº", "á»", "Â")):
        try:
            value = value.encode("cp1252").decode("utf-8")
        except UnicodeError:
            pass
    value = value.replace("Sơn Sagopain ", "Sơn Sagopaint ")
    value = value.replace("Sơn Sagopaint nột thất", "Sơn Sagopaint nội thất")
    value = value.replace("Màn sơn", "Màng sơn")
    value = value.replace("bè mặt", "bề mặt")
    value = value.replace("dể sử dụng", "dễ sử dụng")
    value = value.replace("phúc tạp", "phức tạp")
    value = value.replace("Cộng nghệ", "Công nghệ")
    value = value.replace("ANA MATEXlà", "ANA MATEX là")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def text_from_tag(source: str, tag: str, class_name: str | None = None) -> str:
    if class_name:
        pattern = rf"<{tag}[^>]*class=[\"'][^\"']*{re.escape(class_name)}[^\"']*[\"'][^>]*>(.*?)</{tag}>"
    else:
        pattern = rf"<{tag}[^>]*>(.*?)</{tag}>"
    match = re.search(pattern, source, re.S | re.I)
    if not match:
        return ""
    text = re.sub(r"<[^>]+>", " ", match.group(1))
    return fix_text(text)


def attr_from_tag(source: str, tag: str, class_name: str, attr: str) -> str:
    pattern = rf"<{tag}[^>]*class=[\"'][^\"']*{re.escape(class_name)}[^\"']*[\"'][^>]*>"
    match = re.search(pattern, source, re.S | re.I)
    if not match:
        return ""
    attr_match = re.search(rf"{attr}=[\"']([^\"']+)[\"']", match.group(0), re.I)
    return html.unescape(attr_match.group(1)) if attr_match else ""


def list_items(source: str, class_name: str) -> list[str]:
    ul = re.search(rf"<ul[^>]*class=[\"'][^\"']*{re.escape(class_name)}[^\"']*[\"'][^>]*>(.*?)</ul>", source, re.S | re.I)
    if not ul:
        return []
    items = []
    for item in re.findall(r"<li[^>]*>(.*?)</li>", ul.group(1), re.S | re.I):
        item = re.sub(r"<strong>(.*?)</strong>", r"\1:", item, flags=re.S | re.I)
        item = re.sub(r"<[^>]+>", " ", item)
        text = fix_text(item).replace(": :", ":")
        if text:
            items.append(text)
    return items


def paragraphs(source: str) -> list[str]:
    items = []
    for para in re.findall(r"<p[^>]*class=[\"'][^\"']*detail-copy[^\"']*[\"'][^>]*>(.*?)</p>", source, re.S | re.I):
        text = fix_text(re.sub(r"<[^>]+>", " ", para))
        if text:
            items.append(text)
    return items


def summarize(parts: list[str], fallback: str, limit: int = 158) -> str:
    text = " ".join(parts) or fallback
    text = fix_text(text)
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].rstrip(".,;:")
    return f"{cut}."


def product_category(source: str) -> str:
    match = re.search(r'<a class="breadcrumb-link[^"]*"[^>]*href="([^"]+)"', source)
    return html.unescape(match.group(1)) if match else "son-noi-that.html"


def extract_product(path: Path) -> dict:
    source = path.read_text(encoding="utf-8")
    title = text_from_tag(source, "h1", "product-hero-title") or text_from_tag(source, "title").replace(" - Sago Paint", "")
    image = attr_from_tag(source, "img", "product-detail-image", "src")
    detail = paragraphs(source)
    category_file = product_category(source)
    category = CATEGORY_META[category_file]
    features = list_items(source, "feature-list")
    specs = list_items(source, "spec-list")
    process = list_items(source, "process-list")
    description = summarize(detail, text_from_tag(source, "p", "product-hero-copy"))
    return {
        "file": path.name,
        "name": title,
        "image": image,
        "category_file": category_file,
        "category_name": category["name"],
        "category_short": category["short"],
        "description": description,
        "detail": detail or [description],
        "features": features,
        "specs": specs,
        "process": process,
        "badge": guess_badge(title, features),
    }


def guess_badge(title: str, features: list[str]) -> str:
    text = f"{title} {' '.join(features)}".lower()
    if "chống thấm" in text:
        return "Chống thấm"
    if "bột trét" in text:
        return "Bột trét"
    if "lót" in text or "sealer" in text:
        return "Sơn lót"
    if "lau chùi" in text:
        return "Lau chùi"
    if "rêu mốc" in text:
        return "Chống rêu mốc"
    if "che phủ" in text:
        return "Che phủ cao"
    if "ngoại thất" in text:
        return "Ngoại thất"
    return "Sơn phủ"


def nav(active: str | None = None) -> str:
    def cls(file: str) -> str:
        return " active" if active == file else ""

    aria_home = ' aria-current="page"' if active == "index.html" else ""
    return f"""
    <header class="site-header fixed-top">
      <nav class="navbar navbar-expand-lg" aria-label="Điều hướng chính">
        <div class="container">
          <a class="navbar-brand" href="index.html" aria-label="Sago Paint - Trang chủ">
            <img class="brand-logo" src="assets/sago-logo.png" alt="Logo Sago Professional Coatings">
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNavigation" aria-controls="mainNavigation" aria-expanded="false" aria-label="Mở menu điều hướng">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="mainNavigation">
            <ul class="navbar-nav ms-auto align-items-lg-center">
              <li class="nav-item"><a class="nav-link{cls('index.html')}" href="index.html"{aria_home}>Trang chủ</a></li>
              <li class="nav-item"><a class="nav-link{cls('son-noi-that.html')}" href="son-noi-that.html">Nội thất</a></li>
              <li class="nav-item"><a class="nav-link{cls('son-ngoai-that.html')}" href="son-ngoai-that.html">Ngoại thất</a></li>
              <li class="nav-item"><a class="nav-link{cls('son-chong-tham.html')}" href="son-chong-tham.html">Chống thấm</a></li>
              <li class="nav-item"><a class="nav-link" href="#lien-he">Liên hệ</a></li>
            </ul>
            <a class="btn btn-primary ms-lg-3 mt-3 mt-lg-0" href="#lien-he">Nhận tư vấn</a>
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
            <img class="footer-logo mb-3" src="assets/sago-logo.png" alt="Logo Sago Paint">
            <h2 class="h4 text-white">Công ty Sơn Sago</h2>
            <p class="mb-0">Cung cấp sơn nội thất, sơn ngoại thất, sơn chống thấm và giải pháp sơn nhà toàn diện cho công trình Việt Nam.</p>
          </div>
          <div class="col-sm-6 col-lg-3">
            <h3 class="h5 mb-3 text-white">Thông tin liên hệ</h3>
            <p class="mb-2">Địa chỉ: 123 Đường Nguyễn Văn Linh, Quận 7, TP. Hồ Chí Minh</p>
            <p class="mb-2">Điện thoại: <a href="tel:+842812345678">028 1234 5678</a></p>
            <p class="mb-0">Email: <a href="mailto:hello@sagopaint.com">hello@sagopaint.com</a></p>
          </div>
          <div class="col-sm-6 col-lg-2">
            <h3 class="h5 mb-3 text-white">Danh mục</h3>
            <ul class="list-unstyled d-grid gap-2 mb-0">
              <li><a href="son-noi-that.html">Sơn nội thất</a></li>
              <li><a href="son-ngoai-that.html">Sơn ngoại thất</a></li>
              <li><a href="son-chong-tham.html">Sơn chống thấm</a></li>
            </ul>
          </div>
          <div class="col-lg-3">
            <h3 class="h5 mb-3 text-white">Giờ làm việc</h3>
            <p class="mb-2">Thứ Hai - Thứ Sáu: 08:00 - 17:30</p>
            <p class="mb-2">Thứ Bảy: 08:00 - 12:00</p>
            <p class="mb-0">Chủ Nhật: Nghỉ</p>
          </div>
        </div>
        <div class="footer-bottom py-4 d-flex flex-column flex-md-row justify-content-between gap-2">
          <span>&copy; 2026 Công ty Sơn Sago. Đã đăng ký bản quyền.</span>
          <span>Đại lý sơn uy tín cho giải pháp sơn nhà chuyên nghiệp.</span>
        </div>
      </div>
    </footer>"""


def head(title: str, description: str, path: str, image: str = "assets/sago-logo.png", schema: list[dict] | None = None) -> str:
    canonical = f"{SITE_URL}/{path}"
    schema_json = json.dumps(schema or [], ensure_ascii=False, indent=6)
    return f"""  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(description)}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{esc(canonical)}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(description)}">
    <meta property="og:image" content="{esc(image)}">
    <meta property="og:url" content="{esc(canonical)}">
    <meta property="og:locale" content="vi_VN">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(title)}">
    <meta name="twitter:description" content="{esc(description)}">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <link href="category-pages.css" rel="stylesheet">
    <script type="application/ld+json">
      {schema_json}
    </script>
  </head>"""


def breadcrumb_schema(items: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": index + 1, "name": name, "item": f"{SITE_URL}/{url}"}
            for index, (name, url) in enumerate(items)
        ],
    }


def render_product(product: dict) -> str:
    cat_file = product["category_file"]
    title = f"{product['name']} | {product['category_name']} Sago Paint"
    description = summarize([product["description"]], product["name"], 155)
    schema = [
        breadcrumb_schema([("Trang chủ", "index.html"), (product["category_name"], cat_file), (product["name"], product["file"])]),
        {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": product["name"],
            "image": f"{SITE_URL}/{product['image']}",
            "description": description,
            "brand": {"@type": "Brand", "name": "Sago Paint"},
            "category": product["category_name"],
        },
    ]
    feature_items = "".join(f"<li>{esc(item)}</li>" for item in product["features"][:8])
    spec_items = "".join(f"<li>{esc(item)}</li>" for item in product["specs"][:8])
    process_items = "".join(f"<li>{esc(item)}</li>" for item in product["process"][:14])
    detail_paras = "\n".join(f'                <p class="detail-copy">{esc(item)}</p>' for item in product["detail"])
    keywords = [product["category_name"], product["badge"], "Sago Paint"]
    return f"""<!doctype html>
<html lang="vi">
{head(title, description, product['file'], product['image'], schema)}
  <body>
{nav(cat_file)}
    <main>
      <section class="product-hero">
        <div class="container">
          <div class="row g-5 align-items-center">
            <div class="col-lg-7">
              <a class="breadcrumb-link d-inline-flex mb-3" href="{esc(cat_file)}">&larr; {esc(product['category_name'])}</a>
              <p class="section-kicker mb-3">Chi tiết sản phẩm</p>
              <h1 class="product-hero-title mb-4">{esc(product['name'])}</h1>
              <p class="product-hero-copy mb-4">{esc(description)}</p>
              <div class="keyword-strip mb-4">
                {"".join(f'<span>{esc(item)}</span>' for item in keywords)}
              </div>
              <div class="d-flex flex-wrap gap-2">
                <a class="btn btn-primary" href="#lien-he">Nhận tư vấn sản phẩm</a>
                <a class="btn btn-outline-primary" href="{esc(cat_file)}">Xem danh mục</a>
              </div>
            </div>
            <div class="col-lg-5">
              <div class="product-visual">
                <img class="product-detail-image" src="{esc(product['image'])}" alt="{esc(product['name'])}">
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="section-padding bg-white">
        <div class="container">
          <div class="row g-4 mb-4">
            <div class="col-lg-5">
              <article class="info-panel accent-panel">
                <p class="section-kicker mb-2">Tính năng</p>
                <h2 class="h3 mb-4">Điểm nổi bật</h2>
                <ul class="feature-list">{feature_items or '<li>Phù hợp thi công cho công trình dân dụng và thương mại.</li>'}</ul>
              </article>
            </div>
            <div class="col-lg-7">
              <article class="info-panel">
                <p class="section-kicker mb-2">Thông số</p>
                <h2 class="h3 mb-4">Thông tin kỹ thuật</h2>
                <ul class="spec-list">{spec_items or '<li>Liên hệ Sago Paint để được tư vấn định mức và hệ sơn phù hợp.</li>'}</ul>
              </article>
            </div>
          </div>
          <div class="row g-4">
            <div class="col-lg-7">
              <article class="info-panel">
                <p class="section-kicker mb-2">Mô tả</p>
                <h2 class="h3 mb-4">Thông tin sản phẩm</h2>
{detail_paras}
              </article>
            </div>
            <div class="col-lg-5">
              <article class="info-panel">
                <p class="section-kicker mb-2">Thi công</p>
                <h2 class="h3 mb-4">Hướng dẫn sử dụng</h2>
                <ul class="process-list">{process_items or '<li>Chuẩn bị bề mặt sạch, khô và ổn định trước khi thi công.</li><li>Khuấy đều sản phẩm và thi công theo hệ sơn được tư vấn.</li>'}</ul>
              </article>
            </div>
          </div>
        </div>
      </section>
      <section class="seo-band">
        <div class="container">
          <div class="seo-panel">
            <div>
              <p class="section-kicker mb-2">Tư vấn hệ sơn</p>
              <h2 class="h3 mb-3">Cần chọn đúng sản phẩm cho bề mặt thực tế?</h2>
              <p class="mb-0">Sago Paint hỗ trợ kiểm tra bề mặt, gợi ý sơn lót, sơn phủ và định mức vật tư phù hợp để tối ưu chi phí thi công.</p>
            </div>
            <a class="btn btn-light" href="#lien-he">Liên hệ tư vấn</a>
          </div>
        </div>
      </section>
    </main>
{footer()}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
  </body>
</html>
"""


def category_products(category_file: str, products: list[dict]) -> list[dict]:
    return [item for item in products if item["category_file"] == category_file]


def render_category(category_file: str, products: list[dict]) -> str:
    meta = CATEGORY_META[category_file]
    items = category_products(category_file, products)
    title = f"{meta['title']} | Danh mục sản phẩm chính hãng"
    schema = [
        breadcrumb_schema([("Trang chủ", "index.html"), (meta["name"], category_file)]),
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": meta["title"],
            "description": meta["description"],
            "url": f"{SITE_URL}/{category_file}",
            "mainEntity": {
                "@type": "ItemList",
                "itemListElement": [
                    {"@type": "ListItem", "position": index + 1, "name": product["name"], "url": f"{SITE_URL}/{product['file']}"}
                    for index, product in enumerate(items)
                ],
            },
        },
    ]
    cards = "\n".join(
        f"""            <div class="col-md-6 col-xl-4">
              <article class="product-card d-flex flex-column">
                <a class="product-image-link" href="{esc(product['file'])}" aria-label="Xem {esc(product['name'])}">
                  <img src="{esc(product['image'])}" alt="{esc(product['name'])}">
                </a>
                <div class="product-card-body d-flex flex-column flex-grow-1">
                  <span class="product-badge">{esc(product['badge'])}</span>
                  <h2><a href="{esc(product['file'])}">{esc(product['name'])}</a></h2>
                  <p>{esc(product['description'])}</p>
                  <a class="btn btn-sm btn-outline-primary" href="{esc(product['file'])}">Xem chi tiết</a>
                </div>
              </article>
            </div>"""
        for product in items
    )
    use_cases = "".join(f"<li>{esc(item)}</li>" for item in meta["use_cases"])
    benefits = "".join(f"<li>{esc(item)}</li>" for item in meta["benefits"])
    return f"""<!doctype html>
<html lang="vi">
{head(title, meta['description'], category_file, "assets/sago-logo.png", schema)}
  <body>
{nav(category_file)}
    <main>
      <section class="category-hero">
        <div class="container">
          <div class="row align-items-end g-4">
            <div class="col-lg-8">
              <p class="section-kicker mb-3">{esc(meta['kicker'])}</p>
              <h1 class="category-title mb-4">{esc(meta['headline'])}</h1>
              <p class="category-description mb-0">{esc(meta['description'])}</p>
            </div>
            <div class="col-lg-4">
              <div class="hero-summary">
                <strong>{len(items)} sản phẩm</strong>
                <span>Được phân nhóm theo nhu cầu thi công thực tế.</span>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="section-padding bg-white" aria-labelledby="product-heading">
        <div class="container">
          <div class="row g-4 mb-5">
            <div class="col-lg-7">
              <p class="section-kicker mb-2">Sản phẩm Sago Paint</p>
              <h2 id="product-heading" class="h1 fw-bold mb-3">{esc(meta['heading'])}</h2>
              <p class="lead text-secondary mb-0">{esc(meta['seo'])}</p>
            </div>
            <div class="col-lg-5">
              <div class="category-guide">
                <div>
                  <h3>Ứng dụng phù hợp</h3>
                  <ul>{use_cases}</ul>
                </div>
                <div>
                  <h3>Lợi ích chính</h3>
                  <ul>{benefits}</ul>
                </div>
              </div>
            </div>
          </div>
          <div class="row g-4">
{cards}
          </div>
        </div>
      </section>
      <section class="seo-band">
        <div class="container">
          <div class="seo-panel">
            <div>
              <p class="section-kicker mb-2">Tối ưu vật tư</p>
              <h2 class="h3 mb-3">Chưa chắc nên dùng sản phẩm nào?</h2>
              <p class="mb-0">Gửi tình trạng bề mặt, diện tích và khu vực thi công để Sago Paint tư vấn hệ sơn, định mức và quy trình phù hợp.</p>
            </div>
            <a class="btn btn-light" href="#lien-he">Nhận tư vấn</a>
          </div>
        </div>
      </section>
    </main>
{footer()}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
  </body>
</html>
"""


def main() -> None:
    product_files = [path for path in ROOT.glob("*.html") if path.name not in CATEGORY_META and path.name != "index.html"]
    products = [extract_product(path) for path in sorted(product_files)]
    for product in products:
        (ROOT / product["file"]).write_text(render_product(product), encoding="utf-8", newline="\n")
    for category_file in CATEGORY_META:
        (ROOT / category_file).write_text(render_category(category_file, products), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
