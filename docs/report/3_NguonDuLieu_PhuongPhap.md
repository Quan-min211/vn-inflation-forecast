# 3. NGUỒN DỮ LIỆU VÀ PHƯƠNG PHÁP LUẬN - DATA SOURCES AND METHODOLOGY

---

## 3.1 Nguồn Dữ liệu

### Nguồn chính
- **Tên:** World Bank — World Development Indicators - WDI
- **Tệp dữ liệu:** `dataset_project1.xlsx`
- **Đường dẫn:** `data/dataset_project1.xlsx`
- **Định dạng:** Microsoft Excel (.xlsx), 1 sheet duy nhất
- **Số quan sát:** 27 dòng - tương ứng 27 năm: 1996–2022
- **Số biến:** 11 cột - không tính cột `years`

### Đặc điểm dữ liệu
- Dữ liệu thuộc dạng **chuỗi thời gian - time series** với tần suất **hàng năm**.
- Dữ liệu bao gồm cả **chỉ số tích lũy - Index** và **tỷ lệ tăng trưởng - Growth Rate %**, phục vụ các mục đích phân tích khác nhau.
- Một số biến có **giá trị thiếu - missing values** trong các năm đầu do World Bank chưa thu thập đầy đủ cho Việt Nam.

### Giới hạn của nguồn dữ liệu
- Tần suất hàng năm làm "mịn" các biến động ngắn hạn, khó bắt nhịp các cú sốc tức thời - giá xăng dầu, tỷ giá biến động theo tháng.
- Kích thước mẫu nhỏ - 27 quan sát, giới hạn bậc tự do cho các mô hình đa biến, đặc biệt khi cần ước lượng nhiều tham số - VAR với nhiều lag.

---

## 3.2 Phương pháp luận Tổng quan

Quy trình phân tích được thiết kế thành **pipeline 5 giai đoạn** tuần tự, mỗi giai đoạn xây dựng trên kết quả của giai đoạn trước:

```
┌─────────────────────┐
│ Giai đoạn 1         │
│ Khám phá dữ liệu   │  → Data Overview, Missing Values, Descriptive Stats
│ thô - EDA           │
└────────┬────────────┘
         │
┌────────▼────────────┐
│ Giai đoạn 2         │
│ Làm sạch & Xác thực │  → Xử lý cột trùng, Interpolation, Trend Visualization
│ dữ liệu             │
└────────┬────────────┘
         │
┌────────▼────────────┐
│ Giai đoạn 3         │
│ Phân tích mối       │  → Correlation Heatmap, VIF - Multicollinearity Check
│ quan hệ             │
└────────┬────────────┘
         │
┌────────▼────────────┐
│ Giai đoạn 4         │
│ Kiểm định giả       │  → ADF Test - Stationarity, Differencing, Re-test
│ thuyết thống kê     │
└────────┬────────────┘
         │
┌────────▼────────────┐
│ Giai đoạn 5         │
│ Mô hình hóa &      │  → VAR, Granger Causality, IRF, FEVD
│ Phân rã phương sai  │
└─────────────────────┘
```

---

## 3.3 Các Phương pháp Thống kê và Mô hình

### 3.3.1 Xử lý Dữ liệu Thiếu: Nội suy Tuyến tính - Linear Interpolation

- **Áp dụng cho:** `domestic_credit_index`, `lending_interest_percent`
- **Lý do chọn:** Phương pháp phù hợp nhất cho dữ liệu chuỗi thời gian vì giả định giá trị biến đổi dần dần theo thời gian — hợp lý với dữ liệu kinh tế vĩ mô.
- **Cơ chế:** Giá trị thiếu được ước lượng bằng phép nội suy tuyến tính giữa hai điểm dữ liệu liền kề có giá trị.

### 3.3.2 Ma trận Tương quan Pearson - Correlation Matrix

- **Mục đích:** Xác định mức độ và chiều hướng của mối quan hệ tuyến tính giữa từng cặp biến.
- **Đầu ra:** Heatmap trực quan với giá trị từ -1 - nghịch mạnh, đến +1 - thuận mạnh.
- **Vai trò trong pipeline:** Phát hiện sớm các biến có tương quan cao bất thường — dấu hiệu cảnh báo đa cộng tuyến.

### 3.3.3 Hệ số Phóng đại Phương sai - VIF — Variance Inflation Factor

- **Mục đích:** Lượng hóa mức độ "trùng lặp thông tin" giữa các biến độc lập.
- **Ngưỡng đánh giá:**
  - VIF > 10: Đa cộng tuyến nghiêm trọng → phải loại bỏ hoặc biến đổi biến.
  - VIF > 5: Đa cộng tuyến cần lưu ý.
  - VIF < 5: Chấp nhận được.
