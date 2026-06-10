from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "phong-thuy-son-nha"
SITE = "https://sagopaint.com"
S68_FILE = "sago-s-68-pro-chong-tham-a-nang-lo-thien-cao-cap.html"
S68_NAME = "SAGO S 68 PRO"


ELEMENTS = {
    "kim": {
        "name": "Kim",
        "slug": "menh-kim",
        "title": "Màu Sơn Hợp Mệnh Kim Cho Nhà Sang Trọng, Vượng Khí",
        "description": "Tư vấn màu sơn hợp mệnh Kim theo ngũ hành, phối màu hiện đại, tránh màu xung khắc và gợi ý S68 Pro cho nhà đẹp, bền màu, dễ vệ sinh.",
        "keywords": "màu sơn hợp mệnh kim, sơn nhà cho người mệnh kim, màu sơn phong thủy mệnh kim",
        "palette": ["trắng ấm", "ghi sáng", "vàng kem", "be ánh kim"],
        "avoid": ["đỏ rực", "hồng đậm", "cam cháy quá mạnh"],
        "intro": "Người mệnh Kim thường hợp với không gian sáng, gọn, có cảm giác sạch và sang. Khi chọn sơn nhà, nhóm màu trắng, ghi, be và vàng kem giúp căn nhà rộng hơn, dễ phối nội thất và vẫn giữ được tinh thần phong thủy ôn hòa.",
        "rooms": ["Phòng khách nên dùng trắng ấm hoặc ghi sáng làm nền chính, thêm điểm nhấn vàng kem ở mảng kệ tivi.", "Phòng ngủ hợp be sữa, trắng ngà hoặc ghi nhạt để giảm cảm giác lạnh.", "Mặt tiền có thể phối trắng kem với ghi đá để tạo vẻ hiện đại, ít lỗi thời."],
    },
    "moc": {
        "name": "Mộc",
        "slug": "menh-moc",
        "title": "Màu Sơn Hợp Mệnh Mộc Với Xanh Pastel Tươi Mát",
        "description": "Gợi ý màu sơn hợp mệnh Mộc như xanh lá pastel, xanh mint, olive nhạt cùng cách phối S68 Pro hài hòa cho từng không gian.",
        "keywords": "màu sơn hợp mệnh mộc, sơn nhà cho người mệnh mộc, màu sơn phong thủy mệnh mộc",
        "palette": ["xanh lá pastel", "xanh mint", "xanh olive nhạt", "xanh ngọc dịu"],
        "avoid": ["trắng lạnh quá nhiều", "ghi kim loại đậm", "vàng ánh kim"],
        "intro": "Mệnh Mộc gắn với sự sinh trưởng, mềm mại và gần thiên nhiên. Trong nhà ở hiện đại, màu xanh nên được tiết chế ở sắc độ pastel để không gian nhẹ mắt, dễ sống lâu dài và không bị nặng tính trang trí.",
        "rooms": ["Phòng khách có thể dùng xanh mint cho một mảng nhấn, nền còn lại giữ warm white.", "Phòng ngủ hợp xanh lá pastel hoặc xanh olive nhạt phối rèm be.", "Mặt tiền nên ưu tiên xanh xám rất nhạt, kết hợp trắng kem để tạo cảm giác sạch."],
    },
    "thuy": {
        "name": "Thủy",
        "slug": "menh-thuy",
        "title": "Màu Sơn Hợp Mệnh Thủy Với Xanh Biển, Xanh Xám",
        "description": "Chọn màu sơn hợp mệnh Thủy với xanh biển pastel, xanh xám, trắng kem, cách tránh màu xung khắc và giải pháp S68 Pro bền màu cho nhà hiện đại.",
        "keywords": "màu sơn hợp mệnh thủy, sơn nhà cho người mệnh thủy, màu sơn phong thủy mệnh thủy",
        "palette": ["xanh biển pastel", "xanh xám", "trắng kem", "ghi bạc nhạt"],
        "avoid": ["vàng đất đậm", "nâu nặng", "be quá sậm"],
        "intro": "Mệnh Thủy phù hợp các màu gợi sự lưu chuyển, thư thái và sáng thoáng. Xanh biển pastel, xanh xám và trắng kem giúp nhà có cảm giác mát, rộng, đặc biệt phù hợp căn hộ, nhà phố hẹp hoặc phòng ít ánh sáng.",
        "rooms": ["Phòng khách nên phối xanh xám ở mảng chính, trần và phào giữ trắng kem.", "Phòng ngủ dùng xanh biển pastel nhạt để tạo cảm giác thư giãn.", "Mặt tiền hợp xanh xám phối ghi nhạt, tránh dùng xanh quá đậm trên diện tích lớn."],
    },
    "hoa": {
        "name": "Hỏa",
        "slug": "menh-hoa",
        "title": "Màu Sơn Hợp Mệnh Hỏa Cho Nhà Ấm Áp, Tinh Tế Hơn",
        "description": "Tư vấn màu sơn hợp mệnh Hỏa với hồng pastel, cam nhạt, đỏ đất, màu nên tránh và cách dùng S68 Pro để nhà ấm, đẹp, không chói.",
        "keywords": "màu sơn hợp mệnh hỏa, sơn nhà cho người mệnh hỏa, màu sơn phong thủy mệnh hỏa",
        "palette": ["hồng pastel", "cam nhạt", "đỏ đất", "peach beige"],
        "avoid": ["xanh biển đậm", "đen", "xanh navy trên mảng lớn"],
        "intro": "Mệnh Hỏa có năng lượng mạnh nên khi đưa vào nhà ở cần chọn sắc độ ấm nhưng mềm. Hồng pastel, cam nhạt và đỏ đất dùng đúng tỷ lệ sẽ tạo cảm giác gần gũi, vui vẻ mà không gây mệt mắt.",
        "rooms": ["Phòng khách nên dùng peach beige làm nền, đỏ đất chỉ nên làm điểm nhấn nhỏ.", "Phòng ngủ hợp hồng phấn hoặc cam kem rất nhạt.", "Mặt tiền có thể phối be ấm với một mảng đỏ đất thấp để giữ vẻ cao cấp."],
    },
    "tho": {
        "name": "Thổ",
        "slug": "menh-tho",
        "title": "Màu Sơn Hợp Mệnh Thổ Với Vàng Kem, Be, Nâu Sáng",
        "description": "Gợi ý màu sơn hợp mệnh Thổ gồm vàng kem, be, nâu sáng, màu cần hạn chế và bảng phối S68 Pro cho nhà sang, ấm, dễ bảo trì.",
        "keywords": "màu sơn hợp mệnh thổ, sơn nhà cho người mệnh thổ, màu sơn phong thủy mệnh thổ",
        "palette": ["vàng kem", "be", "nâu sáng", "taupe nhạt"],
        "avoid": ["xanh lá quá nhiều", "xanh rêu đậm", "xanh neon"],
        "intro": "Mệnh Thổ hợp các gam màu ổn định, ấm và gần gũi. Vàng kem, be và nâu sáng đặc biệt phù hợp nhà Việt vì dễ phối gỗ, đá, ánh sáng vàng và phong cách modern luxury.",
        "rooms": ["Phòng khách nên dùng be hoặc vàng kem làm nền để tăng cảm giác rộng.", "Phòng ngủ hợp taupe nhạt, nâu sữa hoặc be hồng.", "Mặt tiền nên phối vàng kem với nâu sáng hoặc ghi ấm để bền thẩm mỹ."],
    },
}


