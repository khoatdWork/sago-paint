# Context — Cách tính lượng sơn cần dùng cho nhà mới và nhà sửa | Sago Paint

## Vai trò

- File: `cach-tinh-luong-son-can-dung.html`
- URL: `https://sagopaint.vn/cach-tinh-luong-son-can-dung`
- Nhóm: Bài hướng dẫn
- Mục đích: Giải đáp nhu cầu cụ thể và gợi ý hệ sơn liên quan.
- Đối tượng: Chủ nhà và người tìm hướng dẫn thi công/phối màu.
- CTA hiện có: `tel:+842866815050`.
- Nguồn chỉnh sửa: HTML biên tập trực tiếp. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: Cách tính lượng sơn cần dùng cho nhà mới và nhà sửa | Sago Paint.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Cách tính lượng sơn cần dùng để không mua thiếu hoặc dư quá nhiều
- H2: Công thức cơ bản
- H2: Cách tính diện tích tường
- H2: Đừng quên sơn lót
- H2: Hao hụt thực tế
- H2: Khi nào nên hỏi tư vấn?

## SEO hiện tại

- Title: Cách tính lượng sơn cần dùng cho nhà mới và nhà sửa | Sago Paint
- Description: Công thức tính lượng sơn cần dùng theo diện tích tường, số lớp, định mức phủ và cách tránh mua thiếu hoặc dư quá nhiều.
- Canonical: `https://sagopaint.vn/cach-tinh-luong-son-can-dung`
- Robots: `index, follow`
- Schema: Article.
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `category-pages.css`
- `assets/css/site-base.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`

## Tiêu chí kiểm thử

- Đọc AGENTS.md và DESIGN.md; sử dụng skill ứng với từng phase/hạng mục.
- Font Be Vietnam Pro cho chữ; không tràn ở 360/768/1440px; thử fallback CDN.
- Navigation, CTA, điểm neo hoạt động; keyboard focus rõ và không bị sticky che.
- CSS chung dùng đường dẫn tương đối theo độ sâu HTML; skip link ẩn mặc định, hiện khi Tab và Enter đưa focus tới nội dung chính. Kiểm tra cả HTTP và mở file trực tiếp.
- Title/description/canonical/schema hợp lệ; không làm hỏng liên kết hoặc tài nguyên.
- Chạy kiểm tra trang, SEO và browser test; dùng Ponytail review diff trước hoàn tất.

Context được tạo từ HTML bằng `python tools/update_contexts.py`; đọc diff và cập nhật
đúng nguồn nội dung trước khi chạy lại. Giải thích hành vi riêng cần giữ ở nguồn và test.
