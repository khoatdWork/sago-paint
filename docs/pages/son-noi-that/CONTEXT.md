# Context — Sơn nội thất Sago Paint | Danh mục sản phẩm chính hãng

## Vai trò

- File: `son-noi-that.html`
- URL: `https://sagopaint.vn/son-noi-that`
- Nhóm: Danh mục
- Mục đích: Chọn và so sánh sản phẩm trong hệ sơn.
- Đối tượng: Người đang lựa chọn hệ sơn.
- CTA hiện có: `tel:+842866815050`, `#lien-he`, `mailto:info.sagopaint@gmail.com`.
- Nguồn chỉnh sửa: tools/refresh_pages.py — CATEGORY_META/render_category. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: Sơn nội thất Sago Paint | Danh mục sản phẩm chính hãng.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Sơn nội thất bền màu, ít mùi, dễ lau chùi cho không gian sống hiện đại
- H2: Sản phẩm sơn nội thất nổi bật
- H3: Ứng dụng phù hợp
- H3: Lợi ích chính
- H2: BỘT TRÉT NỘI THẤT HOASEN ANA
- H2: SƠN NỘI THẤT LAU CHÙI HIỆU QUẢ ANAclean bề mặt bán bóng
- H2: SƠN NỘI THẤT LAU CHÙI HIỆU QUẢ ANAclean bề mặt bán bóng
- H2: Sơn Sagopaint lót nội & ngoại thất Ana Sealer
- H2: Sơn Sagopaint lót nội & ngoại thất Sealer Primer
- H2: Sơn Sagopaint nội thất Che Phủ Tối Đa ANA MATEX
- H2: Sơn Sagopaint nội thất Lau Chùi Hiệu Quả Anaclean - bề mặt bóng mờ
- H2: Sơn Sagopaint nội thất MÀNG SƠN MỊN ĐẸP V - 2000
- H2: Chưa chắc nên dùng sản phẩm nào?
- H2: Công ty Sơn Sago
- H3: Thông tin liên hệ
- H3: Danh mục

## SEO hiện tại

- Title: Sơn nội thất Sago Paint | Danh mục sản phẩm chính hãng
- Description: Danh mục sơn nội thất Sago Paint gồm sơn phủ, sơn lót và bột trét giúp hoàn thiện bề mặt tường trong nhà mịn đẹp, dễ lau chùi, ít mùi và bền màu.
- Canonical: `https://sagopaint.vn/son-noi-that`
- Robots: `index, follow`
- Schema: BreadcrumbList, CollectionPage, HomeAndConstructionBusiness.
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `category-pages.css`
- `assets/css/site-base.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`
- `https://cdn.sagopaint.vn/assets/products/bot-tret-noi-that-hoasen-ana.png`
- `https://cdn.sagopaint.vn/assets/products/son-noi-that-lau-chui-hieu-qua-anaclean-be-mat-ban-bong-2.png`
- `https://cdn.sagopaint.vn/assets/products/son-noi-that-lau-chui-hieu-qua-anaclean-be-mat-ban-bong.png`
- `https://cdn.sagopaint.vn/assets/products/son-sagopain-lot-noi-ngoai-that-ana-sealer.png`
- `https://cdn.sagopaint.vn/assets/products/son-sagopain-lot-noi-ngoai-that-sealer-primer.png`
- `https://cdn.sagopaint.vn/assets/products/son-sagopaint-noi-that-che-phu-toi-a-ana-matex.png`
- `https://cdn.sagopaint.vn/assets/products/son-sagopaint-noi-that-lau-chui-hieu-qua-anaclean-be-mat-bong-mo.png`
- `https://cdn.sagopaint.vn/assets/products/son-sagopaint-not-that-mang-son-min-ep-v-2000.png`

## Tiêu chí kiểm thử

- Đọc AGENTS.md và DESIGN.md; sử dụng skill ứng với từng phase/hạng mục.
- Font Be Vietnam Pro cho chữ; không tràn ở 360/768/1440px; thử fallback CDN.
- Navigation, CTA, điểm neo hoạt động; keyboard focus rõ và không bị sticky che.
- CSS chung dùng đường dẫn tương đối theo độ sâu HTML; skip link ẩn mặc định, hiện khi Tab và Enter đưa focus tới nội dung chính. Kiểm tra cả HTTP và mở file trực tiếp.
- Title/description/canonical/schema hợp lệ; không làm hỏng liên kết hoặc tài nguyên.
- Chạy kiểm tra trang, SEO và browser test; dùng Ponytail review diff trước hoàn tất.

Context được tạo từ HTML bằng `python tools/update_contexts.py`; đọc diff và cập nhật
đúng nguồn nội dung trước khi chạy lại. Giải thích hành vi riêng cần giữ ở nguồn và test.