AGES = {
    1990: ("Canh Ngọ", "Thổ", "Khảm", "vàng kem, be, nâu sáng", "xanh lá đậm"),
    1991: ("Tân Mùi", "Thổ", "Ly", "vàng kem, be, cam đất nhạt", "xanh rêu quá nhiều"),
    1992: ("Nhâm Thân", "Kim", "Cấn", "trắng ấm, ghi sáng, vàng kem", "đỏ rực"),
    1993: ("Quý Dậu", "Kim", "Đoài", "trắng kem, ghi nhạt, be ánh kim", "cam cháy"),
    1994: ("Giáp Tuất", "Hỏa", "Càn", "hồng pastel, cam nhạt, đỏ đất", "xanh navy"),
    1995: ("Ất Hợi", "Hỏa", "Khôn", "peach beige, hồng phấn, đỏ đất nhạt", "đen và xanh biển đậm"),
    1996: ("Bính Tý", "Thủy", "Tốn", "xanh biển pastel, xanh xám, trắng kem", "nâu đất đậm"),
    1997: ("Đinh Sửu", "Thủy", "Chấn", "xanh xám, ghi bạc, trắng ngà", "vàng đất nặng"),
    1998: ("Mậu Dần", "Thổ", "Khôn", "vàng kem, be, nâu sáng", "xanh lá đậm"),
    1999: ("Kỷ Mão", "Thổ", "Khảm", "be ấm, vàng kem, cam đất nhạt", "xanh rêu sậm"),
    2000: ("Canh Thìn", "Kim", "Ly", "trắng ấm, ghi sáng, vàng kem", "đỏ tươi trên diện rộng"),
}


MEDIA = {
    "pillar": {
        "src": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1400&q=82",
        "alt": "Phòng khách hiện đại với màu sơn pastel hợp phong thủy",
        "caption": "Không gian hiện đại dùng bảng màu pastel giúp nguyên lý ngũ hành trở nên nhẹ nhàng và dễ ứng dụng hơn.",
    },
    "kim": {
        "src": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=1400&q=82",
        "alt": "Nhà hiện đại màu trắng kem và ghi sáng hợp mệnh Kim",
        "caption": "Trắng ấm, ghi sáng và be ánh kim giúp mệnh Kim giữ vẻ sang trọng mà không làm không gian bị lạnh.",
    },
    "moc": {
        "src": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1400&q=82",
        "alt": "Không gian nội thất xanh pastel hợp mệnh Mộc",
        "caption": "Xanh mint, xanh sage và vật liệu gỗ tạo cảm giác gần thiên nhiên cho người mệnh Mộc.",
    },
    "thuy": {
        "src": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1400&q=82",
        "alt": "Phòng khách xanh xám và trắng kem hợp mệnh Thủy",
        "caption": "Xanh xám và trắng kem tạo cảm giác mát, thoáng, phù hợp nhà phố hoặc căn hộ ít ánh sáng.",
    },
    "hoa": {
        "src": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=1400&q=82",
        "alt": "Nội thất hồng pastel và cam nhạt hợp mệnh Hỏa",
        "caption": "Sắc hồng pastel và peach beige giúp mệnh Hỏa giữ năng lượng ấm áp nhưng không chói mắt.",
    },
    "tho": {
        "src": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=1400&q=82",
        "alt": "Không gian vàng kem be nâu sáng hợp mệnh Thổ",
        "caption": "Vàng kem, be và nâu sáng là nền màu bền thẩm mỹ, dễ phối gỗ và đá tự nhiên.",
    },
}


ROOM_MEDIA = [
    ("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=900&q=80", "Phòng khách hiện đại phối màu sơn phong thủy pastel", "Phòng khách"),
    ("https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=900&q=80", "Phòng ngủ dùng màu sơn nhẹ dịu hợp tuổi gia chủ", "Phòng ngủ"),
    ("https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=900&q=80", "Mặt tiền nhà hiện đại phối màu sơn bền đẹp", "Mặt tiền"),
]


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def rel(depth: int, path: str) -> str:
    return "../" * depth + path


def breadcrumb(items: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": f"{SITE}/{url}"}
            for i, (name, url) in enumerate(items)
        ],
    }


def faq_schema(faqs: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


def article_schema(title: str, description: str, url: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "author": {"@type": "Organization", "name": "Sago Paint"},
        "publisher": {"@type": "Organization", "name": "Sago Paint", "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/sago-logo.png"}},
        "mainEntityOfPage": f"{SITE}/{url}",
    }


def nav(depth: int) -> str:
    root = "../" * depth
    return f"""
    <header class="site-header fixed-top">
      <nav class="navbar navbar-expand-lg" aria-label="Điều hướng chính">
        <div class="container">
          <a class="navbar-brand" href="{root}index.html" aria-label="Sago Paint - Trang chủ">
            <img class="brand-logo" src="{root}assets/sago-logo.png" alt="Logo Sago Professional Coatings" loading="eager">
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNavigation" aria-controls="mainNavigation" aria-expanded="false" aria-label="Mở menu điều hướng">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="mainNavigation">
            <ul class="navbar-nav ms-auto align-items-lg-center">
              <li class="nav-item"><a class="nav-link" href="{root}index.html">Trang chủ</a></li>
              <li class="nav-item"><a class="nav-link" href="{root}son-noi-that.html">Nội thất</a></li>
              <li class="nav-item"><a class="nav-link" href="{root}son-ngoai-that.html">Ngoại thất</a></li>
              <li class="nav-item"><a class="nav-link" href="{root}son-chong-tham.html">Chống thấm</a></li>
              <li class="nav-item"><a class="nav-link active" href="{root}phong-thuy-son-nha/index.html">Phong thủy</a></li>
            </ul>
            <a class="btn btn-primary ms-lg-3 mt-3 mt-lg-0" href="#tu-van">Nhận tư vấn</a>
          </div>
        </div>
      </nav>
    </header>"""


