# Context — Nhà Mới Xây Bao Lâu Thì Sơn Được? Kinh Nghiệm Cho Miền Tây | Sago Paint

## Vai trò

- File: `son-nha-moi-xay.html`
- URL: `https://sagopaint.vn/son-nha-moi-xay`
- Nhóm: Bài hướng dẫn
- Mục đích: Giải đáp nhu cầu cụ thể và gợi ý hệ sơn liên quan.
- Đối tượng: Chủ nhà và người tìm hướng dẫn thi công/phối màu.
- CTA hiện có: `tel:+842866815050`, `mailto:info.sagopaint@gmail.com`.
- Nguồn chỉnh sửa: tools/generate_blog_pages.py và content/blog/*.md. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: Nhà Mới Xây Bao Lâu Thì Sơn Được? Kinh Nghiệm Cho Miền Tây | Sago Paint.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Nhà Mới Xây Bao Lâu Thì Sơn Được? Kinh Nghiệm Thực Tế Cho Gia Chủ Miền Tây
- H2: Giới thiệu
- H2: Nhà mới xây bao lâu thì sơn được?
- H3: Mốc tham khảo trong điều kiện bình thường
- H3: Không nên chỉ nhìn bề mặt ngoài
- H2: Các yếu tố làm tường miền Tây khô chậm
- H3: Mùa mưa và độ ẩm cao
- H3: Tường dày, phòng bí và chân tường ẩm
- H3: Hồ vữa, bột trét và quy trình bảo dưỡng
- H2: Dấu hiệu tường đã đủ điều kiện sơn
- H2: Quy trình sơn nhà mới xây chuẩn cho miền Tây
- H3: Bước 1: Vệ sinh và xử lý lỗi bề mặt
- H3: Bước 2: Chống thấm các khu vực rủi ro
- H3: Bước 3: Bả bột đúng loại và đúng độ dày
- H3: Bước 4: Sơn lót chống kiềm
- H3: Bước 5: Sơn phủ đủ lớp
- H3: Bước 6: Nghiệm thu sau khi khô
- H2: Có nên sơn nhà mới trong mùa mưa?
- H2: Nhận tư vấn màu sơn miễn phí
- H2: Câu hỏi thường gặp
- H2: Kết luận
- H2: Cần chọn hệ sơn phù hợp?
- H2: Công ty Sơn Sago
- H3: Thông tin liên hệ
- H3: Danh mục

## SEO hiện tại

- Title: Nhà Mới Xây Bao Lâu Thì Sơn Được? Kinh Nghiệm Cho Miền Tây | Sago Paint
- Description: Nhà mới xây bao lâu thì sơn được trong khí hậu miền Tây? Hướng dẫn thời gian chờ, kiểm tra độ ẩm, xử lý tường và hệ sơn bền đẹp.
- Canonical: `https://sagopaint.vn/son-nha-moi-xay`
- Robots: `index, follow`
- Schema: Article, BreadcrumbList, FAQPage.
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `category-pages.css`
- `assets/css/site-base.css`
- `assets/css/editorial.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`
- `https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=1400&q=84`
- `https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=82`
- `https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&w=1200&q=82`
- `https://images.unsplash.com/photo-1562259949-e8e7689d7828?auto=format&fit=crop&w=1200&q=82`
- `https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=82`
- `https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?auto=format&fit=crop&w=1200&q=82`

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
