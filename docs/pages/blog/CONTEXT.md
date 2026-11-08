# Context — Bài viết sơn nhà, chống thấm và màu sơn 2026 | Sago Paint

## Vai trò

- File: `blog.html`
- URL: `https://sagopaint.vn/blog`
- Nhóm: Danh sách bài viết
- Mục đích: Khám phá hướng dẫn sơn nhà theo nhu cầu.
- Đối tượng: Người tìm kinh nghiệm sơn và phối màu.
- CTA hiện có: `tel:+842866815050`, `mailto:info.sagopaint@gmail.com`.
- Nguồn chỉnh sửa: tools/generate_blog_pages.py — render_blog_index. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: Hướng dẫn sơn nhà, chống thấm và màu sơn.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Bài viết chuyên sâu về màu sơn, chống thấm và kỹ thuật thi công
- H2: Bài viết tư vấn sơn nhà
- H3: Xu hướng màu sơn nhà 2026
- H3: Sơn Nhà Miền Tây Mùa Mưa
- H3: Top 10 Màu Sơn Nhà Cấp 4 Đẹp 2026
- H3: Nhà Hướng Tây Sơn Màu Gì?
- H3: Nhà Mới Xây Bao Lâu Thì Sơn Được?
- H3: Màu Sơn Nhà Hợp Phong Thủy 2026
- H3: Chống thấm tường ngoài trời
- H3: Chống thấm sân thượng, ban công
- H2: Cụm nội dung tư vấn sơn nhà miền Tây
- H2: Hướng dẫn hữu ích trước khi chọn sơn
- H2: Công ty Sơn Sago
- H3: Thông tin liên hệ
- H3: Danh mục

## SEO hiện tại

- Title: Bài viết sơn nhà, chống thấm và màu sơn 2026 | Sago Paint
- Description: Tổng hợp bài viết chuyên sâu về màu sơn nhà, chống thấm, chống nóng, phong thủy và kỹ thuật sơn cho nhà miền Tây.
- Canonical: `https://sagopaint.vn/blog`
- Robots: `index, follow`
- Schema: .
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `category-pages.css`
- `assets/css/site-base.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`
- `https://images.unsplash.com/photo-1600210491369-e753d80a41f3?auto=format&fit=crop&w=1400&q=84`
- `https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?auto=format&fit=crop&w=1400&q=84`
- `https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1400&q=84`
- `https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=1400&q=84`
- `https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=1400&q=84`
- `https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1400&q=84`

## Tiêu chí kiểm thử

- Đọc AGENTS.md và DESIGN.md; sử dụng skill ứng với từng phase/hạng mục.
- Font Be Vietnam Pro cho chữ; không tràn ở 360/768/1440px; thử fallback CDN.
- Navigation, CTA, điểm neo hoạt động; keyboard focus rõ và không bị sticky che.
- CSS chung dùng đường dẫn tương đối theo độ sâu HTML; skip link ẩn mặc định, hiện khi Tab và Enter đưa focus tới nội dung chính. Kiểm tra cả HTTP và mở file trực tiếp.
- Title/description/canonical/schema hợp lệ; không làm hỏng liên kết hoặc tài nguyên.
- Chạy kiểm tra trang, SEO và browser test; dùng Ponytail review diff trước hoàn tất.

Context được tạo từ HTML bằng `python tools/update_contexts.py`; đọc diff và cập nhật
đúng nguồn nội dung trước khi chạy lại. Giải thích hành vi riêng cần giữ ở nguồn và test.
