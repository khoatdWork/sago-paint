# Context — Phong Thủy Sơn Nhà: Chọn Màu Hợp Mệnh, Hợp Tuổi

## Vai trò

- File: `phong-thuy-son-nha/index.html`
- URL: `https://sagopaint.vn/phong-thuy-son-nha/`
- Nhóm: Phong thủy
- Mục đích: Gợi ý phối màu theo mệnh/tuổi và dẫn tới sản phẩm phù hợp.
- Đối tượng: Chủ nhà tìm màu sơn theo phong thủy.
- CTA hiện có: `tel:+842866815050`, `#tu-van`, `mailto:info.sagopaint@gmail.com`.
- Nguồn chỉnh sửa: tools/generate_fengshui_pages.py — ELEMENTS/AGES/pillar/element_page/age_page. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: Phong Thủy Sơn Nhà: Chọn Màu Hợp Mệnh, Hợp Tuổi.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Phong Thủy Sơn Nhà - Chọn Màu Sơn Hợp Mệnh, Hợp Tuổi Để Thu Hút Tài Lộc
- H2: Vai trò của màu sơn trong phong thủy nhà ở
- H2: Ý nghĩa ngũ hành trong thiết kế nhà ở
- H2: Cách chọn màu sơn theo mệnh
- H2: Cách chọn màu sơn theo tuổi
- H2: Các sai lầm khi chọn màu sơn phong thủy
- H2: Quy trình chọn màu sơn phong thủy thực tế
- H2: Gợi ý màu theo từng không gian
- H2: Sản phẩm và hệ thi công nên đi cùng màu phong thủy
- H2: Bài Viết Theo Năm Sinh Nổi Bật
- H2: Sản phẩm sơn nên dùng
- H2: Câu hỏi thường gặp
- H2: S68 Pro - giải pháp chống thấm cao cấp cho màu sơn phong thủy hiện đại
- H2: Nhận tư vấn màu sơn phong thủy cùng Sago Paint

## SEO hiện tại

- Title: Phong Thủy Sơn Nhà: Chọn Màu Hợp Mệnh, Hợp Tuổi
- Description: Hướng dẫn chọn màu sơn nhà hợp phong thủy theo mệnh, tuổi, không gian sống và gợi ý S68 Pro bền đẹp, hiện đại, dễ vệ sinh.
- Canonical: `https://sagopaint.vn/phong-thuy-son-nha/`
- Robots: `index, follow`
- Schema: Article, BreadcrumbList, FAQPage, HomeAndConstructionBusiness.
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `../phong-thuy-son-nha/styles.css`
- `../assets/css/site-base.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`
- `https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1400&q=82`
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
