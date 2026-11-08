# Context — Sơn Nhà Miền Tây Mùa Mưa: 7 Giải Pháp Chống Thấm Hiệu Quả | Sago Paint

## Vai trò

- File: `son-nha-mien-tay-mua-mua-chong-tham.html`
- URL: `https://sagopaint.vn/son-nha-mien-tay-mua-mua-chong-tham`
- Nhóm: Bài hướng dẫn
- Mục đích: Giải đáp nhu cầu cụ thể và gợi ý hệ sơn liên quan.
- Đối tượng: Chủ nhà và người tìm hướng dẫn thi công/phối màu.
- CTA hiện có: `tel:+842866815050`, `mailto:info.sagopaint@gmail.com`.
- Nguồn chỉnh sửa: tools/generate_blog_pages.py và content/blog/*.md. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: Sơn Nhà Miền Tây Mùa Mưa: 7 Giải Pháp Chống Thấm Hiệu Quả | Sago Paint.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Sơn Nhà Miền Tây Mùa Mưa: 7 Giải Pháp Chống Thấm Hiệu Quả Cho Tường Ngoài Trời
- H2: Giới thiệu
- H2: Vì sao nhà miền Tây dễ thấm vào mùa mưa?
- H3: Mưa kéo dài, gió tạt và độ ẩm cao
- H3: Nhà gần sông rạch và chân tường thường xuyên ẩm
- H2: 7 giải pháp chống thấm hiệu quả cho tường ngoài trời
- H3: 1. Kiểm tra đúng nguồn thấm trước khi sơn
- H3: 2. Xử lý rêu mốc và lớp sơn cũ triệt để
- H3: 3. Trám vết nứt chân chim và khe tiếp giáp
- H3: 4. Dùng sơn lót chống kiềm trước lớp phủ
- H3: 5. Thi công đủ lớp sơn chống thấm ở mảng hứng mưa
- H3: 6. Chọn thời điểm thi công khô ráo, tránh mưa trong 24-48 giờ
- H3: 7. Bảo trì định kỳ sau mỗi mùa mưa
- H2: Quy trình sơn nhà mùa mưa cho gia chủ miền Tây
- H2: Gợi ý hệ sơn theo từng khu vực nhà
- H2: Lỗi thường gặp khi chống thấm mùa mưa
- H2: Nhận tư vấn màu sơn miễn phí
- H2: Câu hỏi thường gặp
- H2: Kết luận
- H2: Cần chọn hệ sơn phù hợp?
- H2: Công ty Sơn Sago
- H3: Thông tin liên hệ
- H3: Danh mục

## SEO hiện tại

- Title: Sơn Nhà Miền Tây Mùa Mưa: 7 Giải Pháp Chống Thấm Hiệu Quả | Sago Paint
- Description: Kinh nghiệm sơn nhà miền Tây mùa mưa: xử lý thấm, rêu mốc, nứt chân chim và chọn hệ sơn chống thấm bền cho tường ngoài trời.
- Canonical: `https://sagopaint.vn/son-nha-mien-tay-mua-mua-chong-tham`
- Robots: `index, follow`
- Schema: Article, BreadcrumbList, FAQPage.
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `category-pages.css`
- `assets/css/site-base.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`
- `https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?auto=format&fit=crop&w=1400&q=84`
- `https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=82`
- `https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&w=1200&q=82`
- `https://images.unsplash.com/photo-1562259949-e8e7689d7828?auto=format&fit=crop&w=1200&q=82`
- `https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=82`
- `https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?auto=format&fit=crop&w=1200&q=82`

## Tiêu chí kiểm thử

- Đọc AGENTS.md và DESIGN.md; sử dụng skill ứng với từng phase/hạng mục.
- Font Be Vietnam Pro cho chữ; không tràn ở 360/768/1440px; thử fallback CDN.
- Navigation, CTA, điểm neo hoạt động; keyboard focus rõ và không bị sticky che.
- CSS chung dùng đường dẫn tương đối theo độ sâu HTML; skip link ẩn mặc định, hiện khi Tab và Enter đưa focus tới nội dung chính. Kiểm tra cả HTTP và mở file trực tiếp.
- Title/description/canonical/schema hợp lệ; không làm hỏng liên kết hoặc tài nguyên.
- Chạy kiểm tra trang, SEO và browser test; dùng Ponytail review diff trước hoàn tất.

Context được tạo từ HTML bằng `python tools/update_contexts.py`; đọc diff và cập nhật
đúng nguồn nội dung trước khi chạy lại. Giải thích hành vi riêng cần giữ ở nguồn và test.
