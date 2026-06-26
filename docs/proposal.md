# Academic Proposal
# Đề xuất Đề tài: Phân tích các yếu tố vĩ mô tác động đến lạm phát tại Việt Nam từ năm 1996 đến năm 2022 và dự báo xu hướng bằng mô hình chuỗi thời gian

## 1. Đặt vấn đề
Lạm phát luôn là một trong những chỉ số kinh tế vĩ mô quan trọng nhất, phản ánh sức khỏe của nền kinh tế và ảnh hưởng trực tiếp đến đời sống người dân cũng như chiến lược kinh doanh của doanh nghiệp. Trong 3 thập kỷ qua (1996 - 2022), nền kinh tế Việt Nam đã trải qua nhiều giai đoạn biến động: từ khủng hoảng tài chính châu Á (1997), khủng hoảng tài chính toàn cầu (2008), đến đại dịch COVID-19 (2020-2021). 

Mặc dù Ngân hàng Nhà nước luôn nỗ lực kiểm soát lạm phát, một câu hỏi lớn vẫn được đặt ra: **"Lạm phát tại Việt Nam chủ yếu là do quán tính (kỳ vọng lạm phát - bệnh tự miễn) hay do các cú sốc từ bên ngoài (tỷ giá, tín dụng, cung cầu - tác nhân ngoại sinh)?"**. Để trả lời câu hỏi này, việc áp dụng các mô hình kinh tế lượng chuỗi thời gian tiên tiến là vô cùng cần thiết.

## 2. Mục tiêu nghiên cứu
- **Mục tiêu 1:** Phân tích sự biến động của lạm phát (đo lường qua CPI) và các yếu tố vĩ mô (Tăng trưởng GDP, Tỷ giá, Lãi suất, Tín dụng) từ 1996 đến 2022.
- **Mục tiêu 2:** Xây dựng mô hình ARIMA để dự báo lạm phát dựa trên quán tính lịch sử.
- **Mục tiêu 3:** Ứng dụng mô hình VAR (Vector Autoregression) để phân tích tác động qua lại và độ trễ của các biến số kinh tế vĩ mô đối với lạm phát.
- **Mục tiêu 4:** Đưa ra dự báo xu hướng lạm phát trong 3 năm tới và đề xuất hàm ý chính sách.

## 3. Dữ liệu và Phương pháp
- **Dữ liệu:** Dữ liệu thứ cấp dạng năm (Annual Data) từ 1996 - 2022, thu thập từ World Bank, Tổng cục Thống kê (GSO), và Ngân hàng Nhà nước. Bao gồm 11 biến số đại diện cho 4 trụ cột vĩ mô.
- **Phương pháp:**
  - Tiền xử lý dữ liệu và xử lý giá trị khuyết thiếu.
  - Kiểm định tính dừng (Stationarity) bằng Augmented Dickey-Fuller (ADF).
  - Phân tích tương quan và đa cộng tuyến (VIF).
  - Lập mô hình chuỗi thời gian đơn biến (ARIMA) và đa biến (VAR).
  - Phân tích hàm phản ứng xung (IRF) và Phân rã phương sai (FEVD).

## 4. Tính mới và Đóng góp của đề tài
Đề tài không chỉ dừng lại ở việc hồi quy tuyến tính đơn thuần mà áp dụng phương pháp chuỗi thời gian để xử lý đặc tính "tự tương quan" của dữ liệu kinh tế. Việc kết hợp so sánh giữa mô hình ARIMA (nội sinh) và VAR (ngoại sinh) giúp đem lại cái nhìn toàn diện và định lượng rõ ràng hơn về nguồn gốc thực sự của lạm phát tại Việt Nam.