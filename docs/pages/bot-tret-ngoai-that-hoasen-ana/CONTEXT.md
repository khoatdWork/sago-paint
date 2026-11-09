# Context — BỘT TRÉT NGOẠI THẤT HOASEN ANA | Sơn ngoại thất Sago Paint

## Vai trò

- File: `bot-tret-ngoai-that-hoasen-ana.html`
- URL: `https://sagopaint.vn/bot-tret-ngoai-that-hoasen-ana`
- Nhóm: Sản phẩm
- Mục đích: Hiểu ứng dụng, đặc tính và cách thi công sản phẩm.
- Đối tượng: Chủ nhà, thợ sơn và bên mua vật tư.
- CTA hiện có: `tel:+842866815050`, `#lien-he`, `mailto:info.sagopaint@gmail.com`.
- Nguồn chỉnh sửa: tools/refresh_pages.py — extract_product/render_product; nội dung hiện có là đầu vào. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: BỘT TRÉT NGOẠI THẤT HOASEN ANA | Sơn ngoại thất Sago Paint.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Bột trét ngoại thất HOASEN ANA
- H2: Lợi ích khi sử dụng sản phẩm
- H2: Ứng dụng phù hợp
- H2: Điểm nổi bật
- H2: Thông tin kỹ thuật
- H2: Thông tin sản phẩm
- H2: Hướng dẫn sử dụng
- H2: Cần chọn đúng sản phẩm cho bề mặt thực tế?
- H2: Câu hỏi thường gặp
- H3: BỘT TRÉT NGOẠI THẤT HOASEN ANA phù hợp với bề mặt nào?
- H3: Sản phẩm này dùng cho nội thất hay ngoại thất?
- H3: Độ phủ của sản phẩm khoảng bao nhiêu?
- H3: Thời gian khô là bao lâu?
- H3: Có cần sơn lót trước khi sử dụng không?
- H3: Làm sao để nhận báo giá chính xác?
- H2: Sản phẩm liên quan
- H3: Sơn ngoại thất ANA Satin bề mặt bán bóng
- H3: Sơn ngoại thất ANA Satin bề mặt siêu bóng
- H3: Sơn ngoại thất Anashield bề mặt bóng mờ
- H2: Công ty Sơn Sago
- H3: Thông tin liên hệ
- H3: Danh mục

## SEO hiện tại

- Title: BỘT TRÉT NGOẠI THẤT HOASEN ANA | Sơn ngoại thất Sago Paint
- Description: Bột trét tường ngoại thất HOASEN ANA dùng để làm phẳng bề mặt hồ xây và bê tông. Sản phẩm có độ phủ tốt, dễ thi công, tạo bề mặt láng mịn cho sơn nước ngoại thất.
- Canonical: `https://sagopaint.vn/bot-tret-ngoai-that-hoasen-ana`
- Robots: `index, follow`
- Schema: BreadcrumbList, FAQPage, HomeAndConstructionBusiness, Product.
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

## Tiêu chí kiểm thử

- Bố cục: nền trắng/xám nhẹ; sản phẩm dùng ảnh trái và thông tin phải trên desktop, tên–ảnh–mô tả trên mobile. Danh mục ưu tiên danh sách sản phẩm trước hướng dẫn lựa chọn.

- Đọc AGENTS.md và DESIGN.md; sử dụng skill ứng với từng phase/hạng mục.
- Font Be Vietnam Pro cho chữ; không tràn ở 360/768/1440px; thử fallback CDN.
- Navigation, CTA, điểm neo hoạt động; keyboard focus rõ và không bị sticky che.
- CSS chung dùng đường dẫn tương đối theo độ sâu HTML; skip link ẩn mặc định, hiện khi Tab và Enter đưa focus tới nội dung chính. Kiểm tra cả HTTP và mở file trực tiếp.
- Title/description/canonical/schema hợp lệ; không làm hỏng liên kết hoặc tài nguyên.
- FAQ thời gian khô và FAQPage phải cùng dùng "Thời gian khô: 16 giờ" từ hướng dẫn sử dụng; không lấy khối lượng thể tích của bột khô làm thời gian.
- Chạy kiểm tra trang, SEO và browser test; dùng Ponytail review diff trước hoàn tất.

Context được tạo từ HTML bằng `python tools/update_contexts.py`; đọc diff và cập nhật
đúng nguồn nội dung trước khi chạy lại. Giải thích hành vi riêng cần giữ ở nguồn và test.
