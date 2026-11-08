# Kiểm tra cảnh báo --font-sans

Phạm vi: typography chung của 54 trang, ba stylesheet riêng và CSS inline trang
chủ. Đã đọc DESIGN.md và context của trang chủ, danh mục, blog, sản phẩm, phong
thủy, tính sơn. Giữ font, bố cục và metadata hiện tại.

| Phase/hạng mục | Skill đã sử dụng | Đầu vào | Kết quả/bằng chứng | Điều kiện hoàn tất | Trạng thái |
|---|---|---|---|---|---|
| 1. Khảo sát | frontend-static-site, ponytail-audit | Báo cáo người dùng; toàn bộ tham chiếu font | Biến được khai báo trong site-base.css; 17 khai báo lặp lại ở file khác; test trước chỉ xét body/H1 | Phân biệt kiểm tra runtime với cảnh báo editor | Đạt |
| 2. Phương án | frontend-static-site, frontend-design, ponytail | Cascade CSS, template và context | Bỏ khai báo font lặp lại; kế thừa từ typography chung; bổ sung kiểm tra computed font cho chữ/control | Một nguồn điều khiển typography, không thêm dependency | Đạt |
| 3. Thực hiện | frontend-static-site, ponytail | 3 CSS và index.html | Bỏ 17 khai báo font trùng lặp; DESIGN.md ghi nguồn typography duy nhất | Không còn tham chiếu font-sans ngoài file khai báo | Đạt |
| 4. Kiểm thử/SEO | webapp-testing, seo, web-design-guidelines | 54 trang, 3 viewport, test và metadata | npm test đạt: 6 generator, 4 unit, 6 browser; chi tiết bên dưới | Font token có giá trị; chữ/control đúng font; không tràn; kiểm tra SEO đạt | Đạt |
| 5. Review | ponytail-review | Diff và luồng CSS → browser | Trace font từ root/Bootstrap tới chữ/control; không còn Must fix trong phạm vi sửa | Không còn Must fix; báo rõ giới hạn | Đạt |

Không khẳng định đã tái hiện cảnh báo trong editor khi chưa biết ứng dụng/file
người dùng đang mở. Subagent độc lập không khởi chạy được do model mặc định
`my-common` không khả dụng; review thực hiện tại phiên này.

## Bằng chứng sau sửa

- `npm test`: exit 0; 54 trang và 53 URL indexable, sitemap/robots/head không đổi.
- 162 lượt render: --font-sans có giá trị; Be Vietnam Pro tải thực tế;
  không có phần tử chữ/control sai font, không tràn, không axe serious/critical.
- Test bổ sung đọc computed style của root token và mọi phần tử chứa text trực
  tiếp/control; không còn chỉ kiểm tra body/H1. Bằng chứng ở output/browser-*.json.
- Tìm toàn bộ CSS/HTML/template: chỉ assets/css/site-base.css còn tham chiếu biến
  --font-sans, cùng nơi khai báo :root. Không thêm định nghĩa font trùng, import
  CSS hay cấu hình tắt cảnh báo editor. Không cần đổi template vì chúng chỉ liên
  kết stylesheet, không chứa khai báo font bị lặp lại này.
- `git diff --check`: đạt. Không đổi nội dung/context trang vì hành vi và tài nguyên
  không đổi; DESIGN.md bổ sung quy ước kế thừa typography.

## Ponytail review

Thay đổi gom typography về file chung đã được liên kết ở cả 54 trang, xóa các
khai báo lặp lại ở styles.css, category-pages.css, phong-thuy-son-nha/styles.css
và index.html. Giả định chạy website qua HTTP như luồng serve/build/deploy hiện có.

Trace: --font-sans ở :root → biến Bootstrap/body/heading/control trong site-base.css
→ kế thừa tới navigation/card/text. Các selector bị xóa chỉ lặp lại cùng font;
font-size, weight, spacing và metadata giữ nguyên. Generator dùng các stylesheet
này và không cần thay template. Browser/SEO/generator/unit kiểm tra lại đều đạt.

Không còn Must fix trong phạm vi thay đổi này. Chưa kiểm tra diagnostic trong đúng
editor/DevTools của người dùng vì chưa có file/URL hoặc tên ứng dụng; không tuyên
bố đã tái hiện hoặc xác nhận biến mất cảnh báo trên máy người dùng. Không đo lại
Lighthouse vì không đổi font tải hoặc bố cục; không deploy production.
