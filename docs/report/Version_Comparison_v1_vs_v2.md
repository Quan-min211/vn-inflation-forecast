# So sánh Phiên bản V1 và V2

---

## Định hướng Thay đổi

Phiên bản V2 giữ lại ý tưởng cốt lõi của V1 — sử dụng VAR và FEVD để trả lời câu hỏi quán tính hay tác nhân bên ngoài — nhưng loại bỏ toàn bộ các phần phân tích rộng không trực tiếp phục vụ kết luận.

---

## Bảng So sánh Chi tiết

| Hạng mục | Phiên bản V1 | Phiên bản V2 |
|:---|:---|:---|
| **Câu hỏi nghiên cứu** | Có nhưng lẫn vào nhiều phần phân tích | Là trọng tâm duy nhất, xuyên suốt toàn bộ notebook và dashboard |
| **Số biến đưa vào VAR** | 11 biến — dẫn đến cạn bậc tự do với mẫu 27 quan sát | 4 biến tinh túy: CPI, GDP, Lãi suất, Tỷ giá |
| **Bậc lag VAR** | VAR(2) — quá khớp với mẫu nhỏ | VAR(1) — gọn, phù hợp và không tiêu tốn bậc tự do |
| **Phần EDA rộng** | Histogram, Boxplot, Q-Q Plot cho nhiều biến | Đã loại bỏ — chỉ giữ 4 chuỗi thời gian phục vụ câu hỏi |
| **Đường cong Phillips** | Có — OLS regression CPI ~ Thất nghiệp | Đã loại bỏ — không phục vụ trực tiếp VAR |
| **Mô hình ARIMA** | Có — chạy song song với VAR | Đã loại bỏ — và so sánh RMSE train-fit giữa ARIMA và VAR là sai nguyên tắc out-of-sample |
| **Correlation Heatmap** | Có — chương riêng | Đã loại bỏ khỏi luồng chính notebook |
| **FEVD** | Có nhưng đôi khi ít kỳ, vai trò chưa rõ | Giữ đủ 10 kỳ, là bằng chứng trung tâm |
| **Dashboard** | Nhiều panel giải thích rộng | Verdict-first — 4 trang tối giản, mỗi trang phục vụ một bước trong pipeline |
| **Kết luận** | Đề cập ARIMA, FEVD, nhiều chỉ số | Chỉ dựa vào FEVD 10 kỳ và Granger làm bằng chứng chính |

---

## Lý do Loại bỏ ARIMA

So sánh RMSE train-fit giữa VAR và ARIMA để kết luận VAR vượt trội là sai về nguyên tắc thống kê — đây là in-sample fit, không phải out-of-sample evaluation. Thay vào đó, V2 dùng FEVD để định lượng trực tiếp tỷ trọng quán tính ngay trong khuôn khổ VAR, giải quyết câu hỏi nghiên cứu mà không cần so sánh hai mô hình.

---

## Lý do Rút gọn còn 4 Biến

Với 27 quan sát, một mô hình VAR(2) đầy đủ 11 biến tiêu tốn phần lớn bậc tự do, làm giảm độ tin cậy của từng hệ số. Bốn biến được giữ lại là đại diện tối thiểu đủ mạnh cho câu hỏi: **CPI, GDP, Lãi suất, Tỷ giá** — mỗi biến một kênh truyền dẫn, không trùng lặp.

---

## Kết quả Sau Thay đổi

Notebook, Dashboard, và các tài liệu đều hội tụ về một kết luận duy nhất:

> Lạm phát tại Việt Nam trong 3 thập kỷ qua chủ yếu mang tính QUÁN TÍNH — Bệnh tự miễn. Bằng chứng: FEVD 10 kỳ cho thấy CPI tự giải thích phần lớn phương sai của chính nó, trong khi GDP, Lãi suất, Tỷ giá đóng góp tỷ trọng nhỏ hơn rõ rệt.