def footer(depth: int) -> str:
    root = "../" * depth
    return f"""
    <footer id="tu-van" class="feng-footer">
      <div class="container">
        <div class="row g-4 align-items-center">
          <div class="col-lg-7">
            <img class="footer-logo mb-3" src="{root}assets/sago-logo.png" alt="Logo Sago Paint" loading="lazy">
            <h2>Nhận tư vấn màu sơn phong thủy cùng Sago Paint</h2>
            <p>Đội ngũ tư vấn giúp bạn chọn bảng màu hài hòa với mệnh, tuổi, ánh sáng thực tế và ngân sách thi công. S68 Pro được ưu tiên khi cần bề mặt bền đẹp, chống thấm lộ thiên, bền UV và chống bám bẩn.</p>
          </div>
          <div class="col-lg-5">
            <div class="cta-box">
              <strong>Hotline tư vấn miễn phí</strong>
              <a href="tel:+842812345678">028 1234 5678</a>
              <span>hello@sagopaint.com</span>
            </div>
          </div>
        </div>
      </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>"""


def head(title: str, description: str, url: str, depth: int, schemas: list[dict]) -> str:
    root = "../" * depth
    return f"""<!doctype html>
<html lang="vi">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(description)}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{SITE}/{url}">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(description)}">
    <meta property="og:image" content="{SITE}/assets/sago-logo.png">
    <meta property="og:url" content="{SITE}/{url}">
    <meta property="og:locale" content="vi_VN">
    <meta name="twitter:card" content="summary_large_image">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <link href="{root}phong-thuy-son-nha/styles.css" rel="stylesheet">
    <script type="application/ld+json">{json.dumps(schemas, ensure_ascii=False, indent=6)}</script>
  </head>"""


def product_highlight(depth: int) -> str:
    root = "../" * depth
    return f"""
      <section class="product-highlight" aria-labelledby="s68-heading">
        <div class="container">
          <div class="product-panel">
            <div>
              <p class="section-kicker">Sản phẩm ưu tiên</p>
              <h2 id="s68-heading">S68 Pro - giải pháp chống thấm cao cấp cho màu sơn phong thủy hiện đại</h2>
              <p>S68 Pro phù hợp khi gia chủ cần bảo vệ bề mặt lộ thiên, mặt tiền, ban công hoặc khu vực chịu ẩm; sản phẩm có độ bền cao, chống thấm, chống tia UV và hỗ trợ giữ vẻ đẹp công trình ổn định.</p>
              <div class="feature-grid">
                <span>Độ bền trên 15 năm</span><span>Chống tia UV</span><span>Chống thấm lộ thiên</span><span>Không cần pha trộn</span>
              </div>
              <a class="btn btn-primary" href="{root}{S68_FILE}">Nhận tư vấn S68 Pro</a>
            </div>
            <a class="product-packshot" href="{root}{S68_FILE}" aria-label="Xem chi tiết sản phẩm SAGO S 68 PRO">
              <img src="{root}assets/products/sago-s-68-pro-chong-tham-a-nang-lo-thien-cao-cap.png" alt="SAGO S 68 PRO chống thấm đa năng lộ thiên cao cấp" loading="lazy" width="520" height="620">
            </a>
          </div>
        </div>
      </section>"""


def element_links(depth: int) -> str:
    root = "../" * depth
    cards = "\n".join(
        f"""<a class="element-card element-{k}" href="{root}phong-thuy-son-nha/{v['slug']}/index.html">
          <span>Mệnh</span><strong>{v['name']}</strong><small>{", ".join(v['palette'][:3])}</small>
        </a>"""
        for k, v in ELEMENTS.items()
    )
    return f"<div class=\"element-grid\">{cards}</div>"


def age_links(depth: int) -> str:
    root = "../" * depth
    cards = "\n".join(
        f"""<a class="age-card" href="{root}phong-thuy-son-nha/tuoi-{year}/index.html"><strong>{year}</strong><span>{data[0]} - mệnh {data[1]}</span></a>"""
        for year, data in AGES.items()
    )
    return f"<div class=\"age-grid\">{cards}</div>"


def element_key_by_name(name: str) -> str:
    return next(key for key, item in ELEMENTS.items() if item["name"] == name)


def ages_for_element(element: str) -> list[int]:
    return [year for year, data in AGES.items() if data[1] == element]


def related_elements(depth: int, current_key: str | None = None, title: str = "Các Mệnh Khác") -> str:
    root = "../" * depth
    cards = []
    for key, item in ELEMENTS.items():
        if key == current_key:
            continue
        cards.append(
            f"""<a class="element-card element-{key}" href="{root}phong-thuy-son-nha/{item['slug']}/index.html">
          <span>Mệnh</span><strong>{item['name']}</strong><small>{", ".join(item['palette'][:3])}</small>
        </a>"""
        )
    return f"""
          <section class="related-block" aria-labelledby="related-elements-heading">
            <div class="section-heading-row">
              <div>
                <p class="section-kicker">Internal links</p>
                <h2 id="related-elements-heading">{title}</h2>
              </div>
              <a class="text-link" href="{root}phong-thuy-son-nha/index.html">Về trang Phong Thủy Sơn Nhà</a>
            </div>
            <div class="element-grid">{"".join(cards)}</div>
          </section>"""


def related_age_cards(depth: int, years: list[int], title: str = "Bài Viết Liên Quan") -> str:
    root = "../" * depth
    if not years:
        years = [1990, 1992, 1994, 1996, 1998, 2000]
    cards = "\n".join(
        f"""<a class="age-card" href="{root}phong-thuy-son-nha/tuoi-{year}/index.html"><strong>{year}</strong><span>{AGES[year][0]} - mệnh {AGES[year][1]}</span></a>"""
        for year in years
    )
    return f"""
          <section class="related-block" aria-labelledby="related-articles-heading">
            <div class="section-heading-row">
              <div>
                <p class="section-kicker">Bài viết liên quan</p>
                <h2 id="related-articles-heading">{title}</h2>
              </div>
            </div>
            <div class="age-grid">{cards}</div>
          </section>"""


