# Macroeconomic Forecasting Project: Multivariate Analysis

<div align="center">
  <p><strong>BỘ GIÁO DỤC VÀ ĐÀO TẠO</strong></p>
  <p><strong>TRƯỜNG ĐẠI HỌC CÔNG NGHỆ KỸ THUẬT THÀNH PHỐ HỒ CHÍ MINH</strong></p>
  <p><strong>KHOA CÔNG NGHỆ THÔNG TIN</strong></p>
  <br>
  
  <h1><strong>PROJECT 1</strong></h1>
  <h2><strong>PHÂN TÍCH CÁC YẾU TỐ VĨ MÔ TÁC ĐỘNG ĐẾN LẠM PHÁT TẠI VIỆT NAM TỪ NĂM 1996 ĐẾN NĂM 2022 VÀ DỰ BÁO XU HƯỚNG BẰNG MÔ HÌNH CHUỖI THỜI GIAN</strong></h2>
  <br>
</div>

**MÔN HỌC:** PHÂN TÍCH DỮ LIỆU  
**LỚP:** DAAN436277_02  
**GVHD:** ThS. Trần Trọng Bình  

### THÀNH VIÊN NHÓM 02:

| STT | Họ và tên | Mã số sinh viên |
|:---:|:---|:---:|
| 1 | Đỗ Kiến Hưng | 23133030 |
| 2 | Trần Minh Khánh | 23133035 |
| 3 | Nguyễn Đặng Quốc Anh | 23133004 |
| 4 | Phạm Minh Quân | 23133060 |

---

> **THE ULTIMATE QUESTION**
>
> Nhóm tiến hành phân tích dự án nhằm đi tìm lời giải đáp cho vấn đề cốt lõi:
> *"Trong 3 thập kỷ qua, Lạm phát tại Việt Nam chủ yếu là do **'Bệnh tự miễn'** (Quán tính tự sinh ra do tâm lý kỳ vọng) hay do **'Tác nhân bên ngoài'** (Tỷ giá, Tín dụng, Tăng trưởng GDP)? Cần can thiệp vào đâu để kiểm soát nó?"*

## 1. CƠ SỞ KINH TẾ HỌC TRONG VIỆC LỰA CHỌN BIẾN SỐ
Tập dữ liệu 11 biến được nhóm chọn đại diện cho **4 Trụ cột của nền Kinh tế Vĩ mô**:
1. **Trụ cột Giá cả (Đo lường bệnh lý):** `cpi_growth_percent` (Mục tiêu), `gdp_deflator_percent` (Lạm phát từ phía sản xuất).
2. **Trụ cột Tăng trưởng (Áp lực Cầu kéo):** `gdp_growth_percent`, `unemployment_rate` (Đo lường sức khỏe nền kinh tế theo đường cong Phillips).
3. **Trụ cột Tiền tệ (Bơm tiền & Lãi suất):** `domestic_credit_index`, `lending_interest_percent` (Đo lường áp lực từ dòng tiền rẻ).
4. **Trụ cột Đối ngoại (Cú sốc ngoại sinh):** `officical_exchange_rate_percent`, `import_index`, `export_index` (Đo lường độ mở nền kinh tế và áp lực lạm phát nhập khẩu).

## 2. Kiến trúc & Công nghệ (Technology Stack)
- **Data Source:** File Excel gốc chứa dữ liệu vĩ mô Việt Nam (`dataset_project1.xlsx`).
- **Data Processing:** `pandas`, `numpy`, `scipy`.
- **Machine Learning / Time Series Analysis:** `statsmodels` (VAR, ADF Test, VIF, v.v.), `scikit-learn`.
- **Visualization:** `matplotlib`, `seaborn`.

## 3. Cấu trúc thư mục (Repository Structure)
- `data/`: Chứa file `dataset_project1.xlsx`.
- `docs/`: Tài liệu đặc tả kỹ thuật, từ điển dữ liệu (Data Dictionary), và các tài liệu liên quan đến dự án.
- `src/`: Mã nguồn chính của dự án, bao gồm file `Project1_DAAN.ipynb`.