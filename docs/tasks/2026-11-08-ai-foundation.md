# Chuẩn hóa project cho quy trình AI

Mục tiêu: thực hiện kế hoạch đã duyệt; giữ URL, thiết kế và 54 trang nội dung.
Đầu vào: 54 HTML nội dung, một file xác minh, 3 generator, SEO automation hiện có.
Đọc context ở `docs/pages/README.md`; phạm vi giao diện và SEO là toàn site.

| Phase/hạng mục | Skill đã sử dụng | Đầu vào | Kết quả/bằng chứng | Điều kiện hoàn tất | Trạng thái |
|---|---|---|---|---|---|
| 1. Khảo sát | frontend-static-site, ponytail-audit, web-design-guidelines, seo-audit | HTML/CSS, generator, browser 8 trang | docs/audits/baseline.md; output/baseline | Lỗi có trường hợp tái hiện | Đạt |
| 2. Cài skill | skill-installer | các repo upstream | .agents/skills/SOURCES.md và sources.json | Nguồn/commit/giấy phép đủ | Đạt |
| 2. Tài liệu và hệ thiết kế | skill-creator, frontend-design, frontend-static-site | design hiện tại và 54 trang | AGENTS.md, AGENT.md, DESIGN.md, docs/pages | Đủ context và hướng dẫn từng phase | Đạt |
| 3. Typography/responsive | frontend-static-site, frontend-design, web-design-guidelines | CSS/HTML/template | font CDN, site-base.css, skip links | Browser/font/fallback đạt | Đạt |
| 3. Generator | frontend-static-site, ponytail | selection/head/CDN render | giới hạn Product và giữ metadata | Hồi quy generator đạt | Đạt |
| 3. Tính sơn và tư vấn | frontend-static-site, web-design-guidelines | calculate/tab/submit | email, keyboard, validation | E2E tương tác đạt | Đạt |
| 4. SEO/inventory | seo, seo-audit | canonical, sitemap, graph | read-only checks, build công khai | 53 URL, không orphan/link hỏng | Đạt |
| 4. Test/CI | webapp-testing, seo, web-design-guidelines | nguồn và bản dist | unit/generator/browser/axe/Lighthouse | Lệnh tái lập và kết quả thật | Đạt |
| 5. Review | ponytail-review, ponytail-audit, web-design-guidelines | diff, caller và tests | docs/audits/final-review.md | Hết Must fix, ghi giới hạn | Đạt |

Không deploy production. Subagent của host không khởi chạy được vì model mặc định
`my-common` không khả dụng; các kiểm tra được thực hiện trong cùng phiên và các
kiểm tra độc lập chạy song song bằng công cụ thực thi.

## Kết quả bàn giao

- npm test đạt; bổ sung test validation generator sau review: 6 generator + 4 unit
  + 6 browser tests đều đạt. 162 lượt render không tràn, font/ảnh đúng và không axe
  serious/critical. 9 skills qua quick_validate với Python UTF-8.
- Lighthouse 6 trang có Accessibility/SEO 100; trang chủ Performance 78, LCP 5,3s;
  giới hạn và phần performance cần làm tiếp ghi ở seo/seo-summary.md.
- Tối ưu packshot S68 5,5MB → 23KB, giữ nguồn PNG. Sửa thêm xử lý con số tính sơn
  vượt độ chính xác an toàn; test giữ dữ liệu email và chặn kết quả sai.
- Review Ponytail: docs/audits/final-review.md, không còn Must fix.
- Không deploy; Cloudflare auto-build cần chọn npm run build và output dist tại
  dashboard trước khi sử dụng auto deployment. CI chưa được chạy trên GitHub.
