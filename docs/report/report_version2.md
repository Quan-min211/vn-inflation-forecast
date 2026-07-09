# Báo cáo Phân tích Chi tiết: Lạm phát Việt Nam 1996–2022

**Môn học:** Phân tích Dữ liệu  
**Lớp:** DAAN436277_02  
**GVHD:** ThS. Trần Trọng Bình  
**Nhóm:** 02 — Đỗ Kiến Hưng · Trần Minh Khánh · Nguyễn Đặng Quốc Anh · Phạm Minh Quân

---

## 4.1 Xác định Mục tiêu và Câu hỏi Chính

### 4.1.1 Bối cảnh Vấn đề

Lạm phát là một trong những chỉ báo vĩ mô quan trọng nhất, ảnh hưởng trực tiếp đến đời sống người dân, chi phí sản xuất của doanh nghiệp, và khả năng hoạch định chính sách của Ngân hàng Nhà nước. Trong 3 thập kỷ qua, Việt Nam đã trải qua nhiều giai đoạn biến động lạm phát mạnh:

- **Khủng hoảng tài chính châu Á — 1997–1998:** Áp lực giảm phát do suy thoái khu vực.
- **Lạm phát phi mã — 2008 và 2011:** CPI tăng vọt lên đỉnh, trùng khớp với khủng hoảng tài chính toàn cầu và chính sách tiền tệ nới lỏng quá mức trong nước.
- **Giai đoạn ổn định — 2014–2019:** Lạm phát được kiểm soát dưới 5% nhờ chính sách tiền tệ thận trọng.
- **COVID-19 — 2020–2021:** Cú sốc cung-cầu chưa từng có tiền lệ.

Câu hỏi đặt ra: **Yếu tố nào thực sự là động lực chính đằng sau các biến động lạm phát này?** Hiểu đúng bản chất nguyên nhân sẽ quyết định chính sách kiểm soát nào là hiệu quả nhất.

> 📷 **Biểu đồ cần chụp từ Streamlit — trang Data Exploration:** Chụp biểu đồ chuỗi CPI growth rate theo năm 1996–2022 để minh họa các điểm bất thường lịch sử.

### 4.1.2 Mục tiêu Phân tích

**Mục tiêu tổng quát:** Xây dựng pipeline phân tích chuỗi thời gian đa biến để phân tách và định lượng các nguồn gốc biến động của lạm phát Việt Nam, từ đó trả lời dứt khoát câu hỏi — quán tính hay tác nhân bên ngoài?

**Mục tiêu cụ thể:**

| STT | Mục tiêu | Phương pháp | Đầu ra kỳ vọng |
|:---:|:---|:---|:---|
| 1 | Xác thực và làm sạch dữ liệu | Kiểm tra missing values, nội suy tuyến tính | Dữ liệu sạch, sẵn sàng cho mô hình |
| 2 | Kiểm định tính dừng và biến đổi | ADF Test, Sai phân bậc 1 | Chuỗi stationary đầu vào cho VAR |
| 3 | Kiểm tra đa cộng tuyến | VIF | Xác nhận bộ 4 biến không có vấn đề collinearity |
| 4 | Định lượng tác động lên lạm phát | VAR, Granger Causality | Xác định biến nào dẫn dắt CPI |
| 5 | Phân rã biến động lạm phát | FEVD 10 kỳ, IRF | Trả lời câu hỏi: % quán tính so với % ngoại sinh |

**Hai giả thuyết cần kiểm chứng:**

| Giả thuyết | Mô tả | Công cụ kiểm chứng |
|:---|:---|:---|
| H1 — "Bệnh tự miễn" | Lạm phát VN chủ yếu do quán tính nội sinh, kỳ vọng tâm lý tạo ra vòng lặp tự củng cố. | FEVD: CPI tự giải thích trên 80% phương sai. |
| H2 — "Tác nhân bên ngoài" | Lạm phát VN chủ yếu do các yếu tố kinh tế vĩ mô bên ngoài chi phối. | FEVD: Biến ngoại sinh giải thích trên 20%; Granger có ý nghĩa thống kê. |

