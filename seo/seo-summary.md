# SEO và chất lượng — 09/11/2026

Báo cáo hiện tại bao phủ 54 trang nội dung, 53 URL canonical indexable và trang
lỗi 404 riêng. Bản giao diện tối giản, tối ưu ảnh và các sửa SEO bổ sung đã qua
kiểm tra local. Nhật ký phát hành: docs/tasks/2026-11-09-seo-release.md;
chi tiết audit: docs/audits/2026-11-09-seo-release.md.

## Đã sửa trong bản này

- Trang/asset không tồn tại trước đây trả 200 với HTML trang chủ. Thêm 404.html
  cho Cloudflare Pages và local server để trả đúng mã lỗi. Trang lỗi không vào
  sitemap/inventory nội dung và có noindex, follow.
- Hoàn chỉnh 12 mô tả sản phẩm bị cắt giữa câu, đồng bộ meta, Open Graph,
  Twitter, Product schema, hero và context. Chỉ sử dụng thông tin sẵn có.
  Generator ưu tiên mô tả biên tập, không cắt lại theo mốc 155 ký tự.
- Bỏ 5 đoạn ghi chú chiến lược SEO khỏi Markdown và bài viết công khai;
  sửa alt ảnh phòng khách trên trang chủ theo đúng hình.
- Sửa 3 URL logo sai trong generator phong thủy và thêm hồi quy trong thư mục
  tạm. HTML hiện tại đã đúng nên không sinh lại hàng loạt.
- Cập nhật sitemap lastmod ngày 09/11 theo nội dung/giao diện đã thay đổi.
  Giữ 53 URL, canonical, robots, alias ANAclean -2 và file xác minh Google.
- Các đợt UI/performance trước trong cùng release: giảm bố cục rối, sửa ảnh
  S68 khi mở file, bỏ preload ảnh nền cũ khoảng 283 KB trên 17 trang phong thủy,
  sửa FAQ thời gian khô và kiểm tra dữ liệu tính sơn.

## Kiểm tra local cuối

| Kiểm tra | Kết quả |
|---|---|
| Site/SEO | 54 trang, 53 indexable, 0 lỗi; metadata/schema parse được |
| Canonical/alias/Google verification | Giữ đúng baseline; alias vẫn noindex, follow |
| Nội bộ | 53 URL indexable đều có inbound link; liên kết/asset local không hỏng |
| Generator | 8 tests trong thư mục tạm đạt |
| Unit | 4 tests đóng gói, server, inventory, SEO đạt |
| Browser | 22 tests đạt; gồm 54 trang × 360/768/1440px, ảnh, font, overflow, axe, tính sơn, email và menu |
| Trang lỗi | HTTP404, logo/font, bàn phím và axe đạt tại 360/768/1440px |
| Đóng gói | 99 file public khớp byte nguồn; không docs/tests/dependencies hoặc credentials |
| Review | Không còn Must fix trong source, template, 404 và mô tả sản phẩm |

## Lighthouse mobile của bản release

| Trang | Performance | Accessibility | Best Practices | SEO | LCP | CLS |
|---|---:|---:|---:|---:|---:|---:|
| / |95|100|100|100|2,71s|0,000|
| /son-noi-that |97|100|100|100|2,16s|0,020|
| /blog |95|100|100|100|2,62s|0,018|
| /son-nha-moi-xay |95|100|100|100|2,61s|0,021|
| /phong-thuy-son-nha/ |95|100|100|100|2,46s|0,015|
| /tinh-son/ |98|100|100|100|1,85s|0,056|

Lighthouse 13.6 mobile simulated throttling tại localhost, một lượt mỗi trang;
không coi chênh lệch nhỏ là cải thiện chắc chắn. Đợt đo có kiểm soát riêng cho
hub phong thủy ghi trung vị 3 lượt LCP 3,85→2,40s sau khi bỏ preload ảnh thừa.
LCP trang chủ/blog/bài hướng dẫn còn trên 2,5s ở lượt đo release; CSS/font/ảnh
ngoài vẫn có cơ hội tối ưu. Không suy ra Core Web Vitals thực địa từ điểm lab.

## Cơ hội SEO tiếp theo

Hai URL Aqua Shield có tên gần trùng; cần nguồn SKU để xác nhận có nên gộp,
không tự đổi URL/canonical hoặc giảm trang khi chưa rõ sản phẩm. Nhóm bài phong
thủy có ý định tìm kiếm giao nhau; cần truy vấn/landing page từ Search Console
để phân vai nội dung. Không tự thêm giá/đánh giá vào Product schema.

## Bằng chứng và production

output/seo-release/ chứa các audit, mapping mô tả, npm-test.txt,
lighthouse/summary.json, public-manifest.json, ảnh và logs release.
Kết quả commit/deploy/HTTP live sẽ ghi trong nhật ký phát hành sau khi hoàn tất.
Robots production có phần Cloudflare Managed Content bên cạnh file nguồn;
kiểm tra riêng sitemap/crawl và giữ nguyên cấu hình bot của chủ website.

Chưa kiểm tra Search Console, traffic/thứ hạng, rich-result eligibility bằng
Google, Core Web Vitals thực địa, Safari/Firefox hoặc thiết bị thật.
