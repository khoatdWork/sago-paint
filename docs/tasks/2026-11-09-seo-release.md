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
| 3. Release | frontend-static-site | Toàn bộ thay đổi giao diện/performance đã được yêu cầu | Chưa commit/push/deploy | Commit và remote khớp, deploy đúng dist | Chưa làm |
| 4. Kiểm thử/SEO | seo, webapp-testing, web-design-guidelines | Bản cuối, kiểm tra local và live | npm test exit 0: site/SEO, 8 generator, 4 unit, 22 browser (54 trang × 3 viewport). Trang 404 đạt HTTP/font/logo/keyboard/axe ở 3 kích thước. Dist 99 file khớp byte source. Lighthouse 6 nhóm: perf 95–98, accessibility/best practices/SEO đều 100; chờ live | Checks phù hợp đạt; xác minh 54 trang/asset/redirect trên production | Local/Lighthouse đạt; chờ live |
| 5. Review | ponytail-review | Diff và luồng liên quan, audit trước | `release-review.md`, `seo-final-review.md`: không còn Must fix/Should fix; kiểm tra đủ parser/404/alias/schema/đóng gói | Không còn Must fix; ghi giới hạn thực tế | Đạt source; chờ live |

Bằng chứng lưu ở `output/seo-release/`; báo cáo hoàn tất sẽ ghi rõ commit,
deployment, kiểm tra thực sự chạy và phần chưa có dữ liệu.
