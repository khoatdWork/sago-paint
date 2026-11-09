# Kết quả kiểm tra toàn bộ website — 09/11/2026

Đã kiểm tra trang chủ và toàn bộ 53 trang còn lại. Các lỗi xác nhận được đã sửa
ở bản local, bao gồm template sinh trang và kiểm thử hồi quy. Không còn Must fix
trong diff sau review độc lập. Bản sửa của lần kiểm tra này chưa commit/push/deploy.

## Phạm vi và kết quả tổng thể

| Nội dung | Bằng chứng/kết quả |
|---|---|
| Website đang chạy | https://sagopaint.vn, release 6d46fe7; 54 trang × 360/768/1440px = 162 lượt render Chromium |
| Tình trạng live trước sửa | 54/54 route HTTP 200; không thấy ảnh tải hỏng, tràn ngang, lỗi JavaScript hay vi phạm axe WCAG ở 3 kích thước |
| UI bổ sung | 9 trang đại diện × 320/992/1024px; menu mobile mở được 9/9; kiểm tra bàn phím ở các nhóm trang, không xác nhận focus bị che |
| SEO | 54 canonical/robots khớp nguồn; sitemap có đúng 53 URL indexable; 8 redirect cũ tới đúng đích; alias giữ noindex/follow và canonical về bản chính |
| Bản local sau sửa | npm test đạt 7 generator + 4 unit + 22 browser; ma trận 54 trang × 3 kích thước, gồm font/ảnh/overflow/axe và ID trùng |
| Bất biến | Metadata/canonical, dữ liệu doanh nghiệp/Product giữ nguyên; homepage, file Google verification, robots và sitemap không đổi |

Danh sách đủ 54 trang: [page inventory](../pages/README.md). Nhật ký từng phase
và skill thực sự sử dụng: [task record](../tasks/2026-11-09-site-audit.md).

## Lỗi đã sửa ở local

| Lỗi và ảnh hưởng | Thay đổi | Xác minh |
|---|---|---|
| Calculator coi số âm, số vượt khả năng nhập hoặc số lớp lẻ là kết quả hợp lệ; có thể soạn email chứa ước tính sai. Tên chỉ có khoảng trắng và phone `abc` cũng được chấp nhận | Kiểm tra required/min/step/badInput của panel đang chọn; xóa kết quả sai, gắn lỗi với trường và focus khi submit; trim tên và kiểm tra ký tự phone. Gỡ ID lỗi trùng | Test mới tái hiện lỗi trước sửa; sau sửa chặn email sai, vẫn cho diện tích 0, không kiểm tra panel ẩn, chặn overflow, giữ dữ liệu hợp lệ. Không gửi email thật |
| FAQ thời gian khô sai trên 5 sản phẩm và JSON-LD tương ứng: hai bột trét trả lời bằng khối lượng thể tích; Aqua Shield và hai ANA Satin chỉ trả lời tiêu đề rỗng | Generator chọn thông số có giá trị thời gian, dùng quy trình sẵn có khi cần. Bột trét: 16 giờ; ba sơn: khô bề mặt 30 phút, lớp kế tiếp 120 phút | Nội dung visible và FAQPage khớp; test generator trong thư mục tạm kiểm tra không thay metadata/schema khác; không tự tạo thông số |
| Danh mục sơn nội thất và các mục liên quan lặp ANAclean qua alias `-2` | Loại noindex alias khỏi card, ItemList và related trong generator/output; giữ trang alias và canonical hiện có | Danh mục còn 7 lựa chọn sản phẩm; test bảo vệ alias exclusion và noindex/canonical |
| Ảnh SAGO S68 Pro mất khi mở trực tiếp 24 HTML; calculator còn mất JS/ảnh qua `file://` do đường dẫn bắt đầu bằng `/assets/` | Dùng đường dẫn tương đối ở root, thư mục và template phong thủy; sửa script/ảnh calculator; site check chặn tái xuất hiện đường dẫn ảnh này | Test file preview ở sản phẩm, bài viết, phong thủy hai độ sâu và calculator; generator kiểm tra cả 17 output phong thủy; ma trận HTTP toàn site đạt |

Lỗi ảnh của đợt audit này xảy ra ở bản xem file trực tiếp. Trong 162 lượt render
website live, ảnh S68 tải được. Homepage không cần sửa thêm trong đợt này.

## Hiệu năng còn cần cải thiện

Lighthouse là phép đo lab trên bản đóng gói local. Baseline 6 nhóm trang có điểm
performance 91–97; accessibility, best practices và SEO đều 100. Chạy lại 4 trang
đại diện liên quan sau sửa cho performance 92–98; ba nhóm điểm còn lại vẫn 100.
Không diễn giải dao động nhỏ giữa hai lần đo thành cải thiện do sửa lỗi.

| Trang | Quan sát | Nguyên nhân/việc còn lại |
|---|---|---|
| `/phong-thuy-son-nha/` | CLS baseline 0,112; sau sửa 0,117, vượt ngưỡng tốt 0,1 trong lượt đo | Lighthouse chỉ ra font Be Vietnam Pro tải xong làm chữ đầu trang đổi số dòng và đẩy khối minh họa. Khối minh họa đã có chiều cao; không phải ảnh thiếu kích thước. Cần thử riêng cách giảm chênh lệch fallback theo đúng chính sách font |
| `/blog` | LCP baseline 3,32 giây | Còn cơ hội tối ưu tải phần nội dung đầu trang; chưa thay asset/CSS/tải font của trang này |

Không có dữ liệu thực địa để kết luận Core Web Vitals thực tế, trạng thái index,
thứ hạng Google hay rich results. Điểm SEO 100 không xác nhận các trạng thái đó.

## Evidence và giới hạn

Các file tại `output/site-audit/2026-11-09/`: `live-{360,768,1440}.json`,
`live-screenshots/`, `contact-1440-{1,2,3}.png`, `local-before.txt`,
`local-after.txt`, `generators-final.txt`, `invariants.json`,
`lighthouse-before/summary.json`, `lighthouse-after/summary.json`.
Evidence bổ sung và review ở `output/site-audit/{seo-agent,ui-agent,interaction-agent}/`.

Kết quả tự động và ảnh đại diện không thay thế thử nghiệm trên thiết bị thật.
Chưa thử Safari/Firefox, screen reader hoặc thao tác gửi bằng ứng dụng email.
Production ở trên là trước sửa; cần một lần phát hành mới để đưa các sửa lỗi
local lên website thật.