### 4.1.3 Biến Mục tiêu và Các Chỉ số Theo dõi

- **Biến mục tiêu:** `cpi_growth_percent` — Tốc độ tăng chỉ số giá tiêu dùng hàng năm, đo lường mức lạm phát người dân trực tiếp cảm nhận.

| Chỉ số | Ý nghĩa | Nguồn |
|:---|:---|:---|
| FEVD — CPI tự giải thích | Mức độ quán tính lạm phát | Mô hình VAR |
| FEVD — GDP, Lãi suất, Tỷ giá | Đóng góp của từng tác nhân bên ngoài | Mô hình VAR |
| p-value Granger Causality | Ý nghĩa thống kê của tính dẫn dắt | Kiểm định Granger |
| ADF p-value | Tính dừng của từng chuỗi | Kiểm định ADF |
| VIF Score | Mức độ đa cộng tuyến | statsmodels |

### 4.1.4 Giới hạn Phân tích

- Không xây dựng dự báo điểm cho CPI trong tương lai. Mục tiêu là phân tách nguyên nhân.
- Không sử dụng mô hình phi tuyến trong phiên bản này.
- Không phân tích ở tần suất tháng hoặc quý do giới hạn nguồn dữ liệu từ World Bank.

---

## 4.2 Thu thập, Làm sạch và Xác thực Dữ liệu

### 4.2.1 Cấu trúc Dữ liệu Ban đầu

Dữ liệu được tải từ World Bank — World Development Indicators và lưu tại `data/dataset_project1.xlsx`.

- **Số quan sát:** 27 dòng, tương ứng các năm 1996–2022
- **Số cột gốc:** 12 cột, bao gồm cột `years` và 11 biến số kinh tế
- **Kiểu dữ liệu:** Tất cả biến kinh tế là số thực — float64
- **Chỉ mục thời gian:** Cột `years` được chuyển sang định dạng datetime và đặt làm index

### 4.2.2 Phân tích Giá trị Thiếu

Trong toàn bộ 11 biến, chỉ hai biến thuộc Trụ cột Tiền tệ có giá trị thiếu ở một số năm đầu:

| Biến | Lý do thiếu |
|:---|:---|
| `domestic_credit_index` | Dữ liệu tín dụng nội địa World Bank chưa ghi nhận đầy đủ cho Việt Nam giai đoạn đầu |
| `lending_interest_percent` | Tương tự — lãi suất cho vay thiếu ở các năm đầu nghiên cứu |

**Giải pháp:** Nội suy tuyến tính — phù hợp cho chuỗi kinh tế vì giả định giá trị thay đổi dần dần theo thời gian. Sau xử lý, tổng giá trị thiếu bằng 0 và không mất quan sát nào.

> 📷 **Biểu đồ cần chụp từ Streamlit — trang Data Exploration:** Chụp heatmap missing values để minh họa vị trí và phân bố các giá trị thiếu.

### 4.2.3 Làm sạch Dữ liệu

**Phát hiện cột lỗi chính tả:** Dataset gốc có hai cột gần giống nhau — `gdp_delflator_percent` và `gdp_deflator_percent`. Kiểm tra cho thấy đây là hai cột khác nhau về bản chất: một là Index tích lũy, một là Growth Rate hàng năm. Cột đầu được đổi tên thành `gdp_deflator_index` trước khi loại khỏi bộ biến VAR.

**Bốn biến giữ lại cho mô hình VAR:**

| Biến | Kênh truyền dẫn | Vai trò |
|:---|:---|:---|
| `cpi_growth_percent` | Lạm phát | Biến mục tiêu |
| `gdp_growth_percent` | Cầu kéo | Tác nhân bên ngoài |
| `lending_interest_percent` | Kênh tiền tệ | Tác nhân bên ngoài |
| `officical_exchange_rate_percent` | Chi phí đẩy từ tỷ giá | Tác nhân bên ngoài |

