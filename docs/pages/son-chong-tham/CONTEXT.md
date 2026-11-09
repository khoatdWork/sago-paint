# Context — Sơn chống thấm Sago Paint | Danh mục sản phẩm chính hãng

## Vai trò

- File: `son-chong-tham.html`
- URL: `https://sagopaint.vn/son-chong-tham`
- Nhóm: Danh mục
- Mục đích: Chọn và so sánh sản phẩm trong hệ sơn.
- Đối tượng: Người đang lựa chọn hệ sơn.
- CTA hiện có: `tel:+842866815050`, `#lien-he`, `mailto:info.sagopaint@gmail.com`.
- Nguồn chỉnh sửa: tools/refresh_pages.py — CATEGORY_META/render_category. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: Sơn chống thấm Sago Paint | Danh mục sản phẩm chính hãng.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Giải pháp chống thấm cho tường, mái, sân thượng và ban công
- H2: Sản phẩm chống thấm nổi bật
- H2: Chất chống thấm BT-11A pha xi măng
- H2: Chống thấm lộ thiên PU-502
- H2: SAGO S 68 PRO chống thấm đa năng lộ thiên cao cấp
- H2: Sơn chống thấm màu Aqua Shield 5 in 1
- H2: Sơn chống thấm màu Aqua Shield 5 in 1
- H2: Chọn hệ sơn phù hợp
- H3: Ứng dụng phù hợp
- H3: Lợi ích chính
- H2: Chưa chắc nên dùng sản phẩm nào?
- H2: Công ty Sơn Sago
- H3: Thông tin liên hệ
- H3: Danh mục

## SEO hiện tại

- Title: Sơn chống thấm Sago Paint | Danh mục sản phẩm chính hãng
- Description: Danh mục chống thấm Sago Paint cho tường, sân thượng, mái, ban công, tầng hầm và các khu vực cần bảo vệ trước nước, ẩm mốc.
- Canonical: `https://sagopaint.vn/son-chong-tham`
- Robots: `index, follow`
- Schema: BreadcrumbList, CollectionPage, HomeAndConstructionBusiness.
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `category-pages.css`
- `assets/css/site-base.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`
- `https://cdn.sagopaint.vn/assets/products/chat-chong-tham-bt-11a-pha-xi-mang.png`
- `https://cdn.sagopaint.vn/assets/products/chong-tham-lo-thien-pu-502.png`
- `assets/products/sago-s68-pro-preview.webp`
- `https://cdn.sagopaint.vn/assets/products/son-chong-tham-mau-aqua-shield-5-in1.png`
- `https://cdn.sagopaint.vn/assets/products/son-sagopaint-chong-tham-mau-aqua-shield-5in1.png`

## Tiêu chí kiểm thử

- Bố cục: nền trắng/xám nhẹ; sản phẩm dùng ảnh trái và thông tin phải trên desktop, tên–ảnh–mô tả trên mobile. Danh mục ưu tiên danh sách sản phẩm trước hướng dẫn lựa chọn.

- Đọc AGENTS.md và DESIGN.md; sử dụng skill ứng với từng phase/hạng mục.
- Font Be Vietnam Pro cho chữ; không tràn ở 360/768/1440px; thử fallback CDN.
- Navigation, CTA, điểm neo hoạt động; keyboard focus rõ và không bị sticky che.
- CSS chung dùng đường dẫn tương đối theo độ sâu HTML; skip link ẩn mặc định, hiện khi Tab và Enter đưa focus tới nội dung chính. Kiểm tra cả HTTP và mở file trực tiếp.
- Title/description/canonical/schema hợp lệ; không làm hỏng liên kết hoặc tài nguyên.
- Chạy kiểm tra trang, SEO và browser test; dùng Ponytail review diff trước hoàn tất.

Context được tạo từ HTML bằng `python tools/update_contexts.py`; đọc diff và cập nhật
đúng nguồn nội dung trước khi chạy lại. Giải thích hành vi riêng cần giữ ở nguồn và test.
