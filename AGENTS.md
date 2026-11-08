# Hướng dẫn làm việc với Sago Paint

Website tĩnh HTML/CSS, Bootstrap 5; nội dung tiếng Việt. Đọc `DESIGN.md`,
`docs/pages/README.md` và `CONTEXT.md` của các trang bị ảnh hưởng trước khi sửa.
`AGENT.md` là lối vào tương thích; file này là nguồn hướng dẫn chính.

## Quy trình cho mọi task

Tạo bản ghi từ `docs/tasks/TEMPLATE.md`. Task nhỏ vẫn ghi đủ các phase, ngắn gọn.
Mỗi phase và hạng mục ghi skill thực sự đọc/sử dụng, đầu vào, kết quả, bằng chứng
kiểm tra và điều kiện hoàn tất. Không đánh dấu kiểm tra chưa chạy là đã đạt.

1. **Khảo sát:** `frontend-static-site`, `ponytail-audit`; thêm `seo-audit` và
   `web-design-guidelines` cho nội dung/giao diện. Đọc luồng liên quan, xác nhận lỗi.
2. **Phương án:** `frontend-static-site`, `frontend-design` cho giao diện;
   `skill-creator` khi sửa skill. Chốt phạm vi, test, tác động SEO.
3. **Thực hiện:** dùng skill phù hợp từng hạng mục: `frontend-static-site` cho
   HTML/CSS, `frontend-design` cho typography/thành phần, `seo` cho SEO kỹ thuật.
4. **Kiểm thử/SEO:** `webapp-testing`, `seo`, `web-design-guidelines`. Chạy test
   phù hợp; CSS chung cần kiểm tra mọi nhóm trang. Cập nhật context nếu hành vi đổi.
5. **Review:** bắt buộc `ponytail-review`, đối chiếu kết quả audit; sửa hết Must fix.
   Báo rõ kết quả, phần chưa kiểm tra và rủi ro thực tế còn lại.

Skill của project ở `.agents/skills/<tên>/SKILL.md`; ưu tiên đúng đường dẫn này
nếu máy có skill trùng tên. Dùng `skill-installer`/`skill-creator` của host khi
cài hoặc sửa skill. Nguồn, commit và giấy phép ở `.agents/skills/SOURCES.md`.
Ponytail audit/review là quy trình đọc và phân tích của agent, không phải lệnh
CLI hay công cụ đảm bảo tự động bắt mọi lỗi. Phải lưu kết quả có bằng chứng.

## Bất biến và nguồn chỉnh sửa

- Giữ URL công khai: root HTML có canonical bỏ `.html`; thư mục giữ dấu `/`.
- Giữ nguyên file `google*.html`; trang ANAclean `-2` vẫn `noindex, follow`
  và canonical về bản chính. Không thay thông tin doanh nghiệp/sản phẩm thiếu nguồn.
- Font duy nhất cho chữ hiển thị: Be Vietnam Pro qua Google Fonts, fallback Arial.
- Sửa cả template khi thay hành vi sinh trang. `refresh_pages.py` chỉ xử lý trang
  có Product schema, không suy đoán mọi HTML là sản phẩm. Test generator trong
  thư mục tạm trước; không chạy sinh hàng loạt chỉ để thay font.
- `tools/site-files.js` định nghĩa vùng công khai. Thêm nhóm route mới phải cập
  nhật inventory, context và test. `dist` là đầu ra deploy; không deploy repo gốc.
- Giữ stack tĩnh; dependency mới cho test nằm ở devDependencies.

## Lệnh kiểm tra

Node.js 24+ và Python 3.12+; `npm ci`, `npx playwright install chromium`.

- `npm run check:site`: HTML, tài nguyên/liên kết, context và skill.
- `npm run check:seo`: audit chỉ đọc, exit code khác 0 khi thất bại.
- `npm run test:generators`: hồi quy generator trong thư mục tạm.
- `npm run test:unit`: inventory, server và đóng gói.
- `npm run test:e2e`: build rồi kiểm tra Chromium ở 360/768/1440px.
- `npm test`: toàn bộ các kiểm tra trên.
- `npm run audit:lighthouse`: báo cáo lab của trang đại diện, lưu `output/`.
- `npm run build`: tạo `dist`; `npm run serve`: xem bản đóng gói ở localhost.

Chỉ chạy deploy khi task có yêu cầu. Chất lượng lab không chứng minh Google đã
lập chỉ mục hoặc Core Web Vitals thực tế đạt; không tự tạo thông tin Search Console.
