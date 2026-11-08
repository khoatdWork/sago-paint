# Context — Sago Paint - Sơn nội thất, ngoại thất, chống thấm

## Vai trò

- File: `index.html`
- URL: `https://sagopaint.vn/`
- Nhóm: Trang chủ
- Mục đích: Giới thiệu thương hiệu và dẫn khách tới đúng hệ sơn.
- Đối tượng: Chủ nhà, thợ sơn và khách công trình.
- CTA hiện có: `tel:+842866815050`, `mailto:info.sagopaint@gmail.com`, `#lien-he`.
- Nguồn chỉnh sửa: HTML biên tập trực tiếp. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: So sánh giải pháp sơn Sago Paint và tìm nơi tư vấn.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: SAGO S 68 PRO chống thấm mái, sàn, ban công.
- H2: Chọn đúng sơn cho từng khu vực công trình.
- H3: Sơn nội thất
- H3: Sơn ngoại thất
- H3: Sơn chống thấm
- H2: Tính lượng sơn cần dùng
- H2: Chọn màu sơn hợp phong thủy
- H2: Cẩm nang sơn nhà cho khí hậu miền Tây
- H3: Xu hướng màu sơn nhà 2026
- H3: Sơn Nhà Miền Tây Mùa Mưa
- H3: Top 10 Màu Sơn Nhà Cấp 4 Đẹp 2026
- H3: Nhà Hướng Tây Sơn Màu Gì?
- H3: Nhà Mới Xây Bao Lâu Thì Sơn Được?
- H3: Màu Sơn Nhà Hợp Phong Thủy 2026
- H2: Công ty Sơn Sago
- H3: Thông tin liên hệ
- H3: Liên kết nhanh

## SEO hiện tại

- Title: Sago Paint - Sơn nội thất, ngoại thất, chống thấm
- Description: Sago Paint cung cấp sơn nội thất, sơn ngoại thất, sơn chống thấm và giải pháp sơn nhà chuyên nghiệp cho công trình dân dụng, thương mại.
- Canonical: `https://sagopaint.vn/`
- Robots: `index, follow`
- Schema: HomeAndConstructionBusiness.
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `assets/css/site-base.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`
- `assets/products/sago-s68-pro-home.webp`
- `https://cdn.sagopaint.vn/assets/categories/son-noi-that-phong-khach-hien-dai.webp`
- `https://cdn.sagopaint.vn/assets/categories/son-ngoai-that-mat-tien-nha-hien-dai.webp`
- `https://cdn.sagopaint.vn/assets/categories/son-chong-tham-mai-nha-mua.webp`
- `https://images.unsplash.com/photo-1600210491369-e753d80a41f3?auto=format&fit=crop&w=1400&q=84`
- `https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?auto=format&fit=crop&w=1400&q=84`
- `https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1400&q=84`

## Hành vi giao diện

- Menu điều hướng thu gọn dưới 1200px để tránh xuống hàng ở laptop nhỏ.
- Hero SAGO S 68 PRO tĩnh; ảnh luôn hiện ở mobile/tablet/desktop, không có carousel.
- Ảnh hero cắt khoảng trong suốt từ ảnh gốc, không thay nhãn; dùng đường dẫn tương đối cho HTTP và file trực tiếp.
- Ba danh mục đặt cạnh nhau trên desktop/tablet, xếp dọc trên mobile. Công cụ tính sơn và phong thủy là hai mục ngắn.
- Cẩm nang có ba bài kèm ảnh và ba liên kết phụ; giữ đường dẫn tới cả sáu bài viết.

## Tiêu chí kiểm thử

- Đọc AGENTS.md và DESIGN.md; sử dụng skill ứng với từng phase/hạng mục.
- Font Be Vietnam Pro cho chữ; không tràn ở 360/768/1440px; thử fallback CDN.
- Ảnh S68 decode, hiển thị tối thiểu 160×140px, nằm trọn trong hero ở 360/768/1440px qua HTTP và file trực tiếp.
- Navigation, CTA, điểm neo hoạt động; keyboard focus rõ và không bị sticky che.
- CSS chung dùng đường dẫn tương đối theo độ sâu HTML; skip link ẩn mặc định, hiện khi Tab và Enter đưa focus tới nội dung chính. Kiểm tra cả HTTP và mở file trực tiếp.
- Title/description/canonical/schema hợp lệ; không làm hỏng liên kết hoặc tài nguyên.
- Chạy kiểm tra trang, SEO và browser test; dùng Ponytail review diff trước hoàn tất.

Context được tạo từ HTML bằng `python tools/update_contexts.py`; đọc diff và cập nhật
đúng nguồn nội dung trước khi chạy lại. Giải thích hành vi riêng cần giữ ở nguồn và test.