def product_recommendations(depth: int) -> str:
    root = "../" * depth
    return f"""
          <section class="related-block product-links" aria-labelledby="recommended-products-heading">
            <div class="section-heading-row">
              <div>
                <p class="section-kicker">Sản phẩm gợi ý</p>
                <h2 id="recommended-products-heading">Sản phẩm sơn nên dùng</h2>
              </div>
            </div>
            <div class="recommend-grid">
              <a class="recommend-card primary-recommend" href="{root}{S68_FILE}"><strong>S68 Pro</strong><span>Sản phẩm chống thấm cao cấp ưu tiên cho mặt tiền, ban công và bề mặt lộ thiên.</span></a>
              <a class="recommend-card" href="{root}son-noi-that.html"><strong>Sơn nội thất</strong><span>Phù hợp phòng khách, phòng ngủ và căn hộ.</span></a>
              <a class="recommend-card" href="{root}son-chong-tham.html"><strong>Sơn chống thấm</strong><span>Bổ trợ cho mặt tiền, ban công và khu vực ẩm.</span></a>
            </div>
          </section>"""


def hub_links(depth: int) -> str:
    root = "../" * depth
    return f"""
          <div class="quick-links" aria-label="Liên kết điều hướng nhanh">
            <a href="{root}index.html">Về trang chủ</a>
            <a href="{root}phong-thuy-son-nha/index.html">Về hub Phong Thủy Sơn Nhà</a>
            <a href="{root}{S68_FILE}">Xem S68 Pro</a>
          </div>"""


def article_media(key: str, title: str | None = None) -> str:
    media = MEDIA[key]
    heading = title or "Gợi ý hình ảnh phối màu thực tế"
    return f"""
          <figure class="article-media">
            <img src="{media['src']}" alt="{esc(media['alt'])}" loading="lazy" width="1400" height="820">
            <figcaption><strong>{heading}</strong><span>{media['caption']}</span></figcaption>
          </figure>"""


def room_media_grid(subject: str) -> str:
    cards = "\n".join(
        f"""<figure>
              <img src="{src}" alt="{esc(alt)} cho {esc(subject)}" loading="lazy" width="900" height="650">
              <figcaption>{label}</figcaption>
            </figure>"""
        for src, alt, label in ROOM_MEDIA
    )
    return f"""
          <div class="room-media-grid" aria-label="Hình ảnh gợi ý màu sơn theo không gian cho {esc(subject)}">
            {cards}
          </div>"""


def practical_advice(subject: str, colors: str, avoid: str) -> str:
    return f"""
          <h2>Nguyên tắc phối màu 60-30-10 cho {subject}</h2>
          <p>Quy tắc 60-30-10 giúp bảng màu phong thủy dễ ứng dụng hơn trong nhà thật. Khoảng 60 phần trăm nên là màu nền sáng, 30 phần trăm là màu phụ cùng tông hoặc trung tính, 10 phần trăm còn lại là điểm nhấn. Với {subject}, nhóm màu nên ưu tiên là {colors}; tuy nhiên chỉ một phần trong nhóm này cần xuất hiện rõ, phần còn lại có thể được làm mềm bằng trắng ấm, be hoặc ghi nhạt.</p>
          <p>Khi dùng quy tắc này, gia chủ tránh được lỗi chọn màu hợp phong thủy nhưng quá dày đặc. Một căn phòng toàn màu mạnh thường khó nghỉ ngơi, khó phối nội thất và dễ cũ sau vài năm. Ngược lại, nền trung tính kết hợp một mảng hợp mệnh sẽ tạo cảm giác sang, có chiều sâu và vẫn giữ được ý nghĩa phong thủy.</p>
          <h2>Đánh giá ánh sáng trước khi chốt màu</h2>
          <p>Ánh sáng quyết định màu sơn sau khi hoàn thiện. Nhà hướng Tây thường làm màu ấm trở nên đậm hơn vào buổi chiều, trong khi phòng ít cửa sổ khiến màu xanh hoặc ghi dễ bị lạnh. Vì vậy, cùng một bảng màu {colors}, phòng nhiều nắng nên giảm độ bão hòa, còn phòng thiếu sáng nên chọn sắc độ sáng và có nền kem.</p>
          <p>Trước khi thi công toàn bộ, nên sơn thử tối thiểu hai mảng mẫu ở vị trí nhận ánh sáng khác nhau. Quan sát vào buổi sáng, trưa và tối dưới đèn thực tế. Đây là bước quan trọng hơn việc chỉ xem màu trên màn hình, vì màn hình thường làm màu sáng và trong hơn so với bề mặt tường thật.</p>
          <h2>Phối màu theo vật liệu nội thất</h2>
          <p>Nếu nhà dùng nhiều gỗ tự nhiên, màu tường nên mềm và ít vàng hơn để tránh không gian bị nóng. Nếu sàn là gạch sáng hoặc đá vân lạnh, có thể thêm be, peach hoặc xanh sage để cân bằng. Với nội thất kim loại, kính và đá, nhóm màu pastel giúp giảm cảm giác cứng, đồng thời giữ tinh thần modern luxury.</p>
          <p>Gia chủ cũng nên xét màu cửa, rèm, sofa và tủ bếp trước khi chọn sơn. Màu tường là nền cho toàn bộ vật dụng, không nên cạnh tranh với mọi chi tiết. Khi còn phân vân, chọn nền warm white hoặc soft beige, sau đó đưa màu hợp phong thủy vào mảng nhấn sẽ an toàn hơn.</p>
          <h2>Lưu ý màu cần hạn chế</h2>
          <p>Nhóm màu nên hạn chế với {subject} là {avoid}. Hạn chế ở đây không phải cấm tuyệt đối, mà là không dùng làm màu phủ diện rộng nếu nó khiến không gian mất cân bằng. Trong nhiều công trình, màu tương khắc vẫn có thể xuất hiện ở tranh, chậu cây, đèn, ghế đơn hoặc vật dụng dễ thay đổi.</p>
          <p>Cách xử lý này giúp phong thủy đi cùng thẩm mỹ. Một ngôi nhà đẹp cần sự hài hòa, sạch sẽ, thông thoáng và phù hợp sinh hoạt. Nếu màu hợp mệnh gây tối phòng, làm trần thấp hoặc khiến gia chủ nhanh chán, nên ưu tiên phiên bản nhạt hơn thay vì cố dùng màu nguyên bản.</p>
          <h2>Chuẩn bị bề mặt và hệ sơn</h2>
          <p>Phong thủy màu sắc chỉ phát huy tốt khi bề mặt tường phẳng, khô, ít nứt và không bị thấm. Trước lớp phủ hoàn thiện, cần kiểm tra độ ẩm, xử lý kiềm, trám vá vết nứt và dùng sơn lót phù hợp. Nếu bỏ qua bước nền, màu đẹp ban đầu vẫn có thể loang, bong hoặc xuống cấp nhanh.</p>
          <p>S68 Pro được đề xuất làm lớp phủ chính trong cụm tư vấn này vì đáp ứng nhu cầu bề mặt mịn, bền màu, chống bám bẩn, hỗ trợ chống thấm và dễ lau chùi. Với khu vực ngoài trời, ban công hoặc mảng tường chịu ẩm, nên kết hợp thêm giải pháp chống thấm chuyên dụng trước khi hoàn thiện màu.</p>
          <p>Sau khi hoàn thiện, nên lưu lại mã màu, lô sơn và khu vực đã thi công để dễ bảo trì. Với nhà có trẻ nhỏ, thú cưng hoặc khu vực sinh hoạt đông người, ưu tiên màng sơn dễ lau chùi sẽ giúp màu phong thủy duy trì cảm giác sạch đẹp lâu hơn, thay vì chỉ đẹp trong giai đoạn bàn giao.</p>
          <p>Cuối cùng, hãy xem màu sơn như một quyết định dài hạn. Một bảng màu tốt phải làm gia chủ thấy dễ chịu mỗi ngày, giúp không gian sáng hơn, đồ nội thất đẹp hơn và giảm công bảo dưỡng. Khi các yếu tố đó được đáp ứng, ý nghĩa phong thủy sẽ trở nên tự nhiên và thuyết phục hơn.</p>
    """


