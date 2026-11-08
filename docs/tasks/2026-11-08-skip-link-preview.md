# Sửa skip link hiện mặc định khi xem HTML trực tiếp

Mục tiêu: liên kết “Bỏ qua điều hướng” ẩn khi đọc trang, hiện khi Tab và đưa focus
vào nội dung chính khi Enter. Phạm vi: đường dẫn CSS chung của 54 trang và ba
generator; context, validator và hồi quy browser. Giữ nội dung, CSS và SEO hiện có.
Đã đọc DESIGN.md, docs/pages/README.md và context các nhóm trang liên quan.

| Phase/hạng mục | Skill đã sử dụng | Đầu vào | Kết quả/bằng chứng | Điều kiện hoàn tất | Trạng thái |
|---|---|---|---|---|---|
| 1. Khảo sát | frontend-static-site, ponytail, ponytail-audit, seo-audit, web-design-guidelines | Ảnh người dùng, HTML/CSS/template/test/context | Chromium HTTP ẩn đúng; file:// yêu cầu file:///E:/assets/css/site-base.css thất bại, link xanh position:static tại y=79 | Có trường hợp tái hiện | Đạt |
| 2. Phương án | frontend-static-site, frontend-design, ponytail | Luồng tải CSS theo độ sâu trang | Đổi duy nhất href stylesheet chung thành đường dẫn tương đối; giữ skip link hỗ trợ bàn phím; test HTTP và file:// | Chốt phạm vi/test/SEO | Đạt |
| 3. Thực hiện: HTML/template/context | frontend-static-site, ponytail | 54 HTML, ba generator, nguồn context | Chỉ đổi href theo độ sâu; cập nhật DESIGN và nguồn context rồi tạo lại 54 context | Các nguồn đồng bộ, không đổi SEO/nội dung | Đạt |
| 4. Kiểm thử/SEO | webapp-testing, seo, web-design-guidelines | Build, validator, generator, browser/axe/Lighthouse | npm test exit 0: 6 generator, 4 unit, 8 browser; 162 HTTP render; 18 lượt file://; Lighthouse /blog Accessibility/SEO 100 | Kiểm tra phù hợp đạt, ghi giới hạn | Đạt |
| 5. Review | ponytail-review | Diff riêng task và luồng liên quan | Root và subagent trace source/template/validator/browser, đối chiếu byte baseline; không còn Must fix/Should fix trong phạm vi | Không còn Must fix | Đạt |

## Audit có bằng chứng

Website tĩnh giới thiệu sơn và hướng dẫn tiếng Việt; kiểm tra luồng xem trang HTTP
và mở HTML trên máy. Đây là audit giới hạn lỗi ảnh, không phải audit lại toàn repo.

1. **Must fix — CSS chung trỏ sai vị trí khi mở file:** blog.html dùng
   `/assets/css/site-base.css`, Chromium resolve thành `file:///E:/assets/...` thay
   vì thư mục repo. Skip link lộ ra và font body quay về system-ui. Sửa href theo
   độ sâu, gồm cả template; nếu bỏ qua, mọi trang mở trực tiếp đều có thể gặp lỗi.
2. **Should fix — hồi quy chưa kiểm tra vị trí skip link:** test cũ chỉ kiểm tra
   href và focus trang chủ HTTP. Bổ sung kiểm tra nằm ngoài viewport trước Tab,
   trong viewport khi focus, ẩn lại và focus main sau Enter, gồm file://.

Bằng chứng trước sửa: output/skip-link/before-http.png và before-file.png.
CSS hiện có đã đúng; không cần viết thêm selector hoặc bỏ tiện ích accessibility.
Lighthouse trước sửa chạy /blog qua HTTP, báo cáo tại
output/skip-link/lighthouse-before/ (chỉ số lab, không suy diễn index/ranking).

## Kiểm thử và review cuối

- Trước sửa, test hồi quy mới thất bại đúng lỗi: 4/6 generator test fail và
  validator báo cả 54 href tuyệt đối. Không coi test chưa chạy là đạt.
- `npm test`: exit 0. HTML/context/assets/skills đạt; 54 trang, 53 indexable;
  SEO báo 0 quality issue, sitemap/robots không đổi; 6 generator trong thư mục tạm,
  4 unit, 8 browser test đạt (browser 1,7 phút).
- HTTP: 54 trang × 360/768/1440px, không overflow, ảnh và font tải đúng, skip link
  ngoài viewport mặc định, không axe serious/critical. Chi tiết
  output/browser-360.json, browser-768.json và browser-1440.json.
- File trực tiếp: 9 trang đại diện đủ nhóm × 360/1440px, chặn CDN để test độc lập
  tài nguyên ngoài; skip link ẩn → Tab là focus đầu tiên và nằm hoàn toàn trong
  viewport → Enter focus main và skip link ẩn lại. Kiểm tra không chỉ dùng
  toBeVisible vì translate ngoài viewport vẫn có thể được xem là visible.
- /blog: thêm 6 lượt kiểm tra HTTP/file:// tại 360/768/1440px với CDN hoạt động,
  xác nhận Be Vietnam Pro và thao tác Tab/Enter. Số đo trước Tab y=-81,27px,
  khi focus y=8px. Bằng chứng output/skip-link/verified.json; đã xem ảnh
  after-file-1440.png, after-file-360.png và focus-360.png.
- Lighthouse /blog qua HTTP, trước/sau: Accessibility 100/100, Best Practices
  100/100, SEO 100/100, CLS 0/0; Performance 91/90, LCP 3,18/3,37s. Hai lần chạy
  có CDN và tải máy khác nhau; không kết luận suy giảm hay cải thiện hiệu năng từ
  chênh lệch lab này. Lệnh: `node tools/lighthouse-audit.mjs --routes=/blog
  --output=output/skip-link/lighthouse-before` và tương tự lighthouse-after.
- Đối chiếu byte với output/skip-link/source-before.json: 54 HTML và ba generator
  chỉ đổi href stylesheet; nội dung/metadata khác giữ nguyên. Google verification,
  sitemap, robots nguyên byte. Không sinh lại HTML hàng loạt. `git diff --check`
  exit 0 (Git có cảnh báo LF/CRLF từ working tree hiện có).

Ponytail review: website tĩnh phục vụ người xem độc lập; thay đổi chỉ ở cách resolve
stylesheet. Root HTML dùng assets/css/site-base.css; trang một cấp dùng ../assets/;
trang hai cấp dùng ../../assets/. Route công khai và URL asset HTTP giữ đúng,
template mới sinh không làm lỗi quay lại. Đã đối chiếu hai finding audit: lỗi tải
CSS được sửa tại mọi caller, thiếu hồi quy được bổ sung bằng test fail trước sửa.
Không thêm CSS/dependency/JavaScript xử lý skip link. Verdict: Ship.

Người dùng đã xác nhận ảnh được chụp khi mở trực tiếp file HTML trên máy, đúng
trường hợp file:// đã tái hiện và sửa. Giới hạn: không kiểm tra lại mọi tương
tác/tài nguyên khác qua file://; bài test file:// tập trung stylesheet và skip link.
Không audit các thay đổi có từ trước ngoài phạm vi này; không deploy production.
