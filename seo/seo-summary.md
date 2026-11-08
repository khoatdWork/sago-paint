# SEO và chất lượng — 08/11/2026

Kết quả hiện tại bao phủ **54 trang nội dung**, **53 URL indexable** và một file
xác minh Google giữ nguyên SHA-256 theo baseline đã duyệt. Có 54 CONTEXT.md riêng.
Đợt kiểm tra này thay thế phạm vi 41 trang trong báo cáo cũ; các file báo cáo khác
trong thư mục seo/ là lịch sử, không phải bằng chứng kiểm tra của phiên bản này.

## Kết quả xác minh

| Kiểm tra | Kết quả |
|---|---|
| HTML/context/nguồn và giấy phép skills | Đạt; 54 trang, 9 skills |
| Canonical/robots | Giữ đúng baseline từng trang; alias ANAclean -2 vẫn noindex |
| Sitemap | Đúng 53 URL canonical indexable; lastmod được đồng bộ |
| Title/description/H1/JSON-LD | Đủ, parse hợp lệ; title/description indexable không trùng |
| Liên kết nội bộ/tài nguyên local | Không hỏng; không còn trang indexable thiếu inbound link |
| Font trên browser | Be Vietnam Pro tải và áp dụng cho body/heading, đủ dấu tiếng Việt |
| 360/768/1440px | 162 lượt kiểm tra trang, không tràn ngang, không ảnh hỏng |
| Axe WCAG A/AA/2.1 | Không có lỗi serious/critical ở 162 lượt render |
| Generator hồi quy | 6 tests đạt trong thư mục tạm |
| Unit đóng gói/server/SEO | 4 tests đạt |
| E2E | 6 tests đạt; 3 test bao phủ toàn site, 3 test tương tác |
| Menu/carousel/keyboard/skip link | Đạt, có smoke test font CDN bị chặn và reduced motion |
| Tính sơn | 100m²/2 lớp → 20L, 2 thùng; zero, làm tròn, preset và số quá lớn được kiểm tra |
| Tư vấn | CDP xác nhận mailto chứa tên/điện thoại/kết quả; form giữ dữ liệu; không gửi email trong test |
| Build | 93 file công khai; docs/skills/tests/dependencies không có trong dist |

## Lighthouse mobile tại localhost

| Trang | Performance trước → sau | Accessibility trước → sau | SEO sau | LCP trước → sau | CLS sau |
|---|---|---|---|---|---|
| `/` | 70 → 78 | 96 → 100 | 100 | 10.47 → 5.29s | 0.000 |
| `/son-noi-that` | 97 → 98 | 95 → 100 | 100 | 2.16 → 1.86s | 0.019 |
| `/blog` | 94 → 90 | 98 → 100 | 100 | 2.75 → 3.25s | 0.022 |
| `/son-nha-moi-xay` | 95 → 97 | 95 → 100 | 100 | 2.65 → 2.15s | 0.000 |
| `/phong-thuy-son-nha/` | 94 → 95 | 100 → 100 | 100 | 2.23 → 2.18s | 0.074 |
| `/tinh-son/` | 95 → 96 | 97 → 100 | 100 | 2.37 → 2.21s | 0.008 |

Lighthouse 13.6.0, Chromium của Playwright 1.65.0, mobile simulated throttling.
Đây là các lần đo lab, phụ thuộc CPU, cache, mạng tới CDN và tài nguyên bên ngoài;
không phải median nhiều lần hoặc dữ liệu người dùng thực tế. Trang chủ và tính sơn
được đo lại sau thay đổi cuối; các trang khác dùng lượt đầy đủ ngay trước đó.
Không diễn giải chênh lệch nhỏ thành cải thiện hay suy giảm chắc chắn.

Ảnh packshot S68 trên giao diện dùng WebP 860px khoảng 22.770 byte thay cho PNG gốc
5.492.609 byte. Giữ ảnh gốc và URL social image; ưu tiên ảnh hero, lazy-load slide ẩn.
Carousel chuyển slide bằng thao tác người dùng, không tự chạy.

## Còn cần cải thiện

Trang chủ vẫn có LCP lab khoảng 5,3s; blog khoảng 3,2s. Ảnh bên ngoài, CSS Bootstrap/
Google Fonts và cache là các mục Lighthouse còn chỉ ra. Cần một đợt performance
riêng để xác định ngân sách tải, tối ưu ảnh theo viewport/critical CSS và đo lặp
trong điều kiện kiểm soát. Chưa thể kết luận Core Web Vitals thực tế đạt.

## Tái kiểm tra và bằng chứng

- `npm test`; `npm run audit:lighthouse`; `npm run build`.
- Browser chi tiết: output/browser-360.json, browser-768.json, browser-1440.json.
- Ảnh trước/sau: output/baseline và output/screenshots.
- Báo cáo Lighthouse: output/baseline/lighthouse, output/lighthouse,
  output/lighthouse-final-touched. Artifact được gitignore; CI tải lên khi chạy.
- Audit/review Ponytail: docs/audits/baseline.md và docs/audits/final-review.md.
- Nguồn skill: .agents/skills/SOURCES.md và sources.json.

Chưa kiểm tra: Search Console, traffic, thứ hạng, rich-result eligibility bằng Google,
Core Web Vitals field, HTTP production và CI trên GitHub. Chưa deploy production.
