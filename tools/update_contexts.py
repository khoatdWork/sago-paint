"""Refresh page context from source. Run explicitly after checking source changes."""
from pathlib import Path
from site_content import ROOT, Page, context_path, inventory, schema_types


def describe(entry, page):
    route, file = entry["route"], entry["file"]
    types = schema_types(page.schemas)
    if route == "/":
        return "Trang chủ", "Giới thiệu thương hiệu và dẫn khách tới đúng hệ sơn", "Chủ nhà, thợ sơn và khách công trình", "So sánh giải pháp sơn Sago Paint và tìm nơi tư vấn", "HTML biên tập trực tiếp"
    if route == "/tinh-son/":
        return "Công cụ", "Ước tính diện tích, lượng sơn và chi phí tham khảo", "Người chuẩn bị thi công và cần dự toán", "Tính lượng sơn cần dùng trước khi hỏi báo giá", "HTML trực tiếp; assets/js/paint-calculator.js"
    if route in ("/son-noi-that", "/son-ngoai-that", "/son-chong-tham"):
        return "Danh mục", "Chọn và so sánh sản phẩm trong hệ sơn", "Người đang lựa chọn hệ sơn", page.title, "tools/refresh_pages.py — CATEGORY_META/render_category"
    if "Product" in types:
        return "Sản phẩm", "Hiểu ứng dụng, đặc tính và cách thi công sản phẩm", "Chủ nhà, thợ sơn và bên mua vật tư", page.title, "tools/refresh_pages.py — extract_product/render_product; nội dung hiện có là đầu vào"
    if route.startswith("/phong-thuy-son-nha/"):
        return "Phong thủy", "Gợi ý phối màu theo mệnh/tuổi và dẫn tới sản phẩm phù hợp", "Chủ nhà tìm màu sơn theo phong thủy", page.title, "tools/generate_fengshui_pages.py — ELEMENTS/AGES/pillar/element_page/age_page"
    if route == "/blog":
        return "Danh sách bài viết", "Khám phá hướng dẫn sơn nhà theo nhu cầu", "Người tìm kinh nghiệm sơn và phối màu", "Hướng dẫn sơn nhà, chống thấm và màu sơn", "tools/generate_blog_pages.py — render_blog_index"
    if route == "/ve-chung-toi":
        return "Doanh nghiệp", "Giới thiệu Sago Paint và thông tin liên hệ", "Khách xác minh thương hiệu và nhà cung cấp", "Thông tin Công ty Sơn Sago", "HTML biên tập trực tiếp"
    generated_slugs = ("son-nha-mien-tay-mua-mua-chong-tham", "mau-son-nha-cap-4-dep-2026", "son-nha-huong-tay-chong-nong", "son-nha-moi-xay", "son-nha-hop-phong-thuy")
    generator = "tools/generate_blog_pages.py và content/blog/*.md" if route.strip("/") in generated_slugs else "HTML biên tập trực tiếp"
    return "Bài hướng dẫn", "Giải đáp nhu cầu cụ thể và gợi ý hệ sơn liên quan", "Chủ nhà và người tìm hướng dẫn thi công/phối màu", page.title, generator


def main():
    rows = []
    for entry in inventory():
        page = Page((ROOT / entry["file"]).read_text(encoding="utf-8"))
        kind, purpose, audience, intent, source = describe(entry, page)
        target = context_path(entry["route"])
        target.parent.mkdir(parents=True, exist_ok=True)
        headings = "\n".join(f"- {tag.upper()}: {' '.join(text.split())}" for tag, text in page.headings)
        images = list(dict.fromkeys(img.get("src", "") for img in page.images))
        resources = "\n".join(f"- `{x}`" for x in (page.styles + images))
        ctas = [x for x in dict.fromkeys(page.links) if x.startswith(("tel:", "mailto:")) or x in ("#tu-van", "#lien-he", "/tinh-son/", "tinh-son/")]
        extra = "\n- Kiểm tra tính phòng/diện tích, preset, số 0, tab bàn phím và email chứa kết quả; không tự gửi hoặc xóa dữ liệu." if kind == "Công cụ" else ""
        text = f"""# Context — {page.title.strip()}

## Vai trò

- File: `{entry['file']}`
- URL: `https://sagopaint.vn{entry['route']}`
- Nhóm: {kind}
- Mục đích: {purpose}.
- Đối tượng: {audience}.
- CTA hiện có: {', '.join('`'+x+'`' for x in ctas) or 'Theo liên kết nội dung/sản phẩm và liên hệ ở footer'}.
- Nguồn chỉnh sửa: {source}. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: {intent}.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

{headings}

## SEO hiện tại

- Title: {page.title.strip()}
- Description: {page.meta.get('description', '')}
- Canonical: `{page.canonicals[0]}`
- Robots: `{page.meta.get('robots', 'index, follow')}`
- Schema: {', '.join(sorted(schema_types(page.schemas)))}.
- Ngôn ngữ: `{page.lang}`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

{resources}

## Tiêu chí kiểm thử

- Đọc AGENTS.md và DESIGN.md; sử dụng skill ứng với từng phase/hạng mục.
- Font Be Vietnam Pro cho chữ; không tràn ở 360/768/1440px; thử fallback CDN.
- Navigation, CTA, điểm neo hoạt động; keyboard focus rõ và không bị sticky che.
- CSS chung dùng đường dẫn tương đối theo độ sâu HTML; skip link ẩn mặc định, hiện khi Tab và Enter đưa focus tới nội dung chính. Kiểm tra cả HTTP và mở file trực tiếp.
- Title/description/canonical/schema hợp lệ; không làm hỏng liên kết hoặc tài nguyên.
- Chạy kiểm tra trang, SEO và browser test; dùng Ponytail review diff trước hoàn tất.{extra}

Context được tạo từ HTML bằng `python tools/update_contexts.py`; đọc diff và cập nhật
đúng nguồn nội dung trước khi chạy lại. Giải thích hành vi riêng cần giữ ở nguồn và test.
"""
        target.write_text(text, encoding="utf-8", newline="\n")
        rows.append(f"| `{entry['file']}` | `{entry['route']}` | [{kind}]({target.relative_to(ROOT / 'docs/pages').as_posix()}) |")
    readme = "# Bảng context từng trang\n\n54 trang nội dung hiện tại; mỗi trang có CONTEXT.md riêng.\n\n| HTML | Route công khai | Context |\n|---|---|---|\n" + "\n".join(rows)
    readme += "\n\nFile xác minh `google4bd4155c856d151b.html` giữ nguyên byte, không có giao diện, không thuộc sitemap/context trang nội dung.\n\n`404.html` là trang lỗi công khai cho URL không tồn tại, trả HTTP 404 trên\nCloudflare Pages và local server, có `noindex, follow`. File được đóng gói vào\ndist nhưng không tính là trang nội dung, không có canonical và không vào sitemap.\n\nCập nhật bảng bằng `python tools/update_contexts.py`; rà soát diff, không dùng context thay nội dung gốc.\n"
    (ROOT / "docs/pages/README.md").write_text(readme, encoding="utf-8", newline="\n")
    print(f"Updated {len(rows)} page contexts")


if __name__ == "__main__":
    main()
