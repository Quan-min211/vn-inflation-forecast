# Nhận xét & Đánh giá Đồ án Phân tích Lạm phát (Version 1)

## 🌟 Ưu điểm

- **Chủ đề thực tiễn & Rõ ràng:** Bài báo cáo tập trung phân tích các yếu tố vĩ mô tác động đến lạm phát tại Việt Nam giai đoạn 1996–2022. Đây là vấn đề cốt lõi của kinh tế vĩ mô, ảnh hưởng trực tiếp đến lãi suất, tỷ giá và ổn định kinh tế.
- **Phạm vi thời gian tốt:** Phân tích suốt 26 năm bao gồm nhiều cú sốc lớn (Khủng hoảng 1997, 2008, WTO, Covid-19), tạo bối cảnh phong phú qua các chu kỳ kinh tế.
- **Insight kinh tế sắc sảo:** 
  - Nhận diện đúng *Tỷ giá* là leading indicator có quan hệ nhân quả một chiều với lạm phát, trong khi lãi suất có độ trễ.
  - Phân tích tốt nhược điểm của công thức tính ICOR, giải thích các đỉnh ICOR 2020-2021 là cú sốc tạm thời thay vì lãng phí dài hạn.
  - Bóc tách thành công áp lực lạm phát, chứng minh tín dụng đã hạ nhiệt so với thập kỷ trước.
  - Chỉ ra quán tính tâm lý đóng vai trò cực lớn (>90%) định hình lạm phát.
- **Tư duy phân tích toàn diện:** 
  - Không chỉ phân tích riêng lẻ CPI mà kết hợp đa biến (GDP, thất nghiệp, lãi suất, tỷ giá, XNK).
  - Kết hợp tốt mô hình VAR (tương tác vĩ mô) và ARIMA (dự báo xu hướng).
- **Kỹ thuật xử lý dữ liệu chuẩn xác:** Áp dụng Linear Interpolation xử lý dữ liệu thiếu, dùng cả ADF và KPSS để chẩn đoán chéo tính dừng.
- **Tính sáng tạo (Future Work):** Đề xuất dùng NLP và Sentiment Analysis để lượng hóa "Tâm lý lạm phát" là hướng đi cực kỳ đột phá.

---

## ⚠️ Nhược điểm & Hạn chế

- **Thiếu minh chứng trực quan:** Đưa ra kết luận mạnh (90.2% quán tính, tỷ giá báo trước lạm phát) nhưng chưa trình bày biểu đồ rõ ràng, dễ hiểu.
- **Quá nặng về thuật ngữ thống kê:** Lạm dụng nhiều thuật ngữ (Shapiro-Wilk, Jarque-Bera, ADF, KPSS, VAR, ARIMA, IRF, FEVD, Spurious Regression), khiến bài viết giống một "pipeline kỹ thuật" hơn là báo cáo insight kinh tế.
- **Sai lầm về nguyên tắc thống kê & Overfitting:**
  - Chạy mô hình đa biến VAR(2) với 11 biến trên tập dữ liệu quá mỏng (27 quan sát/năm) làm giảm nghiêm trọng bậc tự do, dễ dẫn đến quá khớp (overfitting).
  - So sánh RMSE train-fit giữa VAR và ARIMA để kết luận VAR tốt hơn là sai nguyên tắc (đây là in-sample fit, không phải out-of-sample).
- **Hạn chế về tần suất dữ liệu (Năm):** Dữ liệu năm làm "mịn" các biến động ngắn hạn, mô hình khó bắt nhịp các cú sốc thị trường tức thời (như giá xăng dầu, tỷ giá biến động theo tháng).
- **Giới hạn của mô hình tuyến tính:** VAR/ARIMA khó bắt được các điểm gãy vỡ cấu trúc (structural breaks) do cú sốc bất thường (Covid-19, khủng hoảng toàn cầu), làm tăng sai số tại các điểm cực trị.
- **Cách hành văn:** Cần diễn đạt các kết luận (như "90% quán tính") một cách mềm dẻo hơn, tránh sự tuyệt đối hóa gây phản ứng ngược cho người đọc chuyên môn.
