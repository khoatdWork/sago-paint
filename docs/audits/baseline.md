# Baseline — 08/11/2026

What this repo does: Website tĩnh Sago Paint phục vụ người tìm sơn, cách thi công,
phối màu và công cụ tính vật tư. Giả định tải: nhiều lượt đọc qua CDN; công cụ
tính sơn chạy trong trình duyệt; generator chỉ chạy bởi người bảo trì.

Skills sử dụng: frontend-static-site, Ponytail ponytail-audit, web-design-guidelines,
seo-audit. Nguồn Ponytail: DietrichGebert/ponytail, commit 96608e078b2d5ea607c5c3b8b5a54d1c1fba6846.

## Must fix

1. **Generator ghi đè nhầm loại trang** — `tools/refresh_pages.py`, hàm main.
   - Hiện trạng: chọn mọi root HTML ngoài index/about/danh mục làm sản phẩm.
   - Lỗi: 14/32 file được chọn không có Product schema, gồm blog và xác minh Google.
   - Sửa: nhận diện Product tích cực, test file khác giữ nguyên byte và giữ noindex.
   - Nếu bỏ qua: chạy cập nhật sản phẩm có thể phá nội dung và xác minh tên miền.
2. **Form không gửi nhưng xóa dữ liệu** — `tinh-son/index.html`, submit consultForm.
   - Hiện trạng: preventDefault, không request tới nơi nhận, rồi form.reset().
   - Lỗi: người dùng mất dữ liệu sau khi tưởng đang yêu cầu tư vấn.
   - Sửa: mở email với nội dung rõ, giữ dữ liệu và cung cấp nút gọi.
   - Nếu bỏ qua: mất cơ hội liên hệ và gây hiểu nhầm.
3. **Tràn mobile và tab không điều khiển bằng mũi tên** — nhóm blog/phong thủy/tính sơn.
   - Bằng chứng: Chromium 390px, blog son-nha-moi-xay có visual rộng 533px;
     gutter nhóm phong thủy vượt viewport; ArrowLeft tại tab-area không đổi tab.
   - Sửa: giới hạn flex/image đúng và gutter; roving tabindex/keyboard handlers.
   - Nếu bỏ qua: khó đọc trên điện thoại và khó sử dụng bằng bàn phím.

## Should fix

4. **Template phong thủy ghép ../ trước URL CDN tuyệt đối** — product_highlight.
   - Lỗi: generator sinh URL ảnh sai ở route sâu; bản HTML hiện tại đã được sửa tay.
   - Sửa: URL tuyệt đối không ghép root; test độ sâu 1 và 2.
   - Nếu bỏ qua: lần sinh tiếp theo làm hỏng ảnh.
5. **SEO hiện có chưa bao phủ đủ chất lượng** — seo-summary chỉ ghi 41 trang,
   script báo 0 lỗi nhưng có ba trang không có inbound internal link:
   cach-tinh-luong-son-can-dung, mau-son-phong-khach-nha-nho, son-nha-hop-phong-thuy-2026.
   - Sửa: kiểm tra graph liên kết, cập nhật báo cáo và exit code của audit.
   - Nếu bỏ qua: báo cáo thành công không chứng minh mọi trang được kiểm tra.
6. **Thiếu quy trình/tài liệu/test** — AGENTS/DESIGN/context chưa có;
   `.codex/skills` bị gitignore; deploy trực tiếp repo gốc.
   - Sửa: skills versioned, context từng trang, test và output deploy công khai riêng.
   - Nếu bỏ qua: máy khác thiếu hướng dẫn, tài liệu nội bộ có thể được upload.

## Phạm vi kiểm tra

54 trang nội dung, 53 indexable, một file xác minh; parse title/canonical/H1/JSON-LD
và link nội bộ tất cả trang. Browser baseline: 8 trang đại diện ở 390 và 1440px,
không có pageerror; test tính 100m²/2 lớp cho 20L, 2 thùng, 2.550.000 VNĐ.
Không đánh dấu ảnh lazy chưa tải là ảnh hỏng: sau eager load không thấy ảnh hỏng
ở các trang kiểm tra bổ sung. Fragment #top là hành vi HTML hợp lệ.
Ảnh trước thay đổi lưu `output/baseline` (artifact, không đưa vào Git).

Verdict: sửa generator và luồng tư vấn trước; sau đó typography, responsive và test.
Not checked: Search Console, thứ hạng, traffic, Core Web Vitals thực tế, production deploy.
