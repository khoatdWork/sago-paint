# Sửa ảnh SAGO S 68 PRO và làm gọn trang chủ

Mục tiêu: ảnh sản phẩm hiển thị qua HTTP và file trực tiếp, gồm mobile; giảm rối
thị giác bằng thứ bậc rõ. Phạm vi: index.html, browser test và context trang chủ.
Đã đọc AGENTS.md, DESIGN.md, docs/pages/README.md, docs/pages/home/CONTEXT.md.
Giữ stack, font, URL, metadata và dữ liệu doanh nghiệp/sản phẩm hiện có.

| Phase/hạng mục | Skill đã sử dụng | Đầu vào | Kết quả/bằng chứng | Điều kiện hoàn tất | Trạng thái |
|---|---|---|---|---|---|
| 1. Khảo sát | frontend-static-site, ponytail, ponytail-audit, seo-audit, web-design-guidelines | HTML/CSS, asset, build/test, context | Browser xác nhận ảnh ẩn ở 360, tràn hero ở 768 và sai src khi file://; regression trước sửa 5 fail/1 pass | Tái hiện bằng browser | Đạt |
| 2. Phương án | frontend-static-site, frontend-design, ponytail | Findings audit và DESIGN.md | Hero S68 tĩnh; ba danh mục dễ so sánh; hai công cụ gọn; cẩm nang giảm nhãn/trang trí | Chốt phạm vi/test/SEO | Đạt |
| 3. Thực hiện: ảnh/bố cục/context | frontend-static-site, frontend-design, ponytail | index.html, ảnh hiện có và context | Hero tĩnh, asset crop trong suốt 419×447/26KB, src tương đối; ba danh mục, hai công cụ, ba bài ảnh/ba link phụ; menu collapse dưới 1200; context cập nhật | Ảnh hiện mọi breakpoint; không sửa CSS chung; giữ links/SEO | Đạt |
| 4. Kiểm thử/SEO | webapp-testing, seo, web-design-guidelines | Build và browser | npm test exit 0: 6 generator, 4 unit, 14 browser; targeted cuối 7 pass; screenshots/axe/fallback; Lighthouse trước/sau | 360/768/1440, file://, keyboard, fallback, axe, suite, Lighthouse trước/sau | Đạt |
| 5. Review | ponytail-review | Diff riêng task và luồng liên quan | Root và subagent review HTML/asset/test/build; mọi finding audit đã xử lý; metadata/schema/tập href giữ nguyên | Không còn Must fix; đối chiếu audit | Đạt |

## Audit và phương án

Website tĩnh, khách xem độc lập, không có dữ liệu ghi từ trang chủ. Audit chỉ tập
trung luồng xem trang chủ và đi tới sản phẩm/công cụ/bài viết, không audit toàn repo.

1. Must fix: @media(max-width:575.98px) đặt hero-product-panel display:none;
   src /assets/products/sago-s68-pro-preview.webp resolve sai khi mở file://.
   Asset có thật, 22.770 byte. Ở 768px ảnh còn tràn đáy hero 42px do caption absolute
   và chiều cao banner cố định. Sửa src tương đối và layout flow để ảnh luôn hiện.
2. Should fix: browser test chỉ kiểm tra ảnh decode, không kiểm tra ảnh hiển thị.
   Bổ sung hồi quy visible, kích thước và decode cho HTTP/file:// ở ba chiều rộng.
3. Should fix: ba slide danh mục lặp section danh mục; badge/eyebrow/headline
   cùng ý, nhiều background gradient, shadow và hover chuyển động. Bỏ carousel,
   giữ một hero sản phẩm và các link danh mục; bỏ nhãn/trang trí trùng.

Phương án frontend-design: màu #ffffff (nền), #fff4f1 (đệm nhẹ), #202428 (chữ),
#626b74 (chữ phụ), #d45141 (nhận diện), #a83c31 (CTA). Chữ Be Vietnam Pro kế thừa
site-base; heading 700–800, body 400. Hero ảnh thùng sơn thật trên nền nhẹ,
chữ trái/ảnh phải ở desktop, ảnh dưới chữ ở mobile; không phủ chữ lên ảnh.

Luồng: [Hero S68: nội dung | ảnh] → [Nội thất | Ngoại thất | Chống thấm]
→ [Tính sơn | Chọn màu phong thủy] → [Cẩm nang] → [Liên hệ].

Đối chiếu brief: giữ màu/font/ảnh thương hiệu; điểm nhấn duy nhất là S68.
Không thêm nhãn hoa, số thứ tự trang trí, gradient hoặc card lồng card.
Giữ liên kết bài viết và nhóm phong thủy; title/description/canonical/robots/schema
không đổi. Trang chủ biên tập trực tiếp, không có generator cần sửa.

