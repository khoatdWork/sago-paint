# Giao diện Sago Paint: tối giản, hiện đại, thoáng

Đã chỉnh bố cục và hình thức cho đủ 54 trang theo lựa chọn của người dùng.
Trọng tâm là thứ bậc thị giác, cách đặt ảnh và khoảng thở. Bản này ở local,
chưa commit/push/deploy.

## Thay đổi theo nhóm trang

| Nhóm | Trước | Bản mới |
|---|---|---|
| Trang chủ | Hero nền hồng, giới thiệu tập trung một sản phẩm; các phần thiếu điểm nhấn rõ | Hero nền trắng với ảnh nhà và thùng S68; giới thiệu hệ sơn bên trái; luồng chọn nhóm sơn → công cụ → cẩm nang; bỏ dải số liệu cuối |
| 18 sản phẩm | Tên in hoa dài, nhiều chip/CTA; mobile có nhiều chữ trước ảnh, khung ảnh trống | Ảnh lớn trái/thông tin phải; mobile tên → ảnh → mô tả; tên hiển thị dễ đọc, giữ tên gốc trong dữ liệu; specs và FAQ dùng đường phân cách nhẹ |
| 3 danh mục | Hướng dẫn dài trước danh sách, card có nhiều nút và lớp trang trí | Danh sách sản phẩm lên trước; card ảnh/tên/mô tả/một liên kết; hướng dẫn chọn nằm sau |
| 14 blog/bài viết/giới thiệu | Gradient, badge nổi, nhiều khối bo góc; nội dung và mục phụ cạnh tranh | Blog 2 cột ảnh lớn; bài viết có ảnh rộng và vùng đọc70ch; aside yên tĩnh; about dùng các cột thông tin phẳng. Khôi phục chữ Việt lỗi trên hai trang |
| 17 phong thủy | Nền pastel/gradient, nhà minh họa bằng CSS, nhiều thẻ nhỏ | Hub ảnh không gian thật; nền trung tính, bảng màu giữ ý nghĩa phối màu; mục tuổi/mệnh và liên quan thành danh sách nhẹ; vùng đọc giới hạn860px |
| Calculator | Hero dài, kết quả chia nhiều hộp và gradient | Hero gọn; tab nhập liệu và kết quả rõ hai phần; metric 2 cột, chi phí theo hàng; mobile xếp dọc, không còn CTA cố định che vùng đọc |

Toàn site dùng Be Vietnam Pro, nền trắng/#f5f6f4, chữ #202428/#626b74 và đỏ
#a83c31 cho hành động. Nút bo8px, header trắng gọn, footer xám nhẹ; menu thu gọn
dưới1200px. Không thêm framework, dependency hoặc thông số sản phẩm mới.

## Xem bản mới

- [Trang chủ local](http://127.0.0.1:4310/)
- [SAGO S 68 PRO](http://127.0.0.1:4310/sago-s-68-pro-chong-tham-a-nang-lo-thien-cao-cap)
- [Danh mục nội thất](http://127.0.0.1:4310/son-noi-that)
- [Cẩm nang](http://127.0.0.1:4310/blog)
- [Phong thủy](http://127.0.0.1:4310/phong-thuy-son-nha/)
- [Tính sơn](http://127.0.0.1:4310/tinh-son/)

Ảnh chụp desktop/mobile/tablet ở `output/ui-redesign/final-*.png`, ảnh trước/sau
trong cùng thư mục và các thư mục agent. Các ảnh là render thật của HTML/CSS.

## Kiểm tra và review

`npm test` đạt7generator,4unit,22browser, gồm toàn54trang tại360/768/1440px.
Sau chỉnh rule container và ưu tiên ảnh, chạy lại ma trận162lượt đạt: không
tràn ngang, ảnh lỗi, sai font, ID trùng hoặc vi phạm axe WCAG được kiểm tra.
Site/SEO/generator và kiểm tra whitespace cuối đều đạt.

Review độc lập đã phát hiện và xác minh sửa lỗi số liệu calculator hợp lệ rất
lớn bị cắt/chồng trên mobile; đã thêm hồi quy. Footer và thông báo form được
sửa tương phản sau khi đổi nền. Product/blog/phong thủy đều cập nhật cả template
và output; generator chỉ được thử trong thư mục tạm trước khi áp dụng có chủ đích.

54 title/meta/canonical giữ nguyên. Alias ANAclean tiếp tục noindex/follow,
canonical về bản chính; file Google verification, robots và sitemap không đổi.
Không còn Must fix trong phạm vi diff sau review.

## Giới hạn thực tế

Điểm Lighthouse lab mới nhất của6nhóm: performance86–96; accessibility,
best practices và SEO100. Hero ảnh thật ở hub phong thủy có LCP3,82giây,
chậm hơn hero CSS cũ2,19giây; đã giảm ảnh xuống37,8KB cho mobile và ưu tiên tải.
CLS hub lượt cuối0, so với0,112trước. Chưa hoàn thành tối ưu tốc độ phần ảnh
này; điểm lab không chứng minh Core Web Vitals thực địa hoặc thứ hạng Google.

Chưa thử trên thiết bị thật, Safari/Firefox hoặc screen reader. Website công khai
chưa nhận các thay đổi này. Nhật ký skill/evidence từng phase ở
[task record](../tasks/2026-11-09-ui-redesign.md).
