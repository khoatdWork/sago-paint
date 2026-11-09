# SEO và kiểm tra chất lượng Sago Paint

## Chuẩn bị

Dùng Node.js 24+ và Python 3.12+. Cài công cụ phát triển bằng `npm ci`, rồi
`npx playwright install chromium`. Trên CI Linux dùng `--with-deps`.
Site vẫn là HTML/CSS/Bootstrap tĩnh; không có dependency production mới.

## Kiểm tra trước khi hoàn tất task

- `npm run check:site`: parse 54 trang nội dung; kiểm tra title, description,
  canonical/robots theo baseline, schema JSON, liên kết/ảnh nội bộ, orphan,
  54 context, nguồn và giấy phép skills. Có lỗi trả exit code 1.
- `npm run check:seo`: **chỉ đọc**, kiểm tra metadata, canonical, sitemap và
  robots; không sửa HTML. Không thể kết hợp `--check` với `--deploy`.
- `npm run test:generators`: chạy hồi quy trong thư mục tạm, không sinh đè trang thật.
- `npm run test:unit`: inventory, bản public, route/redirect và chế độ SEO chỉ đọc.
- `npm run test:e2e`: build rồi kiểm tra 54 trang ở 360/768/1440px, font tải thật,
  ảnh, overflow, axe serious/critical, menu, hero S68, calculator và soạn email.
- `npm test`: chạy tất cả các kiểm tra trên.
- `npm run audit:lighthouse`: báo cáo lab cho 6 trang đại diện. Lỗi chạy audit
  trả mã thất bại; điểm số dùng để so sánh và chẩn đoán, không bảo đảm thứ hạng.

Browser report, screenshots, traces và Lighthouse lưu trong `output/`,
`playwright-report/`, `test-results/`; các thư mục này được gitignore.
CI chạy trên push/PR và tải báo cáo lên artifact, không tự deploy.

## Đồng bộ SEO và xuất bản

`node tools/seo-sync.js --dry-run` xem trước, không ghi. Lệnh
`node tools/seo-sync.js` đồng bộ canonical, og:url, favicon, sitemap và robots.
`lastmod` ở chế độ sync lấy từ thời gian sửa file; chế độ check so sánh tập URL,
không yêu cầu timestamp checkout/CI trùng máy phát triển.

Sitemap có 53 URL canonical indexable, bỏ file xác minh Google và trang
ANAclean `-2` đang noindex. Không áp đặt số từ tối thiểu như điều kiện SEO đạt:
độ hữu ích và ý định tìm kiếm được review bằng skill seo-audit.

`404.html` được đóng gói để Cloudflare Pages trả mã 404 cho URL không tồn tại,
không thuộc inventory 54 trang nội dung hoặc sitemap. Local server cũng trả
trang lỗi với GET/HEAD; sau deploy phải kiểm tra mã HTTP cho cả URL trang và
asset không tồn tại, vì nhìn thấy trang lỗi chưa đủ xác nhận mã phản hồi đúng.

`npm run build` chỉ đóng gói các file công khai vào `dist` theo inventory
`tools/site-files.js`; docs, skills, tests và node_modules không được xuất bản.
`npm run serve` phục vụ dist ở http://127.0.0.1:4173, có URL không đuôi .html
và redirect hiện có để kiểm tra tại máy.

Chỉ khi task yêu cầu deploy mới chạy:

```sh
node tools/seo-sync.js --deploy
node tools/seo-sync.js --check --check-live
```

Khi release commit đã đồng bộ SEO và kiểm thử, giữ nguyên nguồn bằng cách build
rồi deploy trực tiếp, không chạy sync ghi lại lastmod sau commit:

```sh
npm run build
npx wrangler pages deploy dist --project-name sagopaint --branch main
node tools/seo-sync.js --check --check-live
```

Deploy dùng `wrangler pages deploy dist --project-name sagopaint`, không dùng
thư mục repo gốc. Nếu Cloudflare Pages còn cấu hình auto build cũ ở dashboard,
cần đổi build command thành `npm run build`, output directory thành `dist`
trước lần auto deploy tiếp theo. Cấu hình dashboard chưa được thay trong đợt này.

## Thêm hoặc đổi trang

1. Sửa nguồn/template và HTML, giữ lang vi, Be Vietnam Pro, skip link và metadata.
2. Nhóm thư mục route mới cần được khai báo trong PUBLIC_DIRS của site-files.js.
3. Đổi URL cần redirect; không bỏ trạng thái noindex của alias nếu chưa có quyết định.
4. Cập nhật baseline `tests/page-contracts.json` khi có thay đổi URL/index được duyệt.
5. Chạy `python tools/update_contexts.py`, đọc diff từng context và cập nhật số
   trang kỳ vọng trong checks/tests khi thêm hoặc bỏ trang có chủ ý.
6. Sync SEO, chạy test và Ponytail review theo AGENTS.md.

## Phạm vi báo cáo

Báo cáo hiện tại là `seo/seo-summary.md` và `docs/audits/final-review.md`.
Các báo cáo còn lại trong seo/ là tài liệu lịch sử của đợt audit trước, có thể chỉ
bao phủ 41 trang. Không dùng điểm 100/100 cũ làm bằng chứng cho lần kiểm tra mới.

Chưa kiểm tra Search Console, traffic, index Google hoặc Core Web Vitals thực tế.
Không cần Indexing API cho trang sản phẩm sơn. Sau deploy được duyệt mới kiểm tra
HTTP live và gửi sitemap trong Search Console nếu người quản trị có quyền.
