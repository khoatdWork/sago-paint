# Kiểm tra toàn bộ website Sago Paint

Yêu cầu: kiểm tra lại trang chủ và toàn bộ trang còn lại. Phạm vi: 54 trang nội
dung (53 indexable, một alias noindex), file xác minh, ảnh/tài nguyên/liên kết,
responsive, bàn phím, calculator, SEO và nguồn generator/build.

Production được khảo sát: https://sagopaint.vn, release 6d46fe7. Repository bắt
đầu tại HEAD a2ecc13, working tree sạch. Các sửa lỗi của lần audit này ở local;
không commit, push hoặc deploy. Đã đọc AGENTS.md, DESIGN.md, docs/pages/README.md
và context liên quan trước khi sửa. Báo cáo: [site audit](../audits/2026-11-09-site-audit.md).

| Phase/hạng mục | Skill đã sử dụng | Đầu vào | Kết quả/bằng chứng | Điều kiện hoàn tất | Trạng thái |
|---|---|---|---|---|---|
| 1. Khảo sát | frontend-static-site, ponytail, ponytail-audit, seo-audit, web-design-guidelines | Source/context, 54 route production, baseline tests | 162 lượt render live; kiểm tra SEO 54 trang; audit UI thêm 27 lượt và interaction. Finding có case tái hiện trong ba báo cáo agent | Lỗi có case, nguồn và evidence; không ghi false positive #top là link hỏng | Đạt |
| 2. Phương án | frontend-static-site, frontend-design, ponytail | Finding đã xác minh, DESIGN.md, generator/caller | Sửa validation; lấy đúng thời gian khô từ thông số sẵn có; bỏ alias khỏi danh mục/related; dùng đường dẫn ảnh tương đối. Giữ metadata/canonical, không thay CSS chung | Chốt phạm vi, test hồi quy và tác động SEO; CLS ghi riêng | Đạt |
| 3. Thực hiện: calculator | frontend-static-site, ponytail | HTML/JS tính sơn, case số âm/badInput/số lớp lẻ và contact rỗng | Kiểm tra native validity của panel đang chọn; chặn kết quả/email sai; trim tên, kiểm tra phone; sửa ID trùng, JS/ảnh khi mở file; cập nhật context | Đủ HTML/JS/context; không gửi email thật | Đạt |
| 3. Thực hiện: FAQ/danh mục | frontend-static-site, seo, ponytail | Thông số có nguồn ở 5 sản phẩm, alias noindex, refresh_pages.py | FAQ visible/JSON-LD khớp thời gian khô; alias không còn trong card/ItemList/related. Generator cập nhật đúng schema sinh ra, giữ dữ liệu khác; test trong thư mục tạm | Sửa source/template/output/context; giữ alias/canonical và dữ liệu doanh nghiệp | Đạt |
| 3. Thực hiện: ảnh local | frontend-static-site, ponytail | S68 root-relative ở 24 HTML và calculator; template phong thủy | Đường dẫn tương đối theo độ sâu; sửa template 17 trang phong thủy, output/context và site check; thêm test file preview | Ảnh hoạt động qua HTTP và file ở các độ sâu; không tái sinh hàng loạt source | Đạt |
| 4. Kiểm thử/SEO | webapp-testing, seo, web-design-guidelines | Dist sau build, source, production baseline, test hồi quy | npm test đạt: 7 generator, 4 unit, 22 browser; 54 trang × 360/768/1440; Lighthouse trước/sau; invariants 54 trang không vi phạm | Test phù hợp đạt; giới hạn và CLS còn lại được ghi trong báo cáo | Đạt, có giới hạn đã ghi |
| 5. Review | ponytail-review | Diff cuối, calculator/generator/caller, findings ban đầu | Review độc lập không còn Must fix trong thay đổi; đã khôi phục tiếng Việt của fixture bị đổi nhầm, chạy lại 7 generator đạt | Đối chiếu finding/test; không còn Must fix trong phạm vi sửa; báo rủi ro thực tế | Đạt |

## Lệnh và bằng chứng

Evidence tại `output/site-audit/2026-11-09/`:

- `local-before.txt`: npm test baseline đạt 6 generator, 4 unit, 14 browser.
- `live-{360,768,1440}.json`, `live-run.txt`, `live-screenshots/` và contact sheets:
  crawl/render production đủ 54 trang mỗi kích thước. Không có ảnh tải hỏng,
  overflow ngang, lỗi JavaScript hay vi phạm axe WCAG trong lượt đo.
- `local-after.txt`: npm test sau sửa đạt 7 generator, 4 unit, 22 browser;
  build tạo 94 public files trong dist; kiểm tra full 54 trang ở 3 kích thước
  bao gồm ID trùng. Generator chạy trong thư mục tạm.
- `generators-final.txt`: chạy lại 7 generator sau khi khôi phục fixture tiếng Việt,
  đạt. Hai test root file preview được định dạng lại, không đổi logic.
- `invariants.json`: 54 trang không vi phạm; metadata/canonical và schema ngoài
  FAQ/ItemList giữ nguyên; homepage, Google verification, robots, sitemap không đổi.
- `lighthouse-before/summary.json`: 6 nhóm trang; performance 91–97,
  accessibility/best practices/SEO 100. `lighthouse-after/summary.json`: 4 trang
  đại diện liên quan; performance 92–98, ba nhóm điểm còn lại 100.
- `final-site-check.txt`, `final-seo-check.txt`, `diff-check.txt`: kiểm tra
  site/SEO/whitespace cuối đều đạt.

Báo cáo nhánh và test tái hiện tại `output/site-audit/seo-agent/`, `ui-agent/`,
`interaction-agent/`. Review cuối: `seo-agent/final-review.md`,
`interaction-agent/FIX-REVIEW.md` và phần review của `ui-agent/REPORT.md`.

## Giới hạn và rủi ro còn lại

- Trang phong thủy có CLS lab 0,117 do font swap làm đoạn đầu thay số dòng;
  blog có LCP baseline 3,32 giây. Chưa tối ưu hai chỉ số này trong lần sửa lỗi.
  Không dùng chiều cao chữ cố định hay thay chính sách font để che kết quả.
- Chromium và mô phỏng viewport; chưa thử thiết bị thật, Safari/Firefox,
  screen reader hoặc gửi qua ứng dụng email. Không có dữ liệu Search Console,
  thứ hạng/index Google hay Core Web Vitals thực tế.
- Production được khảo sát trước sửa; bản sửa mới chỉ được kiểm tra local/dist.