def visible_faq(faqs: list[tuple[str, str]]) -> str:
    items = "\n".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs)
    return f"<section class=\"faq-block\"><h2>Câu hỏi thường gặp</h2>{items}</section>"


def page(title: str, description: str, url: str, depth: int, body: str, crumbs: list[tuple[str, str]], faqs: list[tuple[str, str]]) -> str:
    schemas = [breadcrumb(crumbs), article_schema(title, description, url), faq_schema(faqs)]
    return head(title, description, url, depth, schemas) + f"""
  <body>
    {nav(depth)}
    <main>
      {body}
    </main>
    {footer(depth)}
  </body>
</html>
"""


def pillar() -> str:
    title = "Phong Thủy Sơn Nhà: Chọn Màu Hợp Mệnh, Hợp Tuổi"
    desc = "Hướng dẫn chọn màu sơn nhà hợp phong thủy theo mệnh, tuổi, không gian sống và gợi ý S68 Pro bền đẹp, hiện đại, dễ vệ sinh."
    faqs = [
        ("Chọn màu sơn nhà theo phong thủy có cần tuyệt đối không?", "Không. Phong thủy màu sắc nên được xem như nguyên tắc tham khảo để tạo cảm giác hài hòa, không thay thế các yếu tố ánh sáng, kiến trúc và sở thích sống."),
        ("S68 Pro phù hợp với phong cách màu pastel không?", "Có. S68 Pro được định vị cho bề mặt mịn, bền màu, dễ vệ sinh nên phù hợp các bảng màu pastel cần độ hoàn thiện sạch và tinh tế."),
        ("Nên chọn màu theo mệnh hay theo tuổi?", "Có thể kết hợp cả hai. Mệnh giúp xác định nhóm màu chính, tuổi giúp tinh chỉnh sắc độ và cách phối theo từng không gian."),
    ]
    body = f"""
      <section class="feng-hero">
        <div class="container">
          <div class="row align-items-center g-5">
            <div class="col-lg-7">
              <nav class="breadcrumb-wrap" aria-label="breadcrumb"><a href="../index.html">Trang chủ</a><span>/</span><strong>Phong thủy sơn nhà</strong></nav>
              <p class="section-kicker">Modern Feng Shui Paint Guide</p>
              <h1>Phong Thủy Sơn Nhà - Chọn Màu Sơn Hợp Mệnh, Hợp Tuổi Để Thu Hút Tài Lộc</h1>
              <p class="hero-copy">Màu sơn quyết định cảm xúc đầu tiên của ngôi nhà và là lớp nền quan trọng cho ánh sáng, nội thất, vật liệu. Khi vận dụng ngũ hành một cách thực tế, gia chủ có thể chọn bảng màu vừa hợp phong thủy phổ biến, vừa đẹp lâu dài và dễ thi công.</p>
              <div class="hero-actions"><a class="btn btn-primary" href="#tu-van">Tư vấn miễn phí</a><a class="btn btn-outline-primary" href="#ngu-hanh">Xem màu theo mệnh</a></div>
            </div>
            <div class="col-lg-5">
              <div class="hero-visual" role="img" aria-label="Ngôi nhà hiện đại với bảng màu ngũ hành pastel">
                <div class="house-shape"></div>
                <div class="element-orbit"><span>Kim</span><span>Mộc</span><span>Thủy</span><span>Hỏa</span><span>Thổ</span></div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="content-section">
        <div class="container narrow">
          <h2>Vai trò của màu sơn trong phong thủy nhà ở</h2>
          <p>Màu sơn là diện tích thị giác lớn nhất trong nhà. Một căn phòng có bố cục đẹp nhưng màu tường quá gắt vẫn dễ gây căng thẳng; ngược lại, màu nền đúng sắc độ có thể làm đồ nội thất nổi bật hơn, ánh sáng dịu hơn và sinh hoạt hằng ngày thoải mái hơn.</p>
          <p>Trong phong thủy ứng dụng, màu sắc được liên hệ với ngũ hành để tạo cảm giác cân bằng. Cách tiếp cận phù hợp nhất là không cực đoan: chọn nhóm màu chủ đạo theo mệnh, sau đó điều chỉnh theo hướng nhà, lượng nắng, diện tích phòng và phong cách nội thất.</p>
          {article_media("pillar", "Bảng màu phong thủy hiện đại cho nhà Việt")}
          <h2>Ý nghĩa ngũ hành trong thiết kế nhà ở</h2>
          <p>Kim gợi sự sáng, sạch, tinh tế; Mộc gợi sinh khí và thiên nhiên; Thủy tạo cảm giác mát, sâu và linh hoạt; Hỏa đem lại năng lượng ấm áp; Thổ tạo nền ổn định, vững chãi. Một ngôi nhà đẹp thường không dùng một hành duy nhất mà phối các hành theo tỷ lệ hợp lý.</p>
          <p>Với nhà phố Việt Nam, bảng màu pastel như sage green, warm white, soft beige, pastel blue và pastel peach giúp cân bằng giữa thẩm mỹ hiện đại và nguyên lý ngũ hành. Những màu này cũng dễ lên hình, dễ chọn rèm, sofa, sàn gỗ và đèn.</p>
          <h2>Cách chọn màu sơn theo mệnh</h2>
          <p>Gia chủ nên chọn một màu nền chiếm khoảng 60 phần trăm diện tích, một màu phụ khoảng 30 phần trăm và màu nhấn khoảng 10 phần trăm. Màu hợp mệnh nên xuất hiện ở nền hoặc mảng nhấn có chủ đích, thay vì phủ toàn bộ căn nhà bằng một màu quá mạnh.</p>
          {element_links(1)}
          <h2>Cách chọn màu sơn theo tuổi</h2>
          <p>Nhóm bài theo năm sinh giúp bạn đi nhanh hơn từ thông tin can chi, mệnh, cung tham khảo đến bảng màu cụ thể cho phòng khách, phòng ngủ và mặt tiền. Đây là hướng dẫn thực tế, không khuyến khích chọn màu chỉ vì may mắn mà bỏ qua ánh sáng và công năng.</p>
          {age_links(1)}
          <h2>Các sai lầm khi chọn màu sơn phong thủy</h2>
          <p>Sai lầm phổ biến nhất là dùng màu tương sinh quá đậm trên toàn bộ tường. Ví dụ người mệnh Hỏa dùng đỏ tươi khắp phòng khách, hoặc người mệnh Mộc dùng xanh lá sậm trên cả trần và tường. Kết quả thường là không gian nặng, khó phối đồ và nhanh lỗi thời.</p>
          <p>Sai lầm thứ hai là bỏ qua chất lượng màng sơn. Màu đẹp chỉ thật sự hiệu quả khi bề mặt đều, ít bám bẩn, chống thấm tốt và giữ màu ổn định. Vì vậy, với các bảng màu phong thủy cần độ tinh tế, S68 Pro nên được ưu tiên trong lớp sơn hoàn thiện.</p>
          <h2>Quy trình chọn màu sơn phong thủy thực tế</h2>
          <p>Bước đầu tiên là xác định nhóm màu theo mệnh hoặc tuổi, sau đó loại bỏ các màu không phù hợp với ánh sáng và diện tích nhà. Với nhà nhỏ, hãy ưu tiên màu sáng, độ bão hòa thấp và trần trắng ấm. Với nhà rộng, có thể dùng mảng nhấn đậm hơn nhưng vẫn nên giữ tỷ lệ vừa phải.</p>
          <p>Bước thứ hai là đối chiếu với nội thất. Sofa, sàn, rèm, tủ bếp và cửa chiếm nhiều diện tích thị giác nên phải được xem chung với màu tường. Nếu nội thất đã nổi bật, màu sơn nên đóng vai trò nền. Nếu nội thất tối giản, có thể dùng màu hợp mệnh ở một mảng lớn hơn để tạo cá tính.</p>
          <p>Bước thứ ba là sơn thử mẫu. Không nên quyết định chỉ bằng catalogue hoặc hình ảnh trên điện thoại. Mẫu sơn cần được xem dưới ánh sáng tự nhiên và ánh sáng đèn trong ít nhất một ngày, vì màu pastel có thể thay đổi khá nhiều theo thời điểm.</p>
          <h2>Gợi ý màu theo từng không gian</h2>
          <p>Phòng khách nên sáng, thoáng và có một điểm nhấn rõ. Đây là nơi phù hợp để thể hiện màu hợp mệnh nhưng vẫn cần dễ tiếp khách và dễ phối đồ. Warm white, soft beige, sage green, pastel blue và pastel peach là những nền màu an toàn cho nhiều phong cách.</p>
          <p>Phòng ngủ nên giảm tương phản, giảm màu nóng và ưu tiên cảm giác thư giãn. Dù gia chủ hợp Hỏa, màu đỏ hoặc cam vẫn nên chuyển thành hồng phấn, peach beige hoặc đỏ đất rất nhạt. Dù gia chủ hợp Thủy, xanh biển cũng nên dùng ở sắc độ pastel thay vì xanh đậm.</p>
          <p>Mặt tiền cần cân bằng phong thủy với độ bền thẩm mỹ. Những màu quá rực dễ nhanh cũ dưới nắng mưa. Nên dùng nhóm kem, be, ghi ấm, xanh xám hoặc nâu sáng làm nền, sau đó đưa màu hợp mệnh vào chi tiết cổng, lam, ban công hoặc mảng tường phụ.</p>
          <h2>Sản phẩm và hệ thi công nên đi cùng màu phong thủy</h2>
          <p>Chọn đúng màu nhưng dùng sai hệ sơn sẽ làm giảm hiệu quả hoàn thiện. Tường mới cần sơn lót chống kiềm, tường cũ cần xử lý bong tróc và nấm mốc, khu vực ẩm cần chống thấm trước khi phủ màu. Đây là nền tảng giúp màu sắc lên đều và giữ được cảm giác sạch.</p>
          <p>S68 Pro là sản phẩm được ưu tiên trong cụm nội dung này vì phù hợp vai trò lớp phủ hoàn thiện cao cấp. Khi cần hệ đầy đủ, có thể kết hợp S68 Pro với sơn lót, bột trét hoặc chống thấm trong danh mục Sago Paint tùy tình trạng công trình. Cách tư vấn này giúp 70 phần trăm trọng tâm vẫn dành cho S68 Pro, nhưng không bỏ qua các lớp nền cần thiết.</p>
          <p>Với khách hàng đang chuẩn bị xây mới hoặc cải tạo, nên đặt lịch tư vấn trước khi chốt vật liệu nội thất. Khi bảng màu, bề mặt tường và sản phẩm sơn được quyết định cùng nhau, công trình thường ít phát sinh hơn và tổng thể hoàn thiện đồng bộ hơn.</p>
          <p>Nếu cần triển khai nhanh, gia chủ có thể bắt đầu từ ba lựa chọn an toàn: một màu nền sáng, một màu hợp mệnh ở sắc độ pastel và một màu nhấn nhỏ. Sau đó đội tư vấn sẽ tinh chỉnh theo hướng nhà, ảnh chụp hiện trạng và nhu cầu sử dụng thực tế.</p>
          <p>Cách làm này giúp quá trình chọn màu bớt cảm tính và dễ thống nhất giữa các thành viên trong gia đình. Thay vì tranh luận theo sở thích riêng, mọi người có một khung tham chiếu rõ ràng: màu hợp ngũ hành, màu hợp ánh sáng, màu hợp nội thất và sản phẩm sơn đủ bền cho sinh hoạt lâu dài.</p>
          {hub_links(1)}
          {related_age_cards(1, [1990, 1992, 1994, 1996, 1998, 2000], "Bài Viết Theo Năm Sinh Nổi Bật")}
          {product_recommendations(1)}
          {visible_faq(faqs)}
        </div>
      </section>
      {product_highlight(1)}
    """
    return page(title, desc, "phong-thuy-son-nha/", 1, body, [("Trang chủ", "index.html"), ("Phong thủy sơn nhà", "phong-thuy-son-nha/")], faqs)


