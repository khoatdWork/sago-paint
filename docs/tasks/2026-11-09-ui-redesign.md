# Làm lại giao diện Sago Paint theo hướng tối giản

Người dùng xác nhận yêu cầu là thẩm mỹ và bố cục toàn website, chọn hướng
"Tối giản, hiện đại, thoáng". Phạm vi 54 trang qua các mẫu home, category,
product, editorial/about, phong thủy và calculator. Giữ nội dung có nguồn,
metadata/canonical/noindex và các sửa lỗi audit đang có. Không deploy trong task.

## Khảo sát và phương án thiết kế

Ảnh 54 trang ở task audit trước và source hiện tại cho thấy nền hồng/gradient,
nhãn nhỏ in hoa, thẻ/chip/CTA lặp làm mọi khối cùng nổi bật. Product mobile có
nhiều chữ trước ảnh, khung ảnh trống lớn; article/fengshui chia quá nhiều card.
Đây là vấn đề thứ bậc thị giác và bố cục, không được giải quyết chỉ bằng test kỹ thuật.

Palette: trắng #ffffff, nền phụ #f5f6f4, chữ #202428, chữ phụ #626b74,
đường phân cách #e2e5e1, CTA #a83c31. Be Vietnam Pro/Arial theo chính sách hiện có.
Title có dấu rõ, sentence case, 32–60px theo vai trò; body16–18px/1.65–1.75.
Container1240px; nội dung đọc khoảng70ch. Khoảng section64–96pxdesktop/40–56pxmobile.
Nút bo8px. Đỏ chỉ dùng cho hành động và nhấn có ý nghĩa.

```
Home:     header gọn | lời giới thiệu + CTA     | ảnh công trình + thùng S68
          3 nhóm sơn với ảnh rõ | 2 công cụ | cẩm nang | liên hệ
Product:  breadcrumb | ảnh lớn bên trái       | tên, mô tả, tư vấn bên phải
          thông tin kỹ thuật / ứng dụng / hướng dẫn / FAQ / liên quan
Article:  title + intro | ảnh lớn | nội dung70ch và mục liên quan phụ
```

Đối chiếu brief: bỏ hướng chỉ đổi màu/bo góc vì chưa thay bố cục. Home dùng ảnh
không gian thực tế cùng thùng sơn, product đưa ảnh lên sớm, bài viết tổ chức theo
luồng đọc. Màu ngũ hành giữ như dữ liệu phối màu, không dùng làm nền trang trí.
User đã cho phép thay bố cục và hình thức toàn site nên cập nhật DESIGN.md theo
hướng mới, thay guideline cũ "giữ bố cục/không redesign/button pill".

| Phase/hạng mục | Skill đã sử dụng | Đầu vào | Kết quả/bằng chứng | Điều kiện hoàn tất | Trạng thái |
|---|---|---|---|---|---|
| 1. Khảo sát | frontend-static-site, ponytail, ponytail-audit, seo-audit, web-design-guidelines | DESIGN/context/source và ảnh audit 54 trang; capture trước | Các vấn đề hierarchy/nền/chips/khung ảnh nêu trên | Có bằng chứng UI, không chỉ test tự động | Đạt |
| 2. Phương án | frontend-static-site, frontend-design, ponytail | Lựa chọn trực tiếp của user; assets thật | Palette/type/layout phía trên; phân nhóm ownership | Hướng thẩm mỹ và bố cục rõ | Đạt |
| 3. Home/shared/calculator | frontend-static-site, frontend-design | HTML/CSS hiện có, assets, context | Hero ảnh nhà + S68; header/footer trung tính; calculator metric và chi phí gọn; CSS riêng/context cập nhật | Layout/template/context đồng bộ | Đạt |
| 3. Product/category | frontend-static-site, frontend-design, seo | refresh_pages.py và 21 route | Ảnh trái/chữ phải, tên hiển thị sentence case giữ tên gốc trong schema; cards một liên kết, guide sau danh sách; generator/context đồng bộ | Template/output/context đồng bộ; temp generator | Đạt |
| 3. Editorial/about | frontend-static-site, frontend-design | Blog generator và 14 route | Blog 2 cột; bài viết ảnh lớn/vùng đọc70ch, aside phụ; about phẳng, khôi phục chữ Việt lỗi; ưu tiên ảnh đầu | Template/output/context và layout đọc rõ | Đạt |
| 3. Phong thủy | frontend-static-site, frontend-design | Generator/CSS/17 route | CSS657→105 dòng, bỏ gradient/trang trí ngôi nhà; hub ảnh thật local và srcset720/1200; phần đọc860px, swatch giữ vai trò thông tin | Template/output/context, ảnh S68 giữ file safe | Đạt |
| 4. Kiểm thử/SEO | webapp-testing, seo, web-design-guidelines | Dist sau tích hợp | npm-test-final.txt: 7generator/4unit/22browser đạt. Sau chỉnh readingwidth và tải ảnh chạy lại ma trận162lượt đạt; metadata54trang giữ nguyên; Lighthouse6nhóm + rerun liên quan | 54 trang ×3 viewport; kiểm tra hình ảnh trước/sau, interactions, metadata | Đạt; giới hạn hiệu năng ghi dưới |
| 5. Review | ponytail-review | Diff và UI đã render | Review độc lập tìm và xác minh sửa lỗi cắt số calculator; sửa tương phản footer/form; review source/template và ảnh mới, không còn Must fix trong diff | Không còn Must fix, giao diện đúng hướng; báo giới hạn | Đạt |

