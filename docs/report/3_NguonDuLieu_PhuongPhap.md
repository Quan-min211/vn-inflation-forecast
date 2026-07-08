# 3. Nguồn Dữ liệu và Phương pháp luận

## Nguồn dữ liệu

- File: `data/dataset_project1.xlsx`
- Tần suất: hằng năm
- Đối tượng: kinh tế Việt Nam
- Biến mục tiêu: `cpi_growth_percent`

## Phương pháp tối giản

Đồ án chỉ giữ các bước cần thiết để trả lời câu hỏi quán tính hay tác nhân bên ngoài.

### 1. Làm sạch dữ liệu

- Đọc Excel bằng pandas.
- Đặt `years` làm chỉ mục thời gian.
- Đổi `gdp_delflator_percent` thành `gdp_deflator_index`.
- Nội suy tuyến tính missing values.

### 2. Chọn biến VAR

| Biến | Vai trò |
|---|---|
| `cpi_growth_percent` | Lạm phát / quán tính tự thân |
| `gdp_growth_percent` | Tác nhân bên ngoài: cầu kéo |
| `lending_interest_percent` | Tác nhân bên ngoài: tiền tệ |
| `officical_exchange_rate_percent` | Tác nhân bên ngoài: tỷ giá |

### 3. Kiểm định trước mô hình

- ADF để kiểm tra tính dừng.
- Sai phân biến không dừng.
- VIF để kiểm tra đa cộng tuyến trên bộ biến cuối cùng.

### 4. Mô hình

- Huấn luyện **VAR(1)** để tránh quá khớp với mẫu nhỏ.
- Dự báo ngắn hạn như kiểm tra sanity.
- Tính **FEVD 10 kỳ** để phân rã tỷ trọng quán tính và tác nhân bên ngoài.

## Công cụ

- Python
- pandas, numpy
- statsmodels
- matplotlib, seaborn
- Streamlit