> Lý do rút gọn còn 4 biến: với 27 quan sát, đưa quá nhiều biến vào VAR sẽ cạn bậc tự do và dẫn đến quá khớp.

### 4.2.4 Trực quan hóa Bốn Chuỗi Thời gian

Bốn biến được vẽ song song để xác nhận dữ liệu và nhận biết sơ bộ xu hướng:

- CPI growth có hai đỉnh rõ ràng vào 2008 và 2011, sau đó ổn định dưới 5% từ 2013.
- GDP growth dao động ổn định 5–7%, ngoại trừ 2020 do COVID-19.
- Lãi suất cho vay có xu hướng giảm dần, phản ánh lộ trình nới lỏng tiền tệ của Ngân hàng Nhà nước.
- Tỷ giá có xu hướng tăng tích lũy — dấu hiệu chuỗi không dừng, cần sai phân trước khi vào VAR.

> 📷 **Biểu đồ cần chụp từ Streamlit — trang Data Exploration:** Chụp biểu đồ bốn panel song song của bốn biến để minh họa đặc trưng từng chuỗi.

---

## 4.3 Phân tích và Trực quan hóa Kết quả

### 4.3.1 Kiểm định ADF và Sai phân

Tất cả 4 biến được kiểm định ADF trước khi đưa vào VAR. Biến không vượt qua ADF — p-value lớn hơn 0.05 — được lấy sai phân bậc 1 và kiểm định lại. Sau bước này, toàn bộ bộ biến đầu vào VAR đều đạt tính dừng.

> 📷 **Biểu đồ cần chụp từ Streamlit — trang Stationarity Testing:** Chụp bảng kết quả ADF trước và sau sai phân, bao gồm ADF statistic, p-value, và kết luận Dừng hay Không dừng cho 4 biến.

### 4.3.2 Kiểm tra VIF

VIF được tính trên bộ 4 biến sau sai phân để xác nhận không có đa cộng tuyến nghiêm trọng. VIF cao hơn 10 là ngưỡng cảnh báo. Kết quả hợp lệ là điều kiện cần để hệ số VAR có ý nghĩa thống kê đáng tin cậy.

> 📷 **Biểu đồ cần chụp từ Streamlit — trang Stationarity Testing:** Chụp bảng VIF Score cho 4 biến.

### 4.3.3 Mô hình VAR(1) và Dự báo Ngắn hạn

VAR bậc 1 được chọn vì phù hợp với mẫu 27 quan sát — bậc lag bằng 1 cho phép đọc trực tiếp ảnh hưởng năm trước lên năm nay mà không tiêu tốn quá nhiều bậc tự do. Dự báo ngắn hạn 3 kỳ được tính như kiểm tra sanity — xác nhận chiều dự báo hợp lý về mặt kinh tế học.

> 📷 **Biểu đồ cần chụp từ Streamlit — trang VAR Model:** Chụp bảng dự báo 3 kỳ của 4 biến.

### 4.3.4 FEVD 10 kỳ — Bằng chứng Trung tâm

FEVD phân rã sai số dự báo của CPI thành phần giải thích bởi chính CPI quá khứ và phần đến từ GDP, lãi suất, tỷ giá. Kết quả cho thấy phần CPI tự giải thích chiếm ưu thế ổn định, nghiêng rõ về **quán tính lạm phát**.

Diễn giải kinh tế: lạm phát quá khứ hình thành kỳ vọng, kỳ vọng ảnh hưởng hành vi định giá của doanh nghiệp và người dân, hành vi định giá đó tiếp tục duy trì lạm phát cho kỳ sau — một vòng lặp tự củng cố điển hình của Bệnh tự miễn.

