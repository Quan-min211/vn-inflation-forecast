# 2. MỤC TIÊU VÀ PHẠM VI

---

## 2.1 Câu hỏi Nghiên cứu Chính

Dự án được xây dựng xoay quanh một câu hỏi duy nhất, mang tính quyết định đối với việc hoạch định chính sách kinh tế vĩ mô của Việt Nam:

> *"Trong 3 thập kỷ qua, Lạm phát tại Việt Nam chủ yếu là do **'Bệnh tự miễn'** — quán tính tự sinh ra do tâm lý kỳ vọng, hay do **'Tác nhân bên ngoài'** — Tỷ giá, Lãi suất, Tăng trưởng GDP? Cần can thiệp vào đâu để kiểm soát nó?"*

Câu hỏi này được cụ thể hóa thành hai giả thuyết có thể kiểm chứng bằng định lượng:

| Giả thuyết | Mô tả | Công cụ kiểm chứng |
|:---|:---|:---|
| **H1 — "Bệnh tự miễn"** | Lạm phát VN chủ yếu do quán tính nội sinh, kỳ vọng tâm lý của dân chúng và doanh nghiệp tạo ra vòng lặp tự củng cố. | FEVD: CPI tự giải thích trên 80% phương sai của chính nó. |
| **H2 — "Tác nhân bên ngoài"** | Lạm phát VN chủ yếu do các yếu tố kinh tế vĩ mô bên ngoài chi phối. | FEVD: Các biến ngoại sinh giải thích trên 20% phương sai CPI; Granger Causality có ý nghĩa thống kê. |

---

## 2.2 Bốn Biến được Chọn cho Mô hình VAR

Từ tập dữ liệu 11 biến, phiên bản phân tích này giữ lại **4 biến** đại diện trực tiếp cho câu hỏi nghiên cứu. Tiêu chí lựa chọn: mỗi biến phải đại diện cho một kênh truyền dẫn lạm phát khác nhau và không gây quá khớp do số quan sát nhỏ.

| Biến | Kênh truyền dẫn | Vai trò trong VAR |
|:---|:---|:---|
| `cpi_growth_percent` | Lạm phát — biến đo mức độ bệnh lý | Biến mục tiêu |
| `gdp_growth_percent` | Cầu kéo — áp lực từ tăng trưởng kinh tế | Tác nhân bên ngoài |
| `lending_interest_percent` | Tiền tệ — kênh lãi suất và tín dụng | Tác nhân bên ngoài |
| `officical_exchange_rate_percent` | Đối ngoại — cú sốc chi phí đẩy từ tỷ giá | Tác nhân bên ngoài |

> **Lý do rút gọn còn 4 biến:** Với mẫu dữ liệu chỉ 27 năm, một mô hình VAR nhiều biến sẽ cạn kiệt bậc tự do và dẫn đến quá khớp. Bốn biến được chọn là đại diện tối thiểu và đủ mạnh để trả lời câu hỏi quán tính hay tác nhân bên ngoài.

---

## 2.3 Phạm vi Dữ liệu

| Tiêu chí | Chi tiết |
|:---|:---|
| Phạm vi thời gian | 1996–2022, tương đương 27 năm quan sát |
| Tần suất dữ liệu | Hàng năm |
| Nguồn dữ liệu | World Bank — World Development Indicators |
| Biến mục tiêu | `cpi_growth_percent` — Tốc độ tăng chỉ số giá tiêu dùng |
| Loại phân tích | Phân tách nguyên nhân — Variance Decomposition |

---

## 2.4 Phạm vi Giới hạn

Để đảm bảo tính khả thi và chất lượng học thuật, dự án xác lập các giới hạn sau:

- Không xây dựng mô hình dự báo điểm cho CPI trong tương lai. Mục tiêu chính là phân tách nguyên nhân, không phải dự báo giá trị cụ thể.
- Không sử dụng mô hình phi tuyến như neural network hay regime-switching trong phiên bản này.
- Không phân tích ở tần suất tháng hoặc quý do giới hạn từ nguồn dữ liệu World Bank.

> *Phần tiếp theo: [3. Nguồn Dữ liệu và Phương pháp luận](./3_NguonDuLieu_PhuongPhap.md)*
