# Nguồn skills của project

Cài bằng skill-installer từ commit đã kiểm tra; không cài plugin toàn máy hoặc hooks.
Đọc đúng đường dẫn repo nếu máy có skill trùng tên; có thể chọn skills mới từ lượt tiếp theo.

| Skill | Nguồn ghim | Giấy phép |
|---|---|---|
| ponytail | [96608e078b2d](https://github.com/DietrichGebert/ponytail/tree/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail) | [LICENSE](ponytail/LICENSE) |
| ponytail-audit | [96608e078b2d](https://github.com/DietrichGebert/ponytail/tree/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-audit) | [LICENSE](ponytail-audit/LICENSE) |
| ponytail-review | [96608e078b2d](https://github.com/DietrichGebert/ponytail/tree/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-review) | [LICENSE](ponytail-review/LICENSE) |
| frontend-design | [2c5958ecac7c](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/frontend-design) | [LICENSE.txt](frontend-design/LICENSE.txt) |
| webapp-testing | [2c5958ecac7c](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/webapp-testing) | [LICENSE.txt](webapp-testing/LICENSE.txt) |
| seo | [afa8da942115](https://github.com/addyosmani/web-quality-skills/tree/afa8da942115f2961fdbfa80807ea0b232ff6c00/skills/seo) | [LICENSE](seo/LICENSE) |
| seo-audit | [96798cf38736](https://github.com/coreyhaines31/marketingskills/tree/96798cf38736ecdba015a1d2b0521b0c8f8f41dd/skills/seo-audit) | [LICENSE](seo-audit/LICENSE) |
| web-design-guidelines | [434b7f913646](https://github.com/vercel-labs/web-interface-guidelines/blob/434b7f91364665f2f733b310ec54809bf8f37937/command.md) | [LICENSE](web-design-guidelines/LICENSE) |
| frontend-static-site | [5c2bda6-proj](https://github.com/khoatdWork/sago-paint) | [LICENSE](frontend-static-site/LICENSE) |

Wrapper web-design-guidelines trong vercel-labs/agent-skills không kèm giấy phép tại commit kiểm tra.
Vì vậy dùng trực tiếp bộ quy tắc chính thức từ vercel-labs/web-interface-guidelines có MIT LICENSE, thêm name vào frontmatter để Codex nhận diện.
Giữ nguyên nội dung upstream còn lại. Quy tắc riêng nằm ở frontend-static-site và AGENTS.md.
Khi nâng phiên bản: đọc diff upstream, cập nhật giấy phép/commit trong sources.json và chạy kiểm tra.
Các skill SEO có thể dẫn sang skill chưa cài; chỉ áp dụng nhánh phù hợp, không coi skill liên quan là đã sẵn có.

Tương thích Codex: argument-hint của Ponytail và guidelines chuyển vào metadata.argument_hint; giữ nguyên nội dung quy tắc.