> 📷 **Biểu đồ cần chụp từ Streamlit — trang VAR Model:** Chụp biểu đồ FEVD cột chồng 10 kỳ và bảng số liệu FEVD. **Đây là biểu đồ quan trọng nhất cần chèn vào báo cáo.**

### 4.3.5 Kiểm tra Phụ — Granger Causality và IRF

Granger Causality kiểm tra xem biến ngoại sinh nào có tín hiệu dự báo CPI đủ rõ ở độ trễ 1 năm. GDP là biến có tín hiệu dẫn dắt đáng chú ý nhất. Lãi suất và tỷ giá có ít bằng chứng hơn.

IRF theo dõi phản ứng của CPI trước cú sốc từng biến trong 10 kỳ. Đường IRF về 0 nhanh xác nhận tác động ngắn hạn và hạn chế trong dài hạn của các tác nhân bên ngoài.

> 📷 **Biểu đồ cần chụp từ Streamlit — trang VAR Model:** Chụp bảng Granger Causality và lưới biểu đồ IRF phản ứng của CPI.

---

## 4.4 Tường thuật và Đề xuất

### 4.4.1 Phán quyết

> **Lạm phát tại Việt Nam trong 3 thập kỷ qua chủ yếu mang tính QUÁN TÍNH — Bệnh tự miễn.**

### 4.4.2 Chuỗi Bằng chứng

| Bước | Bằng chứng | Vai trò |
|:---|:---|:---|
| ADF và Sai phân | Tất cả 4 biến dừng trước khi vào VAR | Đảm bảo dữ liệu hợp lệ, tránh Spurious Regression |
| VIF | Không có đa cộng tuyến nghiêm trọng | Xác nhận hệ số VAR đáng tin cậy |
| VAR(1) hội tụ | Mô hình ổn định với mẫu 27 quan sát | Nền tảng để tính FEVD và IRF |
| **FEVD 10 kỳ** | CPI tự giải thích phần lớn phương sai | **Bằng chứng trung tâm** |
| Granger + IRF | GDP dẫn dắt; IRF tắt nhanh | Bằng chứng phụ, xác nhận chiều và bản chất ngắn hạn |

> 📷 **Biểu đồ cần chụp từ Streamlit — trang Conclusion:** Chụp toàn bộ trang Conclusion bao gồm metric "CPI tự giải thích / Tác nhân bên ngoài" và bảng tóm tắt bằng chứng.

### 4.4.3 Hàm ý Chính sách

1. **Neo kỳ vọng lạm phát** — Công bố và duy trì mục tiêu lạm phát rõ ràng, nhất quán để phá vỡ vòng lặp tự củng cố.
2. **Truyền thông chính sách minh bạch và sớm** — Giải thích rõ lý do điều chỉnh lãi suất hay tỷ giá giúp thị trường không hình thành kỳ vọng lạm phát sai lệch.
3. **Theo dõi GDP như tín hiệu dẫn dắt** — Biến ngoại sinh có tín hiệu đáng chú ý nhất. Khi GDP tăng nóng, cần chủ động kiểm soát áp lực cầu kéo trước khi lan sang lạm phát.
4. **Thận trọng với điều chỉnh tiền tệ giật cục** — Tác động của lãi suất và tỷ giá lên lạm phát cốt lõi là hạn chế và có độ trễ.

### 4.4.4 Hạn chế và Hướng mở rộng

- **Mẫu nhỏ và tần suất năm:** Kết luận sẽ vững hơn nếu kiểm chứng lại với dữ liệu quý từ Tổng cục Thống kê.
- **Mô hình tuyến tính:** VAR không bắt được các điểm gãy cấu trúc đột ngột. Regime-Switching VAR là hướng mở rộng tiếp theo.
- **Tích hợp biến tâm lý:** Sentiment Analysis từ báo chí kinh tế để lượng hóa trực tiếp phần kỳ vọng trong kênh quán tính — bằng chứng mạnh hơn cho giả thuyết Bệnh tự miễn.