def element_page(key: str, item: dict) -> str:
    title = item["title"]
    desc = item["description"]
    slug = item["slug"]
    faqs = [
        (f"Mệnh {item['name']} nên sơn màu gì?", f"Mệnh {item['name']} nên ưu tiên {', '.join(item['palette'][:3])}, đồng thời chọn sắc độ nhẹ để căn nhà dễ sống lâu dài."),
        (f"Mệnh {item['name']} có nên dùng màu tương khắc không?", "Có thể dùng ở tỷ lệ nhỏ nếu phù hợp nội thất, nhưng không nên dùng làm màu nền chính cho toàn bộ nhà."),
        ("S68 Pro có phù hợp với bảng màu này không?", "Có. S68 Pro phù hợp các bảng màu pastel và trung tính cần bề mặt mịn, chống bám bẩn, hỗ trợ chống thấm và giữ màu ổn định."),
    ]
    body = f"""
      <section class="feng-hero compact">
        <div class="container">
          <nav class="breadcrumb-wrap" aria-label="breadcrumb"><a href="../../index.html">Trang chủ</a><span>/</span><a href="../index.html">Phong thủy sơn nhà</a><span>/</span><strong>Mệnh {item['name']}</strong></nav>
          <p class="section-kicker">{item['keywords']}</p>
          <h1>{title}</h1>
          <p class="hero-copy">{item['intro']}</p>
        </div>
      </section>
      <section class="content-section">
        <div class="container narrow">
          <h2>Đặc điểm người mệnh {item['name']} khi chọn màu nhà</h2>
          <p>{item['intro']} Khi tư vấn màu, Sago Paint luôn xem phong thủy là một lớp tham khảo bên cạnh kiến trúc, hướng sáng và thói quen sử dụng. Cùng một mệnh nhưng nhà nhiều nắng sẽ cần sắc độ khác nhà thiếu sáng.</p>
          <p>Với phong cách modern luxury, nhóm màu hợp mệnh nên được làm mềm bằng warm white, soft beige hoặc ghi ấm. Cách phối này giúp căn nhà cao cấp hơn, tránh cảm giác màu phong thủy bị phô hoặc quá cá nhân.</p>
          {article_media(key, "Không gian tham khảo cho mệnh " + item["name"])}
          <h2>Màu tương sinh và tương hợp</h2>
          <p>Nhóm màu nên ưu tiên cho mệnh {item['name']} gồm {', '.join(item['palette'])}. Đây là các màu dễ dùng cho tường lớn, đặc biệt khi chọn sắc độ pastel hoặc trung tính ấm. Nếu muốn điểm nhấn, chỉ nên dùng ở vách tivi, đầu giường, hốc trang trí hoặc mảng mặt tiền nhỏ.</p>
          <div class="swatch-row">{"".join(f"<span>{c}</span>" for c in item["palette"])}</div>
          <h2>Màu cần tránh</h2>
          <p>Các màu nên hạn chế gồm {', '.join(item['avoid'])}. Hạn chế không có nghĩa là tuyệt đối kiêng kỵ; vấn đề là tỷ lệ. Nếu gia chủ yêu thích một màu mạnh, có thể chuyển sang sắc độ đất, pastel hoặc dùng qua vật dụng rời để dễ thay đổi.</p>
          <h2>Gợi ý phối màu nội thất</h2>
          <p>{item['rooms'][0]} {item['rooms'][1]} {item['rooms'][2]} Nên đặt mẫu sơn dưới ánh sáng thật trong ít nhất một ngày trước khi quyết định, vì màu trên catalogue thường khác màu khi lên tường.</p>
          <p>Để tối ưu chuyển đổi và trải nghiệm sử dụng, S68 Pro được gợi ý cho các mảng tường chính nhờ bề mặt mịn, chống bám bẩn, hỗ trợ chống thấm và dễ vệ sinh. Các sản phẩm lót, chống thấm hoặc bột trét khác nên dùng bổ trợ theo tình trạng nền tường.</p>
          {practical_advice("mệnh " + item['name'], ", ".join(item['palette']), ", ".join(item['avoid']))}
          <h2>Liên kết nhanh theo tuổi</h2>
          {related_age_cards(2, ages_for_element(item["name"]), "Bài Viết Theo Tuổi Cùng Mệnh " + item["name"])}
          {hub_links(2)}
          {related_elements(2, key)}
          {product_recommendations(2)}
          {visible_faq(faqs)}
        </div>
      </section>
      {product_highlight(2)}
    """
    return page(title, desc, f"phong-thuy-son-nha/{slug}/", 2, body, [("Trang chủ", "index.html"), ("Phong thủy sơn nhà", "phong-thuy-son-nha/"), (f"Mệnh {item['name']}", f"phong-thuy-son-nha/{slug}/")], faqs)


