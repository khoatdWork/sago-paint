# Context — Nhà Hướng Tây Sơn Màu Gì? Bí Quyết Giảm Nóng Cho Miền Tây | Sago Paint

## Vai trò

- File: `son-nha-huong-tay-chong-nong.html`
- URL: `https://sagopaint.vn/son-nha-huong-tay-chong-nong`
- Nhóm: Bài hướng dẫn
- Mục đích: Giải đáp nhu cầu cụ thể và gợi ý hệ sơn liên quan.
- Đối tượng: Chủ nhà và người tìm hướng dẫn thi công/phối màu.
- CTA hiện có: `tel:+842866815050`, `mailto:info.sagopaint@gmail.com`.
- Nguồn chỉnh sửa: tools/generate_blog_pages.py và content/blog/*.md. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: Nhà Hướng Tây Sơn Màu Gì? Bí Quyết Giảm Nóng Cho Miền Tây | Sago Paint.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Nhà Hướng Tây Sơn Màu Gì? Bí Quyết Giảm Nóng Hiệu Quả Cho Khí Hậu Miền Tây
- H2: Giới thiệu
- H2: Nguyên tắc chọn màu cho nhà hướng Tây
- H3: Ưu tiên màu sáng, dịu và ít hấp thụ nhiệt
- H3: Tránh phủ màu đậm trên mảng tường lớn
- H2: 6 nhóm màu sơn phù hợp nhất cho nhà hướng Tây
- H3: Trắng kem và trắng xám
- H3: Be sáng và vàng kem nhạt
- H3: Ghi nhạt và ghi ấm
- H3: Xanh sage và xanh dương nhạt
- H3: Hồng đất nhạt
- H3: Màu nhấn cho cột, chỉ, chân tường
- H2: Sơn chống nóng có đủ không?
- H2: Giải pháp kết hợp để giảm nóng rõ hơn
- H3: Lam che, mái hiên và cây xanh
- H3: Hạn chế kính lớn ở mặt tiền
- H3: Sơn nội thất màu sáng và thông gió
- H2: Gợi ý phối màu theo từng kiểu nhà
- H2: Nhận tư vấn màu sơn miễn phí
- H2: Câu hỏi thường gặp
- H2: Kết luận
- H2: Cần chọn hệ sơn phù hợp?
- H2: Công ty Sơn Sago
- H3: Thông tin liên hệ
- H3: Danh mục

## SEO hiện tại

- Title: Nhà Hướng Tây Sơn Màu Gì? Bí Quyết Giảm Nóng Cho Miền Tây | Sago Paint
- Description: Nhà hướng Tây ở miền Tây nên sơn màu gì để giảm nóng? Gợi ý màu ngoại thất, nội thất, vật liệu che nắng và hệ sơn bền cho mùa mưa.
- Canonical: `https://sagopaint.vn/son-nha-huong-tay-chong-nong`
- Robots: `index, follow`
- Schema: Article, BreadcrumbList, FAQPage.
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `category-pages.css`
- `assets/css/site-base.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`
- `https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=1400&q=84`
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
