# Context — Sơn chống thấm sân thượng mùa mưa: chọn sao cho bền | Sago Paint

## Vai trò

- File: `son-chong-tham-san-thuong-mua-mua.html`
- URL: `https://sagopaint.vn/son-chong-tham-san-thuong-mua-mua`
- Nhóm: Bài hướng dẫn
- Mục đích: Giải đáp nhu cầu cụ thể và gợi ý hệ sơn liên quan.
- Đối tượng: Chủ nhà và người tìm hướng dẫn thi công/phối màu.
- CTA hiện có: `tel:+842866815050`, `mailto:info.sagopaint@gmail.com`.
- Nguồn chỉnh sửa: HTML biên tập trực tiếp. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: Sơn chống thấm sân thượng mùa mưa: chọn sao cho bền | Sago Paint.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Sơn chống thấm sân thượng mùa mưa: chọn sao cho bền?
- H2: Kiểm tra bề mặt trước khi thi công
- H2: Chọn hệ chống thấm Acrylic - PU cho khu vực lộ thiên
- H2: Không bỏ qua lớp gia cường tại điểm yếu
- H2: Thời điểm thi công
- H2: Trước khi báo giá chống thấm
- H2: Công ty Sơn Sago
- H3: Liên hệ

## SEO hiện tại

- Title: Sơn chống thấm sân thượng mùa mưa: chọn sao cho bền | Sago Paint
- Description: Hướng dẫn chọn sơn chống thấm sân thượng mùa mưa: nhận biết bề mặt, xử lý nứt, chọn hệ Acrylic-PU và lưu ý thi công.
- Canonical: `https://sagopaint.vn/son-chong-tham-san-thuong-mua-mua`
- Robots: `index, follow`
- Schema: Article.
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `category-pages.css`
- `assets/css/site-base.css`
- `assets/css/editorial.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`
- `assets/products/sago-s68-pro-preview.webp`

## Giao diện

- Giao diện tối giản: nền trắng/xám nhạt, tiêu đề trái, ảnh minh họa rộng; không gradient hoặc thẻ trang trí nổi.
- Nội dung bài đọc tối đa 70ch; sidebar tư vấn nhẹ, chuyển xuống dưới ở màn hình nhỏ. Danh sách bài dùng ảnh lớn và metadata dạng chữ.
- Menu thu gọn dưới 1200px; CSS editorial riêng không tác động danh mục/sản phẩm.

## Tiêu chí kiểm thử

- Đọc AGENTS.md và DESIGN.md; sử dụng skill ứng với từng phase/hạng mục.
- Font Be Vietnam Pro cho chữ; không tràn ở 360/768/1440px; thử fallback CDN.
- Navigation, CTA, điểm neo hoạt động; keyboard focus rõ và không bị sticky che.
- CSS chung dùng đường dẫn tương đối theo độ sâu HTML; skip link ẩn mặc định, hiện khi Tab và Enter đưa focus tới nội dung chính. Kiểm tra cả HTTP và mở file trực tiếp.
- Title/description/canonical/schema hợp lệ; không làm hỏng liên kết hoặc tài nguyên.
- Chạy kiểm tra trang, SEO và browser test; dùng Ponytail review diff trước hoàn tất.

Context được tạo từ HTML bằng `python tools/update_contexts.py`; đọc diff và cập nhật
đúng nguồn nội dung trước khi chạy lại. Giải thích hành vi riêng cần giữ ở nguồn và test.
