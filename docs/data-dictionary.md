# Data Dictionary
# Vietnam Inflation Forecast Project

This document defines the schema for the macroeconomic dataset used in this project (`dataset_project1.xlsx`).

## 1. Core Dataset Overview

The dataset covers macroeconomic indicators for Vietnam from **1996 to 2022**, with some variables forecasted or updated to 2024. It contains 11 key variables categorized into 4 macroeconomic pillars.

## 2. The 4 Macroeconomic Pillars

### Pillar 1: Prices (Giá cả - Đo lường bệnh lý)
- **`cpi_growth_percent` (Target Variable):** Tỷ lệ tăng trưởng Chỉ số Giá tiêu dùng (CPI). Đại diện trực tiếp cho lạm phát.
- **`cpi_index`:** Chỉ số Giá tiêu dùng gốc.
- **`gdp_deflator_percent`:** Chỉ số giảm phát GDP (%). Đo lường lạm phát từ phía sản xuất và toàn bộ nền kinh tế (không chỉ giới hạn ở giỏ hàng hóa tiêu dùng).

### Pillar 2: Growth (Tăng trưởng - Áp lực Cầu kéo)
- **`gdp_growth_percent`:** Tốc độ tăng trưởng GDP (%).
- **`unemployment_rate`:** Tỷ lệ thất nghiệp (%). Được sử dụng để kiểm chứng mối quan hệ đánh đổi giữa lạm phát và thất nghiệp (Đường cong Phillips).

### Pillar 3: Monetary (Tiền tệ - Bơm tiền & Lãi suất)
- **`domestic_credit_index`:** Tín dụng nội địa. Đại diện cho mức độ cung tiền và khả năng vay vốn trong nền kinh tế.
- **`lending_interest_percent`:** Lãi suất cho vay (%). Chi phí vốn, ảnh hưởng trực tiếp đến đầu tư và tiêu dùng.

### Pillar 4: Foreign Affairs (Đối ngoại - Cú sốc ngoại sinh)
- **`officical_exchange_rate_percent`:** Tỷ giá hối đoái chính thức (VND/USD). Đo lường sức mạnh đồng nội tệ và áp lực lạm phát nhập khẩu.
- **`import_index`:** Chỉ số nhập khẩu.
- **`export_index`:** Chỉ số xuất khẩu.

## 3. Time Index
- **`years`:** Cột thời gian (Index) theo năm, định dạng `YYYY` (1996, 1997, ..., 2024). Dữ liệu là dữ liệu theo năm (Annual Data).

## 4. Missing Values & Data Quality Rules
- **Rule DQ-01:** `domestic_credit_index` and `lending_interest_percent` contain a small number of null values which must be imputed (e.g., using linear interpolation or forward-fill) before modeling.
- **Rule DQ-02:** All percentage and index columns must be stored as `float64`.
- **Rule DQ-03:** The `years` column must be set as the pandas DataFrame Index for Time Series analysis.
