# Context — Công Cụ Tính Sơn Nhà Chính Xác | Tính Lượng Sơn Cần Dùng

## Vai trò

- File: `tinh-son/index.html`
- URL: `https://sagopaint.vn/tinh-son/`
- Nhóm: Công cụ
- Mục đích: Ước tính diện tích, lượng sơn và chi phí tham khảo.
- Đối tượng: Người chuẩn bị thi công và cần dự toán.
- CTA hiện có: `#tu-van`, `tel:+842866815050`, `mailto:info.sagopaint@gmail.com`.
- Nguồn chỉnh sửa: HTML trực tiếp; assets/js/paint-calculator.js. Sửa template cùng trang nếu thuộc generator.

## Nội dung và ý định tìm kiếm

- Ý định tìm kiếm: Tính lượng sơn cần dùng trước khi hỏi báo giá.
- Nội dung cụ thể là các heading dưới đây; không tự thêm thông số, chứng nhận hoặc lời hứa chưa có nguồn.

- H1: Tính lượng sơn cần dùng
- H2: Nhập thông tin công trình
- H2: Lượng sơn và chi phí
- H2: Sản phẩm phù hợp với nhu cầu của bạn
- H2: Liên hệ tư vấn để nhận báo giá chính xác
- H2: Cách tính lượng sơn cho nhà ở chính xác và dễ áp dụng
- H3: Nhà 100m2 cần bao nhiêu sơn?
- H3: 1 thùng sơn sơn được bao nhiêu m2?
- H3: Sơn nội thất và ngoại thất khác nhau như thế nào?
- H3: Nên sơn bao nhiêu lớp?
- H3: Cách tối ưu chi phí khi tính sơn
- H3: Vì sao kết quả cần được làm tròn lên?
- H3: Những yếu tố làm lượng sơn thay đổi
- H3: Cách dùng công cụ tính sơn cho từng loại công trình
- H3: Khi nào nên nhờ tư vấn thay vì tự tính?
- H3: Liên kết hữu ích
- H2: Câu hỏi thường gặp về tính sơn nhà
- H3: Nhà 100m² cần bao nhiêu sơn?
- H3: Một thùng sơn sơn được bao nhiêu m²?
- H3: Sơn mấy lớp là tốt nhất?
- H3: Bao lâu nên sơn lại nhà?
- H3: Sơn nội thất và ngoại thất khác nhau thế nào?
- H2: Công ty Sơn Sago
- H3: Thông tin liên hệ
- H3: Danh mục

## SEO hiện tại

- Title: Công Cụ Tính Sơn Nhà Chính Xác | Tính Lượng Sơn Cần Dùng
- Description: Công cụ tính sơn miễn phí giúp bạn tính chính xác lượng sơn cần dùng cho nhà ở, căn hộ, văn phòng và công trình. Nhận tư vấn và báo giá nhanh chóng.
- Canonical: `https://sagopaint.vn/tinh-son/`
- Robots: `index, follow`
- Schema: BreadcrumbList, FAQPage, HomeAndConstructionBusiness.
- Ngôn ngữ: `vi`. Giữ URL/canonical và trạng thái index khi sửa giao diện.

## Tài nguyên chính

- `https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&display=swap`
- `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css`
- `../category-pages.css`
- `../assets/css/site-base.css`
- `../assets/css/calculator.css`
- `https://cdn.sagopaint.vn/assets/sago-logo.png`

## Tiêu chí kiểm thử

- Đọc AGENTS.md và DESIGN.md; sử dụng skill ứng với từng phase/hạng mục.
- Font Be Vietnam Pro cho chữ; không tràn ở 360/768/1440px; thử fallback CDN.
- Navigation, CTA, điểm neo hoạt động; keyboard focus rõ và không bị sticky che.
- CSS chung dùng đường dẫn tương đối theo độ sâu HTML; skip link ẩn mặc định, hiện khi Tab và Enter đưa focus tới nội dung chính. Kiểm tra cả HTTP và mở file trực tiếp.
- Title/description/canonical/schema hợp lệ; không làm hỏng liên kết hoặc tài nguyên.
- Chạy kiểm tra trang, SEO và browser test; dùng Ponytail review diff trước hoàn tất.
- Kiểm tra tính phòng/diện tích, preset, số 0, tab bàn phím và email chứa kết quả; không tự gửi hoặc xóa dữ liệu.
- Chỉ kiểm tra input của tab đang chọn: bắt buộc nhập, tuân thủ min/step và số hợp lệ. Input lỗi có aria-invalid, mô tả qua calculationMessage; kết quả đổi thành — và submit focus input lỗi đầu tiên. Diện tích 0 hợp lệ; số quá lớn có thông báo riêng.
- Script tính sơn và ảnh S68 dùng đường dẫn tương đối để công cụ hoạt động khi mở file trực tiếp.
- Tên liên hệ được bỏ khoảng trắng đầu/cuối trước required; điện thoại chấp nhận chữ số quốc tế với + đầu chuỗi, khoảng trắng, dấu chấm, gạch nối và ngoặc. Website chỉ mở email để người dùng tự gửi.
- Giao diện tối giản: hero ngắn, tab nhập liệu bên trái và kết quả bên phải; metric 2 cột, chi phí thành hàng thay vì nhiều hộp; mobile xếp dọc. CTA mobile cố định được bỏ để giữ vùng đọc.
- Số liệu lớn nhưng hợp lệ được phép xuống dòng trong metric và hàng chi phí, không bị cắt bởi vỏ calculator. Thông báo form có tương phản trên nền xám nhẹ.

Context được tạo từ HTML bằng `python tools/update_contexts.py`; đọc diff và cập nhật
đúng nguồn nội dung trước khi chạy lại. Giải thích hành vi riêng cần giữ ở nguồn và test.
