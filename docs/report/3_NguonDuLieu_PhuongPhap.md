# 3. Nguồn Dữ liệu và Phương pháp luận

---

## 3.1 Nguồn Dữ liệu

- **File:** `data/dataset_project1.xlsx`
- **Tần suất:** Hàng năm, giai đoạn 1996–2022
- **Nguồn thu thập:** World Bank — World Development Indicators
- **Biến mục tiêu:** `cpi_growth_percent` — Tốc độ tăng chỉ số giá tiêu dùng hàng năm

---

## 3.2 Pipeline Phân tích

Toàn bộ quy trình được thiết kế tối giản, mỗi bước chỉ giữ lại khi trực tiếp phục vụ câu hỏi nghiên cứu.

### Bước 1 — Làm sạch Dữ liệu

- Đọc file Excel bằng pandas.
- Đặt cột `years` làm chỉ mục chuỗi thời gian theo định dạng datetime.
- Đổi tên cột `gdp_delflator_percent` thành `gdp_deflator_index` để tránh nhầm lẫn với growth rate.
- Nội suy tuyến tính cho các giá trị thiếu trong `domestic_credit_index` và `lending_interest_percent`.

### Bước 2 — Chọn Biến VAR

| Biến | Vai trò |
|:---|:---|
| `cpi_growth_percent` | Lạm phát — quán tính tự thân |
| `gdp_growth_percent` | Tác nhân bên ngoài: cầu kéo |
| `lending_interest_percent` | Tác nhân bên ngoài: kênh tiền tệ |
| `officical_exchange_rate_percent` | Tác nhân bên ngoài: tỷ giá |

### Bước 3 — Kiểm định bắt buộc trước Mô hình

- **ADF Test:** Kiểm tra tính dừng cho từng chuỗi. Biến không dừng phải được sai phân trước khi đưa vào VAR.
- **Sai phân bậc 1:** Áp dụng cho các biến không vượt qua ADF.
- **VIF:** Kiểm tra đa cộng tuyến trên bộ 4 biến cuối cùng. Biến có VIF cao cần được xem xét loại bỏ.

### Bước 4 — Mô hình VAR(1) và Phân rã

- Huấn luyện **VAR(1)** để tránh quá khớp với mẫu nhỏ 27 quan sát. Lag bậc 1 cho phép đọc trực tiếp "năm trước ảnh hưởng năm nay".
- Tính **FEVD 10 kỳ** để phân rã tỷ trọng quán tính CPI so với tác động từ GDP, lãi suất, và tỷ giá.
- Kiểm tra phụ qua Granger Causality và IRF để xác nhận chiều tác động.

---

## 3.3 Công cụ Kỹ thuật

- **Ngôn ngữ:** Python
- **Xử lý dữ liệu:** pandas, numpy
- **Mô hình thống kê:** statsmodels
- **Trực quan hóa:** matplotlib, seaborn, plotly
- **Dashboard:** Streamlit

> *Phần tiếp theo: [4.1. Xác định Mục tiêu và Câu hỏi Chính](./4.1_XacDinhMucTieu.md)*
