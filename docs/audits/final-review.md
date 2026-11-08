# Ponytail review — 08/11/2026

What this change does: Chuẩn hóa typography, tài liệu và quy trình AI cho 54 trang
Sago Paint; sửa các lỗi generator, responsive và tư vấn đã xác nhận. Thêm kiểm tra
lặp lại được và chỉ đóng gói tài nguyên công khai. Giả định tải: nội dung tĩnh qua
CDN, tính sơn trong browser; generator chạy bởi người bảo trì.

## Cách review

Đọc và áp dụng .agents/skills/ponytail-review/SKILL.md và ponytail-audit/SKILL.md,
nguồn DietrichGebert/ponytail commit 96608e078b2d5ea607c5c3b8b5a54d1c1fba6846.
Đối chiếu Web Interface Guidelines Vercel, frontend-static-site và seo. Review diff
và trace các caller: discovery → SEO → build → deploy; generator → head/body;
form → validation → mailto; tab → mode → calculate → UI.
Ponytail được áp dụng bằng skill, không có CLI audit giả lập hoặc plugin toàn máy.

## Must fix

Không còn finding Must fix trong phạm vi đã kiểm tra. Những lỗi đã sửa và retest:

| Vấn đề | Cách sửa và bằng chứng |
|---|---|
| Refresh ghi đè HTML không phải sản phẩm | Nhận diện Product JSON-LD; blog/file Google giữ nguyên byte trong fixture |
| Metadata/noindex bị reset | Giữ head gốc; xác thực mọi head trước lần ghi đầu tiên; test head thiếu không ghi một file nào |
| Template sinh lại font cũ/URL ảnh sai | Google Fonts + site-base + skip links trong cả 3 generator; test depth 1/2 |
| Ảnh mất kích thước khi regenerate | Mang width/height từ nguồn, gắn kích thước logo; test mọi img render |
| Tràn mobile blog và phong thủy | Sửa min-width/flex/image, gutter mobile và email footer; 162 lượt không tràn |
| Tab không dùng được bằng bàn phím | Roving tabindex, ArrowLeft/Right/Home/End, hidden panel; E2E đạt |
| Form xóa dữ liệu chưa gửi | Soạn mailto được encode; CDP kiểm tra dữ liệu, không reset, có nút gọi |
| Số rất lớn sinh Infinity trong báo giá | Chặn kết quả ngoài số nguyên an toàn, thông báo và không cho ghép email sai; E2E đạt |
| SEO check luôn thành công/scan file nội bộ | Inventory công khai chung; --check chỉ đọc và exit 1; test không ghi/không deploy |
| Sync SEO mất khả năng sửa canonical | Chỉ check chặn trước; sync sửa rồi audit lại; fixture canonical sai được sửa |
| Deploy cả repo | Build dist theo allowlist; test loại docs/skills/tests/node_modules và file stale |
| Sai accessible name/tương phản | Bỏ aria-label thừa trên link có text; màu chữ/nút đủ tương phản; axe không serious/critical |
| Ảnh hero quá lớn | WebP 23KB từ nguồn có sẵn, giữ ảnh gốc, ưu tiên hero và lazy slide ẩn |

## Should fix

1. **Tải lần đầu trên mobile vẫn còn chậm** (`index.html`, tài nguyên bên ngoài).
   - What this is: trang chủ dùng ảnh công trình, Bootstrap và Google Fonts từ CDN.
   - Problem: LCP lab cuối khoảng 5,3s; blog khoảng 3,2s. Một lượt lab không chứng
     minh field metrics nhưng cho thấy còn dư địa tải ảnh/CSS/cache.
   - Fix: mở đợt tối ưu performance có budget và baseline nhiều lần; ảnh responsive,
     tối ưu critical CSS/cache theo CDN hiện có, giữ lựa chọn Google Fonts của chủ dự án.
   - If we skip it: trang vẫn hoạt động, nhưng người dùng mạng chậm có thể chờ lâu
     trước khi nội dung đầu trang hoàn thiện. Không cam kết CWV đạt từ đợt này.

## Kết quả và giới hạn

6 generator tests, 4 unit tests và 6 browser tests đạt. Browser kiểm tra 54 trang
ở 3 viewport; 9 skill qua validator Codex (Python UTF-8). check:site/check:seo và
build đạt; file xác minh nguyên byte, canonical/robots theo baseline, 53 sitemap URL.
Lighthouse 6 trang đại diện có Accessibility/SEO 100; xem seo/seo-summary.md cho
Performance/CLS và điều kiện đo. Đã xem screenshot desktop/mobile; không thay palette
hoặc bố cục tổng thể. Git diff --check đạt.

Verdict: Ship trong phạm vi kế hoạch đã duyệt; chưa deploy production. Cải thiện
performance nêu trên là hạng mục tiếp theo, không được trình bày là đã giải quyết hết.
Not checked: GitHub-hosted CI, Cloudflare dashboard/production, GSC, thứ hạng, traffic,
rich results của Google và Core Web Vitals thực tế. Local Chromium không thay thế
kiểm tra thiết bị thật. Không gửi email hay dữ liệu khách hàng trong test.