- **Hậu quả nếu bỏ qua:** Mô hình VAR sẽ cho hệ số "ảo" — kết luận sai về yếu tố nào thực sự ảnh hưởng lạm phát.

### 3.3.4 Kiểm định Tính Dừng: Augmented Dickey-Fuller - ADF

- **Giả thuyết:**
  - H0: Chuỗi KHÔNG dừng - có nghiệm đơn vị — unit root
  - H1: Chuỗi dừng - stationary
- **Quy tắc:** Bác bỏ H0 khi p-value < 0.05.
- **Hành động khi không dừng:** Lấy sai phân bậc 1 (`diff()`) — biến đổi chuỗi từ "giá trị tuyệt đối" thành "tỷ lệ thay đổi".
- **Tại sao bắt buộc:** Mô hình VAR CHỈ hoạt động đúng khi tất cả chuỗi đầu vào đều dừng. Nếu vi phạm, kết quả hồi quy sẽ là "hồi quy giả" - spurious regression.

### 3.3.5 Mô hình VAR - Vector Autoregression

- **Bản chất:** Hệ phương trình đồng thời, trong đó mỗi biến được dự báo bằng giá trị quá khứ - lag, của chính nó và tất cả các biến khác trong hệ thống.
- **Ví dụ:** `CPI_t = f(CPI_{t-1}, GDP_{t-1}, ExchangeRate_{t-1}, LendingRate_{t-1})`
- **Điều kiện tiên quyết:** Tất cả chuỗi phải dừng - stationary.
- **Chọn bậc trễ - Lag Order:** Sử dụng tiêu chuẩn thông tin AIC - Akaike Information Criterion. Giới hạn `maxlags=2` do kích thước mẫu nhỏ - ~25 quan sát sau differencing.
- **Các biến đưa vào VAR - sau khi loại bỏ đa cộng tuyến:**
  - `cpi_growth_percent` — Lạm phát - Target
  - `gdp_growth_percent` — Tăng trưởng kinh tế
  - `lending_interest_percent` — Lãi suất cho vay
  - `officical_exchange_rate_percent` — Tỷ giá hối đoái

### 3.3.6 Kiểm định Nhân quả Granger - Granger Causality Test

- **Câu hỏi:** "Biết giá trị quá khứ của biến X có giúp dự báo CPI tốt hơn so với chỉ dùng giá trị quá khứ của CPI không?"
- **Lưu ý quan trọng:** "X Granger-causes Y" KHÔNG có nghĩa là "X gây ra Y" theo nghĩa nhân quả truyền thống. Đây là khái niệm dự báo - predictive causality, không phải nhân quả cấu trúc.
- **Quy tắc:** p-value < 0.05 → Biến X CÓ tính dẫn dắt - predictive power, đối với CPI.

### 3.3.7 Hàm Phản ứng Xung kích - IRF — Impulse Response Function

- **Mục đích:** Mô phỏng phản ứng của CPI khi một biến khác bị "sốc" 1 độ lệch chuẩn.
- **Đầu ra:** Biểu đồ phản ứng qua 10 kỳ - 10 năm, cho biết:
  - Cú sốc làm tăng hay giảm lạm phát?
  - Tác động kéo dài bao lâu trước khi tắt dần?

### 3.3.8 Phân rã Phương sai Sai số Dự báo - FEVD — Forecast Error Variance Decomposition

- **Mục đích:** Trả lời câu hỏi cốt lõi — "Trong tổng biến động của lạm phát, bao nhiêu % do chính quán tính gây ra, bao nhiêu % do GDP, Tỷ giá, Lãi suất?"
- **Đầu ra:** Bảng và biểu đồ cột chồng cho 10 kỳ dự báo.
- **Ý nghĩa quyết định:**
  - CPI tự giải thích >90% → Quán tính - "Bệnh tự miễn" là chủ đạo.
  - Yếu tố ngoại sinh chiếm >20% → Có thể can thiệp qua chính sách kinh tế.

---

## 3.4 Công cụ và Công nghệ

| Thành phần | Công nghệ |
|:---|:---|
| Ngôn ngữ lập trình | Python 3.9+ |
| Đọc và xử lý dữ liệu | pandas, numpy |
| Kiểm định thống kê & Mô hình chuỗi thời gian | statsmodels - ADF, VAR, Granger, IRF, FEVD |
| Kiểm tra đa cộng tuyến | statsmodels - VIF via `variance_inflation_factor` |
| Trực quan hóa | matplotlib, seaborn |
| Môi trường thực thi | Google Colab / Jupyter Notebook |

---

> *Phần tiếp theo: [4.1. Xác định Mục tiêu và Câu hỏi Chính](./4.1_XacDinhMucTieu.md)*
