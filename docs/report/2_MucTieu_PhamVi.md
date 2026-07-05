# 2. MỤC TIÊU VÀ PHẠM VI - OBJECTIVE AND SCOPE

---

## 2.1 Câu hỏi Nghiên cứu Chính - The Ultimate Question

Dự án được xây dựng xoay quanh một câu hỏi duy nhất, mang tính quyết định đối với việc hoạch định chính sách kinh tế vĩ mô của Việt Nam:

> *"Trong 3 thập kỷ qua, Lạm phát tại Việt Nam chủ yếu là do **'Bệnh tự miễn'** - Quán tính tự sinh ra do tâm lý kỳ vọng, hay do **'Tác nhân bên ngoài'** - Tỷ giá, Tín dụng, Tăng trưởng GDP? Cần can thiệp vào đâu để kiểm soát nó?"*

Câu hỏi này được cụ thể hóa thành hai giả thuyết có thể kiểm chứng bằng định lượng:

| Giả thuyết | Mô tả | Công cụ kiểm chứng |
|:---|:---|:---|
| **H1: "Bệnh tự miễn"** | Lạm phát VN chủ yếu do quán tính nội sinh — kỳ vọng tâm lý của dân chúng và doanh nghiệp tạo ra vòng lặp tự củng cố. | FEVD: CPI tự giải thích >80% phương sai của chính nó. |
| **H2: "Tác nhân bên ngoài"** | Lạm phát VN chủ yếu do các yếu tố kinh tế vĩ mô bên ngoài (tỷ giá, tín dụng, GDP) chi phối. | FEVD: Các biến ngoại sinh giải thích >20% phương sai CPI; Granger Causality có ý nghĩa thống kê. |

---

## 2.2 Cơ sở Kinh tế học trong Lựa chọn Biến số

Tập dữ liệu 11 biến được lựa chọn dựa trên nền tảng lý thuyết kinh tế vĩ mô, đại diện cho **4 Trụ cột của nền Kinh tế Vĩ mô**. Mỗi trụ cột đại diện cho một kênh truyền dẫn lạm phát khác nhau:

### Trụ cột 1: Giá cả - Đo lường bệnh lý
- **Biến số:** `cpi_growth_percent` - Biến mục tiêu — Target, `gdp_deflator_percent`
- **Lý do chọn:** CPI đo lường giá cả từ phía tiêu dùng (giỏ hàng hóa hộ gia đình), còn GDP Deflator đo từ phía sản xuất. Khi cả hai cùng tăng, ta xác nhận lạm phát là "thật" chứ không phải do một sự kiện cục bộ.

### Trụ cột 2: Tăng trưởng - Áp lực Cầu kéo — Demand-pull
- **Biến số:** `gdp_growth_percent`, `unemployment_rate`
- **Lý do chọn:** Theo lý thuyết Đường cong Phillips, khi GDP tăng nhanh → thất nghiệp giảm → áp lực tăng lương → giá cả tăng. Đây là kênh "Cầu kéo" - Demand-pull của lạm phát.

### Trụ cột 3: Tiền tệ - Bơm tiền & Lãi suất — Monetary channel
- **Biến số:** `domestic_credit_index`, `lending_interest_percent`
- **Lý do chọn:** Khi tín dụng mở rộng - bơm tiền, và lãi suất giảm → doanh nghiệp và người dân vay nhiều hơn → lượng tiền trong nền kinh tế tăng → giá cả tăng. Đây là kênh "Tiền tệ" - Monetary channel.

### Trụ cột 4: Đối ngoại - Cú sốc ngoại sinh — Cost-push
- **Biến số:** `officical_exchange_rate_percent`, `import_index`, `export_index`
- **Lý do chọn:** Khi VND mất giá so với USD → hàng nhập khẩu - xăng dầu, nguyên liệu, đắt hơn → chi phí sản xuất tăng → giá cả tăng. Đây là kênh "Chi phí đẩy" - Cost-push từ bên ngoài.

---

## 2.3 Phạm vi Dữ liệu và Phân tích

| Tiêu chí | Chi tiết |
|:---|:---|
| **Phạm vi thời gian** | 1996 – 2022 - 27 năm quan sát |
| **Tần suất dữ liệu** | Hàng năm - Annual |
| **Nguồn dữ liệu** | World Bank — World Development Indicators - WDI |
| **Số lượng biến** | 11 biến - bao gồm cả biến index tích lũy và biến growth rate |
| **Biến mục tiêu** | `cpi_growth_percent` — Tốc độ tăng chỉ số giá tiêu dùng - % |
| **Đối tượng phân tích** | Nền kinh tế Việt Nam |
| **Loại phân tích** | Dự đoán - Predictive — Dự báo xu hướng lạm phát và xác định yếu tố chi phối |

### Bảng Tổng hợp 11 Biến số

| STT | Tên biến | Mô tả | Trụ cột |
|:---:|:---|:---|:---|
| 1 | `cpi_index` | Chỉ số giá tiêu dùng - Index tích lũy | Giá cả |
| 2 | `cpi_growth_percent` | Tốc độ tăng CPI hàng năm - % — **TARGET** | Giá cả |
| 3 | `gdp_deflator_percent` | Tốc độ tăng GDP Deflator - % | Giá cả |
| 4 | `gdp_delflator_percent` | GDP Deflator Index - tích lũy — *lỗi chính tả gốc* | Giá cả |
| 5 | `gdp_growth_percent` | Tốc độ tăng trưởng GDP thực - % | Tăng trưởng |
| 6 | `unemployment_rate` | Tỷ lệ thất nghiệp - % | Tăng trưởng |
| 7 | `domestic_credit_index` | Chỉ số tín dụng nội địa - Index | Tiền tệ |
| 8 | `lending_interest_percent` | Lãi suất cho vay - % | Tiền tệ |
| 9 | `officical_exchange_rate_percent` | Tỷ giá hối đoái chính thức - Index | Đối ngoại |
| 10 | `import_index` | Chỉ số giá trị nhập khẩu - Index | Đối ngoại |
| 11 | `export_index` | Chỉ số giá trị xuất khẩu - Index | Đối ngoại |

---

> *Phần tiếp theo: [3. Nguồn Dữ liệu và Phương pháp luận](./3_NguonDuLieu_PhuongPhap.md)*