def age_page(year: int, data: tuple[str, str, str, str, str]) -> str:
    can_chi, element, cung, colors, avoid = data
    title = f"Người Sinh Năm {year} Sơn Nhà Màu Gì Hút Tài Lộc?"
    desc = f"Tư vấn tuổi {year} {can_chi} mệnh {element} nên sơn nhà màu gì, màu cần tránh, phối phòng khách, phòng ngủ, mặt tiền và gợi ý S68 Pro."
    element_key = next(k for k, v in ELEMENTS.items() if v["name"] == element)
    faqs = [
        (f"Tuổi {year} sơn màu trắng được không?", f"Tuổi {year} có thể dùng trắng nếu phối đúng sắc độ. Với mệnh {element}, nên kết hợp trắng ấm hoặc trắng kem để không gian dịu và dễ phối nội thất."),
        (f"Tuổi {year} hợp màu xanh không?", f"Màu xanh cần xét theo mệnh {element}. Nếu không phải màu chủ đạo phù hợp, vẫn có thể dùng xanh pastel ở cây, tranh, rèm hoặc mảng nhấn nhỏ."),
        ("Sơn nhà màu nào giúp tăng tài lộc?", f"Nên ưu tiên nhóm {colors}, kết hợp ánh sáng tốt, bố cục gọn và lớp sơn bền màu như S68 Pro để tạo cảm giác sáng sủa, ổn định."),
    ]
    body = f"""
      <section class="feng-hero compact">
        <div class="container">
          <nav class="breadcrumb-wrap" aria-label="breadcrumb"><a href="../../index.html">Trang chủ</a><span>/</span><a href="../index.html">Phong thủy sơn nhà</a><span>/</span><strong>Tuổi {year}</strong></nav>
          <p class="section-kicker">{can_chi} {year} - mệnh {element}</p>
          <h1>Người Sinh Năm {year} Sơn Nhà Màu Gì Để Hút Tài Lộc Và May Mắn?</h1>
          <p class="hero-copy">Gợi ý màu sơn cho tuổi {year} dựa trên ngũ hành phổ biến, đồng thời điều chỉnh theo kiến trúc nhà Việt, ánh sáng tự nhiên và nhu cầu bảo trì thực tế.</p>
        </div>
      </section>
      <section class="content-section">
        <div class="container narrow">
          <h2>Tổng quan tuổi {year}</h2>
          <p>Người sinh năm {year} là tuổi {can_chi}, mệnh {element}, cung tham khảo {cung}. Khi chọn màu sơn, thông tin này giúp xác định nhóm màu nên ưu tiên, nhưng quyết định cuối cùng vẫn cần xét diện tích phòng, hướng nắng, màu sàn, màu cửa và phong cách nội thất.</p>
          <p>Với nhà ở hiện đại, mục tiêu không phải biến toàn bộ căn nhà thành một màu hợp tuổi, mà tạo bảng màu cân bằng. Màu hợp tuổi nên làm nền hoặc điểm nhấn chủ đạo; màu trung tính như warm white, soft beige và ghi ấm giúp bảng màu sạch, sang và ít lỗi thời.</p>
          {article_media(element_key, "Bảng màu tham khảo cho tuổi " + str(year))}
          <h2>Màu tương sinh</h2>
          <p>Tuổi {year} nên ưu tiên nhóm {colors}. Các màu này có thể dùng cho phòng khách, phòng ngủ, mặt tiền hoặc hành lang nếu chọn sắc độ vừa phải. Với diện tích nhỏ, nên dùng màu sáng hơn catalogue một đến hai tông để tránh cảm giác bí.</p>
          <h2>Màu tương hợp</h2>
          <p>Màu tương hợp nên xuất hiện ở mảng tường chính, rèm, sofa hoặc vật liệu gỗ đá đi kèm. Nếu gia chủ thích phong cách minimal, hãy chọn một màu nền ấm, một màu phụ cùng tông và một màu nhấn rất tiết chế.</p>
          <h2>Màu nên tránh</h2>
          <p>Tuổi {year} nên hạn chế {avoid} trên diện tích lớn. Nếu vẫn muốn dùng, hãy chuyển sang sắc độ pastel hoặc đặt ở chi tiết nhỏ. Điều này giúp giữ tinh thần phong thủy mà không làm căn nhà nặng mắt.</p>
          <h2>Gợi ý phối màu</h2>
          <p>Phòng khách nên dùng màu sáng thuộc nhóm {colors}, phối trần trắng ấm để tăng độ cao thị giác. Phòng ngủ nên giảm độ bão hòa để dễ nghỉ ngơi. Mặt tiền cần ưu tiên màu bền thẩm mỹ, ít bám bẩn và hài hòa với cảnh quan xung quanh.</p>
          {room_media_grid("tuổi " + str(year))}
          <h3>Màu phòng khách</h3>
          <p>Phòng khách là nơi tiếp nhận nhiều ánh sáng và thể hiện cá tính gia chủ. Với tuổi {year}, nên dùng nền trung tính ấm, thêm một mảng màu hợp mệnh phía sau sofa hoặc kệ tivi. S68 Pro phù hợp khu vực này vì dễ lau chùi khi có bụi, vết tay hoặc sinh hoạt gia đình.</p>
          <h3>Màu phòng ngủ</h3>
          <p>Phòng ngủ cần dịu hơn phòng khách. Hãy chọn phiên bản pastel của nhóm màu hợp tuổi, tránh tương phản quá mạnh. Ánh sáng đèn vàng ấm sẽ giúp màu tường mềm hơn vào buổi tối.</p>
          <h3>Màu mặt tiền</h3>
          <p>Mặt tiền nên chọn màu hợp tuổi nhưng vẫn bền với thời gian. Các tông kem, be, ghi ấm hoặc xanh xám nhạt thường dễ bảo trì hơn màu quá rực. Nếu khu vực chịu mưa nắng, nên kết hợp xử lý chống thấm và lớp phủ chất lượng.</p>
          <h2>Gợi ý sản phẩm</h2>
          <p>S68 Pro là lựa chọn ưu tiên cho tuổi {year} khi cần màu lên đều, bề mặt mịn, chống bám bẩn, hỗ trợ chống thấm và tạo cảm giác cao cấp. Các sản phẩm khác như sơn lót, bột trét, chống thấm chuyên dụng nên dùng theo nền tường thực tế để tăng tuổi thọ hệ sơn.</p>
          <h2>Đọc thêm theo mệnh</h2>
          <p><a href="../{ELEMENTS[element_key]['slug']}/index.html">Xem hướng dẫn màu sơn hợp mệnh {element}</a> để đối chiếu thêm bảng màu, màu cần tránh và cách phối nội thất.</p>
          {practical_advice("tuổi " + str(year), colors, avoid)}
          {hub_links(2)}
          {related_age_cards(2, [y for y in ages_for_element(element) if y != year], "Bài Viết Liên Quan Cùng Mệnh " + element)}
          {related_elements(2, element_key, "Mệnh Liên Quan Khác")}
          {product_recommendations(2)}
          {visible_faq(faqs)}
        </div>
      </section>
      {product_highlight(2)}
    """
    return page(title, desc, f"phong-thuy-son-nha/tuoi-{year}/", 2, body, [("Trang chủ", "index.html"), ("Phong thủy sơn nhà", "phong-thuy-son-nha/"), (f"Tuổi {year}", f"phong-thuy-son-nha/tuoi-{year}/")], faqs)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> None:
    write(OUT / "index.html", pillar())
    for key, item in ELEMENTS.items():
        write(OUT / item["slug"] / "index.html", element_page(key, item))
    for year, data in AGES.items():
        write(OUT / f"tuoi-{year}" / "index.html", age_page(year, data))


if __name__ == "__main__":
    main()

