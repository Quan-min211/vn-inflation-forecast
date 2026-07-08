# Báo cáo phiên bản tối giản

## Câu hỏi nghiên cứu

> Lạm phát tại Việt Nam chủ yếu là do "Bệnh tự miễn" (quán tính) hay do "Tác nhân bên ngoài"?

## Câu trả lời dựa trên dữ liệu

> **Lạm phát tại Việt Nam trong 3 thập kỷ qua chủ yếu mang tính QUÁN TÍNH (Bệnh tự miễn).**

## Pipeline

1. Đọc `dataset_project1.xlsx`.
2. Làm sạch dữ liệu, xử lý missing bằng nội suy tuyến tính.
3. Giữ bốn biến phục vụ trực tiếp câu hỏi:
   - CPI growth
   - GDP growth
   - lending interest
   - exchange rate
4. Kiểm định ADF, sai phân biến không dừng.
5. Kiểm tra VIF.
6. Huấn luyện VAR(1).
7. Tính FEVD 10 kỳ.

## Bằng chứng chính

FEVD 10 kỳ là phần trung tâm của báo cáo. Nếu CPI tự giải thích phần lớn sai số dự báo, kết luận là lạm phát có tính quán tính. Các biến bên ngoài chỉ được xem là tác nhân phụ khi tỷ trọng đóng góp của chúng nhỏ hơn rõ rệt.

## Kết luận chính sách

- Chính sách kiểm soát lạm phát nên ưu tiên neo kỳ vọng.
- Truyền thông chính sách cần minh bạch để giảm vòng lặp kỳ vọng giá tăng.
- GDP, lãi suất và tỷ giá vẫn cần theo dõi, nhưng không phải trọng tâm giải thích sự kéo dài của lạm phát trong mô hình này.
