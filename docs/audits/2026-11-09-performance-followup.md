# Tối ưu tài nguyên sau chỉnh giao diện

Website tĩnh phục vụ người xem trên mobile/desktop qua CDN. Audit tập trung
vào tài nguyên đầu trang phong thủy, nơi Lighthouse còn chậm sau redesign.
Áp dụng frontend-static-site, ponytail-audit, seo-audit, web-design-guidelines;
phương án giữ hướng frontend-design đã chọn. Không audit lại nội dung kinh doanh.

## Phát hiện và sửa

1. **Preload ảnh nền cũ tranh băng thông với nội dung hiện tại — Should fix.**
   Cả17HTML phong thủy còn preload ảnh Unsplash1920px, khoảng283KB ở mức ưu
   tiên cao. Hub đã dùng WebP local720/1200;16hero mệnh/tuổi là nội dung chữ.
   Không có CSS hay ảnh hiển thị nào dùng đúng URL preload cũ.
   Đã bỏ đúng1dòng trên mỗi trang. Template `generate_fengshui_pages.py:head`
   vốn không sinh hint này, không cần thay thuật toán hay sinh lại nội dung.
   Nếu giữ nguyên, mỗi lượt mở trang vẫn tốn request ảnh không sử dụng.

Cache production đã có Brotli, CSS cache4giờ; cảnh báo cache của Lighthouse
local không chứng minh production thiếu cache. GoogleFonts đã preconnect và
display=swap; giữ đủ font/weight theo DESIGN. Không thêm header, dependency
hoặc thay JS chỉ để thay đổi điểm lab.

## Đo trước/sau

Snapshot được chụp từ source sau redesign ở `output/performance-followup/before/`.
Lighthouse13.6 mobile, mô phỏng mạng/CPU mặc định, cùng máy và server,3lượt hub
mỗi phiên bản. Không chạy build/test browser trong các lượt đo chính.

| Hub phong thủy | Trước | Sau |
|---|---:|---:|
| Trung vị Performance |87|96|
| Trung vị LCP |3,848giây|2,401giây|
| Khoảng LCP của3lượt |3,811–3,966giây|2,384–2,534giây|
| CLS của3lượt |0|0|
| Accessibility / Best Practices / SEO |100/100/100|100/100/100|

LCP trung vị giảm37,6%. Tuổi1998 một cặp đo cho97điểm cảtrước/sau,
LCP2,169→2,149giây; chênh lệch nhỏ này chưa cho thấy cải thiện LCP có ý nghĩa
trên route đó. Lợi ích chắc chắn của cả17trang là không còn tải ảnh cũ.

Nguồn số liệu: `measurement-summary.json`, `lighthouse-before*/`,
`lighthouse-after*/`; thử nghiệm độc lập tại `analysis-agent/`. Không dùng
thử nghiệm font bị lỗi stylesheet làm bằng chứng tối ưu.

## Kiểm tra và review

- `source-preservation.json`:17HTML mỗi trang chỉ bỏ preload. Tất cả file
  công khai khác, title/meta/canonical/schema/URL/hình hiển thị giữ nguyên byte.
- `final-review.md`, `review-diff.json`: review độc lập theo ponytail-review,
  không có Must fix/Should fix còn lại trong thay đổi này.
- `visual-check.json`: hub, mệnh Kim và tuổi 1998 tại 360/768/1440px có 9/9
  layout và ảnh chụp giống hệt trước/sau; ảnh hiển thị và menu mobile đạt;
  các trang sau tối ưu không request URL ảnh cũ.
- `npm-test.txt`: `npm test` exit 0. Site/SEO, 7 generator, 4 unit và 22 browser
  test đạt, bao gồm ma trận 54 trang × 3 viewport, ảnh S68 HTTP/file, fallback
  font, bàn phím và tính sơn. Generator được kiểm tra trong thư mục tạm.
- Build tạo 98 file công khai trong `dist`; không thay server để tăng điểm đo.

Verdict: đã giải quyết tải thừa, kiểm tra và review đạt.
Lean: giảm17dòng, không thêm dependency hay logic runtime.

Chưa kiểm tra Safari/Firefox, thiết bị thật, Core Web Vitals thực địa hoặc
Search Console. Source hiện tại chưa commit/push/deploy trong đợt này.
Production đang là bản cũ; sau lần deploy tới cần kiểm tra MIME và decode của
ảnh local mới, vì asset chưa tồn tại có thể trả HTMLfallback với status200.