## Kết quả và evidence

- [Báo cáo giao diện](../audits/2026-11-09-ui-redesign.md).
- `output/ui-redesign/home-before-{360,1440}.png`, `home-after-*.png`,
  `final-{home,product,catalog,blog,feng,article}-{360,768,1440}.png`;
  ảnh trước/sau nhóm khác trong các thư mục agent.
- `npm-test-final.txt`: toàn bộ 7 generator +4 unit +22 browser đạt.
  Lượt đầu `npm-test.txt` bắt được form thiếu tương phản và assertion còn bám
  tên ảnh/menu cũ; đã sửa, chạy lại full suite đạt. Không tính lượt đầu là đạt.
- `responsive-final.txt`: chạy lại 3 bài kiểm tra đủ54trang/360/768/1440 sau khi
  giới hạn lại `.container.narrow` bị rule chung mở rộng; cả3 đạt. Ảnh srcset
  được bổ sung sau lượt này và kiểm tra riêng hub/file/template.
- `metadata-preservation.json`: 54title/meta/canonical giữ nguyên;
  Google verification/robots/sitemap không đổi byte.
- `product-agent/review.md`, `editorial-agent/REVIEW.md`, `feng-agent/REPORT.md`,
  `final-review.md`: trace source/template và review giao diện độc lập.
- `calculator-large-independent-fixed.json/png`: số liệu hợp lệ rất lớn không
  bị cắt ở320/360/768/1440. Hồi quy đưa vào calculator-validation.spec.cjs.
- `lighthouse/summary.json`, `lighthouse-final/summary.json`,
  `lighthouse-hub-final/summary.json`: lab6nhóm, rerunblog/article/hub sau ưu tiên
  ảnh, hub sau resize ảnh720px. Điểm accessibility/best practices/SEO đều100.
- Site/SEO/generator và git diff --check chạy lại cuối, không lỗi.
- `hub-responsive-image-final.json`: ảnh hero srcset decode qua HTTP/file ở
  360/768/1440, cả6trường hợp đạt. Build cuối tạo98publicfiles trong dist.

## Phần chưa kiểm tra và rủi ro còn lại

Lighthouse lab mới nhất: home94, category96, blog93, article95, hub phong thủy86,
calculator96. Hero ảnh thật mới ở hub có LCP3,82giây, chậm hơn hero CSS cũ
2,19giây dù đã dùng WebP720px37,8KB/ưu tiên tải; CLS lượt cuối0 thay vì0,112
baseline. Đây là đánh đổi cần ghi rõ, chưa khẳng định tốc độ/SEO thực địa đạt.
Chưa kiểm tra Safari/Firefox, thiết bị thật hoặc screen reader. Các thay đổi hiện
chỉ ở source/dist; server preview4310 còn mở để user xem, chưa commit/push/deploy.
