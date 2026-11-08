# Context — Màu Sơn Hợp Mệnh Kim Cho Nhà Sang Trọng, Vượng Khí

## Vai trò

- File: `phong-thuy-son-nha/menh-kim/index.html`
- URL: `https://sagopaint.vn/phong-thuy-son-nha/menh-kim/`
- Nhóm: Phong thủy
- Mục đích: Gợi ý phối màu theo mệnh/tuổi và dẫn tới sản phẩm phù hợp.
- Đối tượng: Chủ nhà tìm màu sơn theo phong thủy.
- CTA hiện có: `tel:+842866815050`, `mailto:info.sagopaint@gmail.com`.
- Nguồn chỉnh sửa: tools/generate_fengshui_pages.py — ELEMENTS/AGES/pillar/element_page/age_page. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: Màu Sơn Hợp Mệnh Kim Cho Nhà Sang Trọng, Vượng Khí.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Màu Sơn Hợp Mệnh Kim Cho Nhà Sang Trọng, Vượng Khí
- H2: Đặc điểm người mệnh Kim khi chọn màu nhà
- H2: Màu tương sinh và tương hợp
- H2: Màu cần tránh
- H2: Gợi ý phối màu nội thất
- H2: Nguyên tắc phối màu 60-30-10 cho mệnh Kim
- H2: Đánh giá ánh sáng trước khi chốt màu
- H2: Phối màu theo vật liệu nội thất
- H2: Lưu ý màu cần hạn chế
- H2: Chuẩn bị bề mặt và hệ sơn
- H2: Liên kết nhanh theo tuổi
- H2: Bài Viết Theo Tuổi Cùng Mệnh Kim
- H2: Các Mệnh Khác
- H2: Sản phẩm sơn nên dùng
- H2: Câu hỏi thường gặp
- H2: S68 Pro - giải pháp chống thấm cao cấp cho màu sơn phong thủy hiện đại
- H2: Nhận tư vấn màu sơn phong thủy cùng Sago Paint

## SEO hiện tại

- Title: Màu Sơn Hợp Mệnh Kim Cho Nhà Sang Trọng, Vượng Khí
- Description: Tư vấn màu sơn hợp mệnh Kim theo ngũ hành, phối màu hiện đại, tránh màu xung khắc và gợi ý S68 Pro cho nhà đẹp, bền màu, dễ vệ sinh.
- Canonical: `https://sagopaint.vn/phong-thuy-son-nha/menh-kim/`
- Robots: `index, follow`
- Schema: Article, BreadcrumbList, FAQPage, HomeAndConstructionBusiness.
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `../../phong-thuy-son-nha/styles.css`
- `../../assets/css/site-base.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`
- `https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=1400&q=82`
- `/assets/products/sago-s68-pro-preview.webp`

## Tiêu chí kiểm thử

- Đọc AGENTS.md và DESIGN.md; sử dụng skill ứng với từng phase/hạng mục.
- Font Be Vietnam Pro cho chữ; không tràn ở 360/768/1440px; thử fallback CDN.
- Navigation, CTA, điểm neo hoạt động; keyboard focus rõ và không bị sticky che.
- CSS chung dùng đường dẫn tương đối theo độ sâu HTML; skip link ẩn mặc định, hiện khi Tab và Enter đưa focus tới nội dung chính. Kiểm tra cả HTTP và mở file trực tiếp.
- Title/description/canonical/schema hợp lệ; không làm hỏng liên kết hoặc tài nguyên.
- Chạy kiểm tra trang, SEO và browser test; dùng Ponytail review diff trước hoàn tất.

Context được tạo từ HTML bằng `python tools/update_contexts.py`; đọc diff và cập nhật
đúng nguồn nội dung trước khi chạy lại. Giải thích hành vi riêng cần giữ ở nguồn và test.