## Bằng chứng kiểm tra và review

Baseline source: output/home-cleanup/index-before.html và
output/home-cleanup/site-spec-before.cjs. Các kết quả sau là lệnh đã chạy:

- Browser trước sửa: output/home-cleanup/before.json và before-{http,file}-{width}.png.
  HTTP360 ảnh loaded nhưng box 0×0; file:// resolve về E:/assets, naturalWidth=0.
  Regression trước sửa 5 fail/1 pass, lưu regression-before.txt/.json.
- `npm test`: exit 0, 6 generator trong thư mục tạm, 4 unit, 14 browser test (1,9 phút).
  Log: output/home-cleanup/npm-test.txt. Kiểm tra 54 trang × 360/768/1440px:
  không tràn ngang, ảnh decode, font áp dụng, không axe serious/critical.
  Bài test file:// skip link đủ nhóm trang vẫn đạt.
- Hồi quy ảnh mới: HTTP/file:// × 360/768/1440px, ảnh visible, decode, kích thước
  ≥160×140px và nằm trong hero. Ảnh thực tế 224×239 / 280×299 / 360×384px.
  Tài nguyên local đóng gói trong dist; ảnh mới chỉ crop khoảng alpha từ preview
  hiện có bằng canvas, không thay nhãn hoặc dùng ảnh tạo sinh. Asset dùng chung cũ
  giữ nguyên để không ảnh hưởng trang khác.
- `node output/home-cleanup/verify-home.cjs`: cả HTTP/file tại ba chiều rộng
  không ảnh lỗi và không overflow; chặn Google Fonts vẫn đọc được qua fallback,
  CTA nhận focus và không bị header che. Focus button dùng box-shadow 4px
  rgba(49,132,253,.5) của Bootstrap; xem keyboard-focus.png.
- Đã xem trực tiếp ảnh full page desktop, hero 360/768/1440 và focus mobile.
  Sau sửa, trang desktop cao 2873px so với 6836px trước; 360px còn 5528px so với
  9516px. Tập đích href giữ nguyên, gồm sáu bài viết và năm mệnh phong thủy.
- Kiểm tra thêm 320/576/767/992/1024/1200px phát hiện header menu ngang ở 992/1024
  wrap thành 88px. Đã đồng bộ navbar/align/CTA sang breakpoint xl để menu thu gọn
  dưới 1200. Kiểm lại chín chiều rộng 320–1440: không overflow, header một hàng;
  menu mở được ở 1024. Bằng chứng output/home-cleanup/breakpoints.json.
- Sau chỉnh header, `npx playwright test --grep 'home S68|navigation, skip'`
  đạt 7/7; log targeted-final.txt. CSS chung không thay đổi; không chạy lại toàn
  suite sau thay đổi chỉ ở breakpoint header này vì kiểm tra liên quan đã đạt.
- `node tools/lighthouse-audit.mjs --routes=/ --output=output/home-cleanup/lighthouse-before`
  và tương tự lighthouse-after: Performance 76→96, LCP 5,23→2,39s, CLS 0→0;
  Accessibility/Best Practices/SEO đều 100→100. Đây là hai lượt lab trên máy,
  CDN/tải máy có thể khác; không cam kết Core Web Vitals hoặc thứ hạng Google.
- `check:site`, `check:seo` đạt: 54 trang nội dung, 53 indexable, 0 quality issue;
  sitemap/robots nguyên trạng. Metadata/canonical/JSON-LD và tập đích href đối
  chiếu byte/nội dung không đổi; output/home-cleanup/diff-review.json.
  HTML giảm 1320→373 dòng, 51.627→23.551 byte. `git diff --check` exit 0;
  Git có cảnh báo LF/CRLF từ thay đổi có trước.

Review Ponytail: thay đổi chỉ ở trang chủ, một asset và kiểm thử/context. Luồng xem
sản phẩm/danh mục/công cụ/cẩm nang/liên hệ còn đủ. Ảnh dùng flow grid, giữ tỷ lệ;
không còn display:none hoặc root src; regression bắt được lỗi cũ. Đã xử lý cả
ba finding audit, thêm lazy ảnh danh mục và xóa CSS carousel/visual không còn dùng.
Subagent độc lập kiểm tra cả build inventory và test, không phát hiện Must fix
hoặc Should fix mới. Verdict: Ship.

Giới hạn: đã kiểm Chromium, chưa kiểm Safari/Firefox hay thiết bị thật; font,
Bootstrap, logo và ảnh nội dung khác vẫn cần CDN. Không audit thay đổi tồn tại
sẵn ngoài phạm vi trang chủ. Không có dữ liệu Search Console và không deploy.
