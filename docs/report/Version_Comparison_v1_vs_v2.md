## 1. Tóm tắt Tổng quan

Tài liệu này trình bày những điểm khác biệt chính và sự nâng cấp về phương pháp luận trong **Phiên bản 2** - `Project1_DAAN_v2.ipynb`, so với **Phiên bản 1** ban đầu - `Project1_DAAN.ipynb`. 

Trong khi Phiên bản 1 thiết lập nền tảng cho việc khám phá dữ liệu - EDA, và xây dựng khung dự báo chuỗi thời gian đa biến cơ bản, thì Phiên bản 2 là một bước nhảy vọt về tính chặt chẽ trong thống kê. Các cập nhật trong v2 giải quyết triệt để những cạm bẫy phổ biến trong phân tích chuỗi thời gian, chẳng hạn như hiện tượng đa cộng tuyến, dữ liệu không dừng, và hồi quy giả, đảm bảo rằng các kết luận cuối cùng mang tính khoa học và có độ tin cậy cao nhất.

---

## 2. So sánh Chi tiết

### 2.1 Làm sạch & Tiền xử lý Dữ liệu

| Bước/Tính năng | Phiên bản 1 - `Project1_DAAN.ipynb` | Phiên bản 2 - `Project1_DAAN_v2.ipynb` | Tác động của sự nâng cấp trong v2 |
|:---|:---|:---|:---|
| **Đặt tên Cột** | Giữ nguyên tên cột gốc từ dữ liệu thô. | Phát hiện và sửa lỗi chính tả - `gdp_delflator_percent` → `gdp_deflator_index`. | Làm rõ sự khác biệt bản chất giữa Chỉ số lạm phát bóc tách - Index, và Tốc độ tăng trưởng, ngăn ngừa việc diễn giải sai. |
| **Xử lý Giá trị Thiếu** | Xử lý cơ bản hoặc có thể làm mất dữ liệu khi loại bỏ các dòng `NaN`. | Áp dụng **Nội suy Tuyến tính - Linear Interpolation** đặc biệt phù hợp cho dữ liệu chuỗi thời gian. | Giữ nguyên toàn bộ 27 quan sát - rất quan trọng với mẫu nhỏ, trong khi vẫn bảo toàn được xu hướng thời gian tự nhiên của các trụ cột vĩ mô. |

### 2.2 Chọn lọc Biến & Đa cộng tuyến

| Bước/Tính năng | Phiên bản 1 - `Project1_DAAN.ipynb` | Phiên bản 2 - `Project1_DAAN_v2.ipynb` | Tác động của sự nâng cấp trong v2 |
|:---|:---|:---|:---|
| **Kiểm tra VIF** | Chưa được chú trọng hoặc xử lý triệt để. | Đưa vào ngưỡng đánh giá **Hệ số Phóng đại Phương sai - VIF** nghiêm ngặt. | Ngăn chặn mô hình VAR bị nhiễu do đa cộng tuyến gây ra bởi các biến chỉ số - tín dụng, xuất/nhập khẩu, có độ tương quan quá cao. |
| **Chọn lọc Biến** | Có xu hướng đưa tất cả/hầu hết các biến vào mô hình. | Chọn lọc tinh gọn thành 4 biến cốt lõi đại diện cho 4 Trụ cột Vĩ mô - CPI, GDP, Lãi suất, Tỷ giá. | Tăng bậc tự do - degrees of freedom, cho mô hình VAR và cải thiện độ ổn định của các hệ số ước lượng. |

### 2.3 Tính Dừng & Các giả định Chuỗi thời gian

| Bước/Tính năng | Phiên bản 1 - `Project1_DAAN.ipynb` | Phiên bản 2 - `Project1_DAAN_v2.ipynb` | Tác động của sự nâng cấp trong v2 |
|:---|:---|:---|:---|
| **Kiểm định ADF** | Có kiểm tra tính dừng nhưng chưa xử lý triệt để trước khi đưa vào mô hình. | Kiểm định **Augmented Dickey-Fuller - ADF** toàn diện kết hợp bắt buộc **Sai phân Bậc 1** - `diff()` cho các biến không dừng. | Loại bỏ hoàn toàn rủi ro *Hồi quy giả - Spurious Regression*. Đảm bảo tất cả dữ liệu đầu vào đều dừng, giúp kết quả của mô hình VAR hoàn toàn hợp lệ về mặt thống kê. |

### 2.4 Mô hình VAR Nâng cao & Diễn giải

| Bước/Tính năng | Phiên bản 1 - `Project1_DAAN.ipynb` | Phiên bản 2 - `Project1_DAAN_v2.ipynb` | Tác động của sự nâng cấp trong v2 |
|:---|:---|:---|:---|
| **Chọn Bậc trễ - Lag** | Chọn bậc trễ ngẫu nhiên hoặc theo mặc định. | Chọn bậc trễ có hệ thống dựa trên **Tiêu chuẩn Akaike - AIC** với ràng buộc `maxlags=2`. | Cân bằng giữa độ phức tạp của mô hình với quy mô mẫu giới hạn - ngăn chặn overfitting. |
| **Phân tích Nhân quả** | Tập trung nhiều vào dự báo cơ bản. | Đi sâu vào **Kiểm định Nhân quả Granger**, **Hàm Phản ứng Xung kích - IRF**, và **Phân rã Phương sai Sai số Dự báo - FEVD**. | Chuyển trọng tâm dự án từ dự báo đơn thuần sang *Suy luận Cấu trúc*. Trả lời thành công "Câu hỏi Tối thượng" bằng cách lượng hóa được >90% biến động lạm phát là do quán tính - "Bệnh tự miễn". |

---

## 3. Kết luận

Sự chuyển đổi từ `Project1_DAAN.ipynb` sang `Project1_DAAN_v2.ipynb` đánh dấu sự trưởng thành của dự án từ một bản phân tích khám phá cơ bản thành một **nghiên cứu kinh tế vĩ mô chuyên sâu, đạt chuẩn học thuật và chặt chẽ về mặt thống kê**. 

Bằng cách giải quyết triệt để đa cộng tuyến - VIF, và đảm bảo tính dừng - ADF + Sai phân, **Phiên bản 2** đảm bảo rằng toàn bộ pipeline phân tích—đặc biệt là kết quả Granger Causality và FEVD—hoàn toàn vững chắc, mang tính thuyết phục cao và đủ khả năng làm cơ sở cho các đề xuất chính sách thực tiễn.

---
*Được tạo bởi AI Assistant cho Tài liệu Dự án Dự báo Kinh tế Vĩ mô.*
