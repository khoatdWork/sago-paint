# Context — Sơn ngoại thất Sago Paint | Danh mục sản phẩm chính hãng

## Vai trò

- File: `son-ngoai-that.html`
- URL: `https://sagopaint.vn/son-ngoai-that`
- Nhóm: Danh mục
- Mục đích: Chọn và so sánh sản phẩm trong hệ sơn.
- Đối tượng: Người đang lựa chọn hệ sơn.
- CTA hiện có: `tel:+842866815050`, `#lien-he`, `mailto:info.sagopaint@gmail.com`.
- Nguồn chỉnh sửa: tools/refresh_pages.py — CATEGORY_META/render_category. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: Sơn ngoại thất Sago Paint | Danh mục sản phẩm chính hãng.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Bảo vệ mặt tiền trước nắng mưa, rêu mốc và phai màu
- H2: Sản phẩm sơn ngoại thất nổi bật
- H2: Bột trét ngoại thất HOASEN ANA
- H2: Sơn ngoại thất ANA Satin bề mặt bán bóng
- H2: Sơn ngoại thất ANA Satin bề mặt siêu bóng
- H2: Sơn ngoại thất Anashield bề mặt bóng mờ
- H2: Sơn ngoại thất chống rêu mốc Super Satin
- H2: Chọn hệ sơn phù hợp
- H3: Ứng dụng phù hợp
- H3: Lợi ích chính
- H2: Chưa chắc nên dùng sản phẩm nào?
- H2: Công ty Sơn Sago
- H3: Thông tin liên hệ
- H3: Danh mục

## SEO hiện tại

- Title: Sơn ngoại thất Sago Paint | Danh mục sản phẩm chính hãng
- Description: Danh mục sơn ngoại thất Sago Paint giúp xử lý bề mặt, chống kiềm, chống rêu mốc, hạn chế phai màu và bảo vệ công trình trước điều kiện thời tiết.
- Canonical: `https://sagopaint.vn/son-ngoai-that`
- Robots: `index, follow`
- Schema: BreadcrumbList, CollectionPage, HomeAndConstructionBusiness.
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `category-pages.css`
- `assets/css/site-base.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`
- `https://cdn.sagopaint.vn/assets/products/bot-tret-ngoai-that-hoasen-ana.png`
- `https://cdn.sagopaint.vn/assets/products/son-ngoai-that-ana-satin-be-mat-ban-bong.png`
- `https://cdn.sagopaint.vn/assets/products/son-ngoai-that-ana-satin-be-mat-sieu-bong.png`
- `https://cdn.sagopaint.vn/assets/products/son-sagopaint-ngoai-that-chong-phai-mau-anashield-be-mat-bong-mo.png`
- `https://cdn.sagopaint.vn/assets/products/son-sagopaint-ngoai-that-chong-reu-moc-super-satin-1.png`

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
