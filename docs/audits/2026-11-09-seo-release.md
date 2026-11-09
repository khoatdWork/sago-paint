# Kiểm tra SEO bổ sung và phát hành

Phạm vi: 54 trang nội dung, 53 URL canonical indexable, toàn bộ template và
đóng gói public. Website tĩnh của Sago Paint phục vụ người tìm hệ sơn, hướng
dẫn thi công/phối màu và liên hệ tư vấn. Đọc source, DESIGN, context và kiểm
tra HTTP production; không có dữ liệu Search Console hoặc thứ hạng thực tế.

## Phát hiện đã xử lý

| Vấn đề và bằng chứng | Sửa nguồn/đầu ra | Xác minh |
|---|---|---|
| URL trang và ảnh không tồn tại đều trả 200 với HTML trang chủ; đây là phản hồi lỗi không đúng mã HTTP | Thêm 404.html để Cloudflare Pages xử lý lỗi native; local server trả HTML 404 với GET/HEAD; loại trang lỗi khỏi inventory nội dung/sitemap, vẫn đóng gói public | live-before.json tái hiện; unit trước sửa thất bại/sau sửa đạt. Browser local 360/768/1440 kiểm tra ảnh/logo/font/keyboard/axe đạt. Chờ xác minh production sau deploy |
| 12 mô tả sản phẩm kết thúc giữa câu như “Với.”, “mang lại bề.”, “đảm bảo rằng.” | Viết lại câu hoàn chỉnh chỉ từ chi tiết có sẵn; đồng bộ meta/OG/Twitter/Product schema/hero và bản sao liên quan. Generator ưu tiên mô tả biên tập, không cắt lại ở 155 ký tự | mapping/check trong output; regression temp giữ đúng mô tả dài, dấu nháy/entity, thứ tự thuộc tính và roundtrip; 6 mô tả tốt giữ nguyên |
| 5 bài viết lộ ghi chú biên tập “Search intent”, “Các bài đang xếp hạng cao”, “Điểm cần bổ sung” | Bỏ đúng đoạn ghi chú trong cả Markdown và HTML, giữ intro/hướng dẫn thực tế | content-cleanup-checks.json; head của cả 5 bài không đổi |
| Generator phong thủy ghép origin website vào URL logo CDN tuyệt đối | Sửa publisher.logo, og:image và twitter:image trong template; HTML hiện tại đã đúng nên không sinh lại hàng loạt | 54 trang/647 tham chiếu JSON-LD/social không có double-origin; regression 17 output temp xác minh URL chính xác |
| Alt ảnh phòng khách ở trang chủ mô tả thành nhà cấp 4 ngoại thất | Sửa alt theo đúng nội thất trong ảnh | Đọc ảnh/source; không thay asset hay layout |
| Sitemap chưa phản ánh các thay đổi nội dung/giao diện ngày 09/11 | Đồng bộ lastmod theo mtime nguồn trước commit; giữ đúng 53 URL | seo-sync: 0 head sửa ngoài phạm vi, robots không đổi, 0 quality issue |

## Bất biến và kiểm tra

Canonical công khai giữ nguyên, root bỏ .html và thư mục giữ dấu /. Alias
ANAclean -2 vẫn noindex, follow, canonical về bản chính. Google verification
giữ nguyên byte. Không thêm giá, đánh giá, chứng nhận hay schema không có nguồn.
Trang 404 có noindex, follow, không canonical/sitemap và không tăng 54 trang
nội dung. Tất cả 53 trang indexable có liên kết nội bộ trỏ tới.

Review độc lập: release-review.md và seo-final-review.md, không còn Must fix.
`npm test` exit 0: site/SEO, 8 generator, 4 unit và 22 browser test đạt, gồm
54 trang × 360/768/1440px. Kiểm tra riêng 404 ở 3 kích thước đạt HTTP, ảnh,
font, bàn phím và axe serious/critical bằng 0. Build có 99 file public khớp
byte nguồn, không docs/tests/dependencies hay credentials. Git diff --check đạt.
Lighthouse mobile bản cuối: 6 nhóm trang có performance 95–98, accessibility,
best practices và SEO đều 100. LCP home/blog/bài hướng dẫn khoảng 2,6–2,7s,
còn dư địa tối ưu tài nguyên ngoài. Bảng số liệu ở seo/seo-summary.md; đây là
lab một lượt mỗi route, không xác nhận thứ hạng hoặc Core Web Vitals thực địa.
Production code d8dfb26 đã phát hành tại https://sagopaint.vn/ qua deployment
758ae9a4-7412-4895-a63d-a9c69971a559. Kiểm tra cả custom domain và deployment
domain: 54 trang metadata/schema đúng, 41 asset khớp byte/MIME, Google
verification giữ nguyên, 8 redirect đúng đích. Missing page và missing image
GET/HEAD trả đúng HTTP404 (4 trường hợp/domain), không còn 200 trang chủ.
Browser production 24 trường hợp ở 3 kích thước đạt ảnh/font/layout/bàn phím/
menu/axe. GitHub Actions run 42573978284 success cho đúng code commit.
Chi tiết SHA/log/giới hạn trong docs/tasks/2026-11-09-seo-release.md.

## Cơ hội nội dung cần xác minh thêm

- Hai URL Aqua Shield đang indexable có cùng tên hiển thị. Cần xác nhận với
  nguồn sản phẩm có phải cùng SKU trước khi gộp/canonical/redirect; đợt này giữ
  URL đã công khai và không suy đoán từ tên gần giống.
- Hub phong thủy và các bài theo năm có phần ý định tìm kiếm gần nhau. Dữ liệu
  truy vấn/landing page từ Search Console sẽ giúp quyết định phân vai hoặc gộp
  bài; không kết luận tranh hạng chỉ từ nội dung giống nhau.
- Product schema có thể cần dữ liệu giá/đánh giá thực để đủ điều kiện một số
  rich results. Không tự tạo Offer/rating để đạt công cụ kiểm tra.

## Bằng chứng và giới hạn

`output/seo-release/`: live-before.json, schema-audit.md, on-page-audit.md,
product-description-audit.md, product-description-mapping.json,
product-description-check.json, 404-review.md, 404-browser.json,
release-review.md, seo-final-review.md và logs kiểm tra/release.

Robots trên production có phần Cloudflare Managed Content ngoài file nguồn;
phần cuối vẫn cho phép crawl chung và trỏ sitemap canonical. Không thay cấu
hình bot hoặc DNS ngoài phạm vi release. Host www không kết nối được ở lượt
kiểm tra; các canonical và liên kết hiện tại dùng domain apex sagopaint.vn.

Chưa có bằng chứng Google lập chỉ mục, rich-result eligibility, traffic hoặc
Core Web Vitals thực địa. Chưa kiểm tra Safari/Firefox và thiết bị thật.
