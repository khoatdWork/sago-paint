# Tối ưu tải trang sau đợt chỉnh giao diện

Mục tiêu: xử lý phần tải chậm còn lại, ưu tiên nhóm phong thủy, giữ giao diện tối
giản đã được người dùng chọn. Phạm vi chính là tài nguyên đầu trang và template
phong thủy; không đổi nội dung, URL hoặc metadata SEO. Baseline là source hiện
tại sau redesign, không phải Git HEAD trước redesign.

Context: `docs/pages/README.md`, `docs/pages/phong-thuy-son-nha/CONTEXT.md`,
context mệnh/tuổi bị ảnh hưởng và `DESIGN.md`.

| Phase/hạng mục | Skill đã sử dụng | Đầu vào | Kết quả/bằng chứng | Điều kiện hoàn tất | Trạng thái |
|---|---|---|---|---|---|
| 1. Khảo sát | frontend-static-site, ponytail, ponytail-audit, seo-audit, web-design-guidelines | Lighthouse redesign, source/template, resource timing và header production | Snapshot99file/54trang; preload ảnh cũ khoảng283KB trên17trang; `resource-audit.md`, `analysis-agent/REPORT.md` | Có nguyên nhân và baseline so sánh | Đạt |
| 2. Phương án | frontend-static-site, frontend-design, ponytail | Hướng tối giản và layout hiện tại; thử nghiệm ở output | Chọn bỏ17preload thừa. Không thêm preload/font/header/dependency vì xóa tải thừa đã giải quyết điểm nghẽn. Test nguồn, Lighthouse, browser và SEO | Chốt thay đổi nhỏ và kiểm tra tương ứng | Đạt |
| 3. Thực hiện | frontend-static-site, ponytail | 17HTML, template head và context hub/16mệnh-tuổi | MỗiHTML bỏ đúng1dòng; template đã không sinh preload này nên không cần sửa. Layout và tài nguyên hiển thị không đổi; context hiện tại vẫn đúng | Đồng bộ đầu ra/template/context | Đạt |
| 4. Kiểm thử/SEO | webapp-testing, seo, web-design-guidelines | Source sau tối ưu, snapshot trước | `source-preservation.json`: chỉ 17 dòng bị xóa. `measurement-summary.json`: trung vị LCP 3848→2401ms, perf 87→96. `npm-test.txt`: site/SEO, 7 generator, 4 unit và 22 browser đạt, bao gồm 54 trang × 3 viewport. `visual-check.json`: 9/9 layout và screenshot giống hệt nhau, ảnh/menu đạt, không request ảnh cũ | Site/SEO/generator/browser phù hợp; đo cùng điều kiện; giữ hình thức | Đạt |
| 5. Review | ponytail-review | Diff tối ưu so snapshot, nguồn/CSS/template và kiểm thử | `final-review.md`, `review-diff.json`: không có Must fix/Should fix; xác nhận ảnh cũ không dùng trong CSS/hero và template không tái tạo. Tất cả kiểm tra của root hoàn tất | Không còn Must fix; nêu giới hạn đo lab | Đạt |

Chưa commit/push/deploy trong đợt tối ưu này. Không xem điểm lab là bằng chứng
Core Web Vitals thực địa hoặc trạng thái lập chỉ mục Google.

Lighthouse mobile13.6, server và cấu hình không đổi;3lần hub mỗi phiên bản,
trung vị LCP giảm37,6%. Hub không dịch bố cục trong cả6lần đo (CLS0).
Tuổi1998 một cặp đo97điểm cảtrước/sau, LCP2169→2149ms; không tuyên bố cải
thiện LCP riêng trang này từ chênh lệch nhỏ. Vẫn bỏ được request ảnh không dùng.
Các lượt đo/thử nghiệm độc lập ở `output/performance-followup/`.

`npm test` hoàn tất exit 0; build trong suite tạo 98 file công khai ở `dist`.
Đối chiếu giao diện dùng hub/mệnh Kim/tuổi 1998 × 360/768/1440px, chờ font và
ảnh giải mã rồi so ảnh chụp byte/hash; cả 9 trường hợp giống hệt trước/sau.
Không thêm test vào repo cho việc xóa hint đơn giản; dùng suite hiện có và
script xác minh trong output. Báo cáo: `docs/audits/2026-11-09-performance-followup.md`.
