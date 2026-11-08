# Hệ thống thiết kế Sago Paint

## Mục đích

Giúp chủ nhà, thợ sơn và khách công trình Việt Nam chọn hệ sơn, hiểu cách thi công
và liên hệ tư vấn. Giữ bố cục, hình ảnh sản phẩm và nhận diện hiện có.

## Màu và typography

| Vai trò | Giá trị |
|---|---|
| Màu thương hiệu | `#d45141` |
| Màu thương hiệu đậm, chữ/nút cần tương phản | `#a83c31` |
| Chữ chính | `#202428` |
| Chữ phụ | `#626b74` |
| Nền nhẹ | `#fff4f1` |
| Nền trắng | `#ffffff` |

Chữ dùng Be Vietnam Pro, Arial, sans-serif. Tải Google Fonts với `display=swap`,
weight normal 300–900 và italic 400/700. Không nhúng font vào repo.
Token ở `assets/css/site-base.css`; override cả Bootstrap và heading.
Khai báo font-family và tham chiếu --font-sans chỉ nằm trong file chung này;
CSS riêng của trang kế thừa font, không khai báo lặp lại biến ở file khác.
Body 400, nhãn 600, navigation/button 700, heading 700–800; số nhấn 900 khi cần.
Weight trung gian 650/750/850 được chuẩn hóa về 600/700/800 để dùng font có thật.
Giữ type scale từng nhóm trang, chỉ chỉnh khi cần tránh tràn và đảm bảo đọc rõ dấu.
Body tối thiểu 16px; line-height 1.6; nội dung dài rộng tối đa khoảng 75ch.

## Bố cục và thành phần

- Dùng container/grid Bootstrap; các mốc chính 576/768/992/1200/1400px.
- Spacing theo bội số 4/8px; section hiện có 46–80px; không redesign toàn site.
- Header fixed: nội dung và điểm neo phải chừa đủ khoảng trống phía trên.
- CTA chính là tư vấn/chọn sản phẩm/tính sơn. Hình sản phẩm dùng `object-fit: contain`;
  hình công trình dùng `cover`, luôn có giới hạn chiều rộng và tỉ lệ ổn định.
- Giữ button pill hiện có. Link/heading có tên rõ; không dùng card trang trí thay
  cấu trúc thông tin. Số liệu tính sơn dùng tabular-nums.
- Form tính sơn chỉ ước tính. Form tư vấn mở ứng dụng email với dữ liệu và kết quả
  hiện tại; người dùng tự gửi email. Có nút gọi dự phòng, không hiển thị “đã gửi”.

## Tương tác và accessibility

Skip link là phần tử focus đầu tiên, trỏ tới `#main-content`; ẩn mặc định và hiện
khi nhận focus. Stylesheet chung dùng đường dẫn tương đối theo độ sâu HTML để
tải được cả khi mở file trực tiếp và qua HTTP. Tab điều khiển
bằng ArrowLeft/ArrowRight/Home/End; chỉ tab đang chọn nằm trong thứ tự Tab.
Link/button/input có focus ring rõ; sticky CTA không che phần tử focus.
Giữ nhãn và thông báo lỗi gắn với control; lỗi đầu tiên nhận focus.
Màu chữ cần đạt WCAG AA, kiểm tra trên nền thực tế; không chỉ dựa trên token.
Motion tôn trọng `prefers-reduced-motion`; transition liệt kê thuộc tính cụ thể.
Không che overflow bằng cách cắt nội dung; sửa gutter, min-width và hình gây tràn.

## Kiểm tra khi thay đổi

Kiểm tra 360/768/1440px và font fallback; screenshot trang đại diện trước/sau.
Đổi CSS chung phải kiểm tra đủ các nhóm trang. Chạy axe cho trang đã render,
kiểm tra bàn phím và so sánh Lighthouse; không sử dụng điểm lab như cam kết SEO.
