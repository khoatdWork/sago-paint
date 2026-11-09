# Rà soát SEO và xuất bản giao diện mới

Người dùng yêu cầu commit, deploy toàn bộ giao diện/tối ưu hiện tại, đồng thời
kiểm tra SEO thêm và sửa những điểm có bằng chứng. Giữ hướng tối giản, URL
canonical, alias ANAclean noindex và file xác minh Google. Không tự tạo dữ liệu
Search Console, giá, đánh giá hoặc chứng nhận sản phẩm.

Phạm vi: 54 trang nội dung, generator, sitemap/robots/redirect, bản public dist
và kiểm tra production sau deploy. Đọc DESIGN, inventory/context liên quan.

| Phase/hạng mục | Skill đã sử dụng | Đầu vào | Kết quả/bằng chứng | Điều kiện hoàn tất | Trạng thái |
|---|---|---|---|---|---|
| 1. Khảo sát | frontend-static-site, ponytail-audit, seo-audit, web-design-guidelines | Source 54 trang, các báo cáo UI/performance, template, cấu hình deploy và HTTP production | Audit trong `output/seo-release/`: soft404, 12 mô tả cắt câu, 5 đoạn ghi chú nội bộ, generator URL logo sai; các URL/canonical còn lại hợp lệ | Có lỗi hoặc cơ hội cụ thể với bằng chứng | Đạt |
| 2. Phương án | frontend-static-site, frontend-design, seo, ponytail | Audit SEO, bất biến DESIGN/AGENTS | Thêm 404 native theo nhận diện tối giản; sửa copy từ dữ liệu sẵn có; bảo vệ mô tả biên tập trong generator; sửa URL template; sync sitemap trước commit | Chốt phạm vi/check/ảnh hưởng SEO | Đạt |
| 3. SEO kỹ thuật | seo, frontend-static-site, frontend-design | Metadata/schema, sitemap/robots và generator | 404/server/inventory/docs đồng bộ; 12 mô tả meta/social/schema/hero/context sửa đầy đủ; Markdown/HTML 5 bài cùng sửa; logo generator và regression temp; sitemap 53 URL lastmod 09/11 | Source/output/context đồng bộ, không sinh hàng loạt ngoài phạm vi | Đạt |
| 3. Release | frontend-static-site | Toàn bộ thay đổi giao diện/performance đã được yêu cầu | Commit d8dfb26 (148 file) push origin/main; Cloudflare Pages production 758ae9a4 từ đúng commit, chỉ deploy 99 file public trong dist | Commit và remote khớp, deploy đúng dist | Đạt |
| 4. Kiểm thử/SEO | seo, webapp-testing, web-design-guidelines | Bản cuối, kiểm tra local và live | npm test exit 0: site/SEO, 8 generator, 4 unit, 22 browser (54 trang × 3 viewport). Trang 404 đạt 3 kích thước. Lighthouse 6 nhóm: perf 95–98, các điểm khác 100. Live cả custom/deployment domain: 54 trang, 41 asset, 8 redirect, 4 lỗi GET/HEAD đúng 404. Browser production 24 trường hợp đạt; CI success | Checks phù hợp đạt; xác minh 54 trang/asset/redirect trên production | Đạt |
| 5. Review | ponytail-review | Diff và luồng liên quan, audit trước | `release-review.md`, `seo-final-review.md`: không còn Must fix/Should fix; parser/404/alias/schema/đóng gói và kiểm tra live hoàn tất | Không còn Must fix; ghi giới hạn thực tế | Đạt |

Bằng chứng lưu ở `output/seo-release/`; báo cáo hoàn tất sẽ ghi rõ commit,
deployment, kiểm tra thực sự chạy và phần chưa có dữ liệu.

## Kết quả phát hành

- Code commit `d8dfb265472cc5a1ba09e32a03cbf1dcbe40f79e`, đã push origin/main.
  Staged scan 148 file không có output/cache/private path hoặc mẫu credentials;
  staged diff --check đạt. Không thay file xác minh Google.
- `npm run build` tạo 99 file công khai; `wrangler pages deploy dist` với
  project sagopaint, branch main, commit-hash đúng SHA code hoàn tất.
  Deployment ID `758ae9a4-7412-4895-a63d-a9c69971a559`, URL
  https://758ae9a4.sagopaint.pages.dev và https://sagopaint.vn/.
- `verify-live.cjs` đạt trên cả hai domain: 54 trang HTTP200, title/description/
  canonical/robots và JSON-LD khớp source; 41 asset (gồm sitemap) khớp SHA256,
  MIME ảnh đúng; Google verification khớp byte sau redirect .html native;
  8 redirect đúng status/đích; trang và ảnh không tồn tại GET/HEAD đều 404,
  GET có nội dung noindex, follow, HEAD rỗng. Lượt đầu script quên theo redirect
  verification nên dừng assert; sửa script kiểm tra redirect thực, không sửa
  production/file xác minh để làm đạt.
- `node tools/seo-sync.js --check --check-live` exit 0: sitemap/robots200,
  53 URL indexable và 8 redirect không lỗi. Live JSON chi tiết ở
  `live-sagopaint.vn.json`, `live-758ae9a4.sagopaint.pages.dev.json`.
- `browser-production.json`: 8 route đại diện × 360/768/1440px, gồm trang lỗi,
  ảnh giải mã thành công, font tải thật, không overflow/pageerror/axe
  serious/critical; skip link và menu hoạt động. Đã xem screenshot home mobile.
- GitHub Actions https://github.com/khoatdWork/sago-paint/actions/runs/42573978284
  success cho đúng code commit: npm test, Lighthouse 6 trang và artifact đều
  hoàn tất. `ci.json` chứa trạng thái/jobs cuối.
- Sau deploy chỉ cập nhật tài liệu xác minh trong commit riêng; không sửa
  99 file public. Bản production giữ đúng code commit ở trên.

Giới hạn: chưa có Search Console/traffic/ranking/field Core Web Vitals, chưa
Safari/Firefox/thiết bị thật. Cơ hội gộp các URL Aqua Shield hoặc phân vai bài
phong thủy cần nguồn SKU/truy vấn trước khi thay đổi URL. Domain www chưa kết
nối được từ lượt kiểm tra, các URL canonical dùng apex sagopaint.vn.
