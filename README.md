# Macroeconomic Forecasting Project: Multivariate Analysis

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B.svg?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626.svg?logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Statsmodels-Time_Series-orange.svg" alt="Statsmodels">
</div>

<div align="center">
  <p><strong>BỘ GIÁO DỤC VÀ ĐÀO TẠO</strong></p>
  <p><strong>TRƯỜNG ĐẠI HỌC CÔNG NGHỆ KỸ THUẬT THÀNH PHỐ HỒ CHÍ MINH (HCMUTE)</strong></p>
  <p><strong>KHOA CÔNG NGHỆ THÔNG TIN</strong></p>
  <br>
  
  <h2><strong>PROJECT 1</strong></h2>
  <h3><strong>PHÂN TÍCH CÁC YẾU TỐ VĨ MÔ TÁC ĐỘNG ĐẾN LẠM PHÁT TẠI VIỆT NAM TỪ NĂM 1996 ĐẾN NĂM 2022 VÀ DỰ BÁO XU HƯỚNG BẰNG MÔ HÌNH CHUỖI THỜI GIAN</strong></h3>
  <br>
</div>

---

## 1. Giới thiệu Dự án (About The Project)

Dự án này ứng dụng phương pháp Phân tích Chuỗi thời gian Đa biến (Multivariate Time Series Analysis) nhằm mổ xẻ nguyên nhân lạm phát tại Việt Nam giai đoạn 1996-2022. Thay vì dự báo điểm đơn thuần, dự án tập trung vào **suy luận cấu trúc (Structural Inference)** để giúp các nhà hoạch định chính sách hiểu rõ kênh truyền dẫn lạm phát thông qua mô hình Vector Autoregression (VAR).

Dự án đi kèm một **Interactive Streamlit Dashboard** để trực quan hóa dữ liệu vĩ mô, các bài kiểm định thống kê và kết quả mô hình theo thời gian thực.

### Câu hỏi Nghiên cứu Cốt lõi (The Ultimate Question)
> *"Trong 3 thập kỷ qua, Lạm phát tại Việt Nam chủ yếu là do **'Bệnh tự miễn'** - Quán tính tự sinh ra do tâm lý kỳ vọng, hay do **'Tác nhân bên ngoài'** - Tỷ giá, Tín dụng, Tăng trưởng GDP? Cần can thiệp vào đâu để kiểm soát nó?"*

---

## 2. Tính năng Cốt lõi (Key Features)

- **Data Exploration (EDA):** Xử lý dữ liệu khuyết thiếu bằng nội suy tuyến tính (Linear Interpolation) và trực quan hóa 4 trụ cột vĩ mô.
- **Diagnostic Testing:** Đảm bảo độ tin cậy của mô hình thông qua kiểm định đa cộng tuyến (VIF) và kiểm định tính dừng (ADF Test).
- **VAR Modeling:** Xây dựng hệ phương trình đồng thời (Vector Autoregression) để tìm ra mối liên hệ động giữa các biến vĩ mô.
- **Causality & Impact Analysis:** Lượng hóa tác động bằng Kiểm định Nhân quả (Granger Causality), Hàm Phản ứng Xung kích (IRF) và Phân rã Phương sai (FEVD).

---

## 3. Cấu trúc Thư mục (Repository Structure)

```text
vn-inflation-forecast/
├── data/
│   └── dataset_project1.xlsx          # Dữ liệu vĩ mô thô (World Bank)
├── docs/
│   ├── ref/                           # Tài liệu tham khảo & Báo cáo PDF
│   └── report/                        # Báo cáo chi tiết định dạng Markdown (Chương 1-4)
├── src/
│   ├── Project1_DAAN.ipynb            # Version 1: EDA cơ bản & Baseline Model
│   ├── Project1_DAAN_v2.ipynb         # Version 2: Pipeline Time Series chuyên sâu
│   └── dashboard/                     # Web App (Streamlit)
│       ├── Home.py                    # App Entry Point
│       └── pages/                     # Phân hệ Dashboard (EDA, VAR, IRF, v.v.)
└── README.md                          # Tổng quan dự án
```

---

## 4. Hướng dẫn Cài đặt và Chạy Dự án (Installation & Usage)

Để chạy dự án và mở Dashboard trực quan hóa trên máy tính cá nhân, vui lòng thực hiện các bước sau:

### Bước 1: Clone Repository và Di chuyển vào thư mục dự án
```bash
git clone https://github.com/Quan-min211/vn-inflation-forecast.git
cd vn-inflation-forecast
```

### Bước 2: Cài đặt các thư viện phụ thuộc
Đảm bảo bạn đã cài đặt Python 3.9 trở lên. Chạy lệnh sau để cài đặt các thư viện cần thiết:
```bash
pip install pandas numpy scipy statsmodels scikit-learn matplotlib seaborn streamlit openpyxl
```

### Bước 3: Khởi chạy Streamlit Dashboard (Giao diện Web)
Dashboard là sản phẩm đầu cuối giúp tương tác trực quan với dữ liệu và mô hình. Chạy lệnh sau trong terminal:
```bash
python -m streamlit run src/dashboard/Home.py
```
*Sau khi chạy lệnh, trình duyệt sẽ tự động mở trang Dashboard tại địa chỉ `http://localhost:8501`.*

### Bước 4: Xem và Chạy Notebook Phân tích (Tùy chọn)
Nếu muốn xem chi tiết mã nguồn phân tích toán học và thống kê, hãy mở file Jupyter Notebook:
```bash
jupyter notebook src/Project1_DAAN_v2.ipynb
```

---

## 5. Kết quả Nổi bật (Key Findings)

Dựa trên kết quả từ mô hình VAR và kỹ thuật phân rã phương sai (FEVD), nhóm nghiên cứu rút ra các kết luận chính:
- **>90% biến động CPI** được giải thích bởi chính nó trong quá khứ, khẳng định quán tính lạm phát (kỳ vọng lạm phát) là yếu tố áp đảo tại Việt Nam.
- Các cú sốc ngoại sinh từ tỷ giá hay tăng trưởng tín dụng có tác động lan truyền đến lạm phát, nhưng ảnh hưởng này suy yếu rất nhanh (theo kết quả từ Hàm phản ứng xung kích IRF).
- Lãi suất cho vay tại Việt Nam mang tính **phản ứng** chính sách nhiều hơn là nguyên nhân gốc rễ gây ra lạm phát (theo kiểm định Granger Causality).

---

## 6. Thành viên Nhóm 02 (Contributors)

**Môn học:** Phân tích Dữ liệu | **Lớp:** DAAN436277_02 | **GVHD:** ThS. Trần Trọng Bình

| Tên thành viên | Mã số Sinh viên | Vai trò |
|:---|:---:|:---|
| **Đỗ Kiến Hưng** | 23133030 | Data Cleaning, Modeling |
| **Trần Minh Khánh** | 23133035 | EDA, Visualization |
| **Nguyễn Đặng Quốc Anh** | 23133004 | Statistical Testing |
| **Phạm Minh Quân** | 23133060 | Dashboard Development |