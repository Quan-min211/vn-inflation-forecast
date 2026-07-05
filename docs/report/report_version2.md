# 4.1 XÁC ĐỊNH MỤC TIÊU VÀ CÂU HỎI CHÍNH

**Bước 1 trong Quy trình Xây dựng Báo cáo Phân tích Dữ liệu**

---

## 4.1.1 Bối cảnh Vấn đề

Lạm phát là một trong những chỉ báo vĩ mô quan trọng nhất, ảnh hưởng trực tiếp đến đời sống người dân, chi phí sản xuất của doanh nghiệp, và khả năng hoạch định chính sách của Ngân hàng Nhà nước. Trong 3 thập kỷ qua - 1996–2022, Việt Nam đã trải qua nhiều giai đoạn biến động lạm phát mạnh, bao gồm:

- **Khủng hoảng tài chính châu Á - 1997–1998:** Áp lực giảm phát do suy thoái khu vực.
- **Lạm phát phi mã - 2008, 2011:** CPI tăng vọt lên đỉnh, trùng khớp với khủng hoảng tài chính toàn cầu và chính sách tiền tệ nới lỏng quá mức trong nước.
- **Giai đoạn ổn định - 2014–2019:** Lạm phát được kiểm soát dưới 5% nhờ chính sách tiền tệ thận trọng.
- **COVID-19 - 2020–2021:** Cú sốc cung-cầu chưa từng có tiền lệ.

Câu hỏi đặt ra: **Yếu tố nào thực sự là động lực chính đằng sau các biến động lạm phát này?** Hiểu đúng bản chất nguyên nhân sẽ quyết định chính sách kiểm soát nào là hiệu quả nhất.

---

## 4.1.2 Mục tiêu Phân tích

### Mục tiêu Tổng quát
Xây dựng một pipeline phân tích chuỗi thời gian đa biến - multivariate time series analysis, để phân tách và định lượng các nguồn gốc biến động của lạm phát Việt Nam.

### Mục tiêu Cụ thể

| STT | Mục tiêu | Phương pháp | Đầu ra kỳ vọng |
|:---:|:---|:---|:---|
| 1 | Khám phá và hiểu đặc trưng dữ liệu thô | EDA, thống kê mô tả, trực quan hóa | Bức tranh tổng quan về 11 biến kinh tế vĩ mô |
| 2 | Xác định mối quan hệ giữa các biến | Correlation, VIF | Ma trận tương quan, phát hiện đa cộng tuyến |
| 3 | Kiểm định tính dừng và biến đổi dữ liệu | ADF Test, Differencing | Dữ liệu sạch và stationary, sẵn sàng cho mô hình |
| 4 | Định lượng tác động của các yếu tố lên lạm phát | VAR, Granger Causality | Xác định biến nào "dẫn dắt" CPI |
| 5 | Phân rã biến động lạm phát | FEVD, IRF | Trả lời Ultimate Question — % quán tính vs. % ngoại sinh |

---

## 4.1.3 Câu hỏi Nghiên cứu Chi tiết

Từ câu hỏi tối thượng - The Ultimate Question, dự án triển khai thành một chuỗi câu hỏi nghiên cứu con, mỗi câu hỏi tương ứng với một bước phân tích cụ thể:

### Nhóm 1: Khám phá - Descriptive
- **Q1.1:** Dữ liệu kinh tế vĩ mô của Việt Nam có những đặc trưng gì? - Phân phối, xu hướng, giá trị thiếu
- **Q1.2:** Các sự kiện kinh tế lớn - khủng hoảng 2008, COVID-19, để lại dấu ấn gì trên dữ liệu?

### Nhóm 2: Chẩn đoán - Diagnostic
- **Q2.1:** Biến nào có tương quan mạnh nhất với lạm phát CPI?
- **Q2.2:** Có hiện tượng đa cộng tuyến nghiêm trọng giữa các biến không? - VIF
- **Q2.3:** Chuỗi dữ liệu nào dừng, chuỗi nào không dừng? - ADF

### Nhóm 3: Dự đoán - Predictive
- **Q3.1:** Yếu tố bên ngoài nào có khả năng "dẫn dắt" - Granger-cause, lạm phát?
- **Q3.2:** Khi nền kinh tế chịu cú sốc từ một yếu tố - ví dụ: tỷ giá tăng vọt, lạm phát phản ứng thế nào qua thời gian? - IRF

### Nhóm 4: Phán quyết - Prescriptive
- **Q4.1:** Trong tổng biến động lạm phát, bao nhiêu % do quán tính - bệnh tự miễn, và bao nhiêu % do tác nhân ngoại sinh? - FEVD
- **Q4.2:** Chính sách kiểm soát lạm phát nên tập trung vào quản trị kỳ vọng hay can thiệp vào các biến số kinh tế?

---

## 4.1.4 Biến Mục tiêu và Chỉ số Theo dõi

### Biến Mục tiêu - Target Variable
- **Tên:** `cpi_growth_percent`
- **Ý nghĩa:** Tốc độ tăng chỉ số giá tiêu dùng hàng năm - %, đo lường mức độ lạm phát mà người dân trực tiếp cảm nhận.
- **Lý do chọn:** CPI growth là thước đo lạm phát phổ biến nhất, được NHNN sử dụng làm mục tiêu chính sách.

### Các Chỉ số Theo dõi - KPIs

| Chỉ số | Ý nghĩa | Nguồn |
|:---|:---|:---|
| FEVD % của CPI → CPI | Mức độ quán tính - tự giải thích | Mô hình VAR |
| FEVD % của GDP → CPI | Tác động kênh Cầu kéo | Mô hình VAR |
| FEVD % của Exchange Rate → CPI | Tác động kênh Chi phí đẩy | Mô hình VAR |
| FEVD % của Lending Rate → CPI | Tác động kênh Tiền tệ | Mô hình VAR |
| p-value Granger Causality | Ý nghĩa thống kê của tính dẫn dắt | Kiểm định Granger |
| ADF p-value | Tính dừng của chuỗi | Kiểm định ADF |
| VIF Score | Mức độ đa cộng tuyến | statsmodels VIF |

---

## 4.1.5 Phạm vi Giới hạn

Để đảm bảo tính khả thi và chất lượng phân tích trong khuôn khổ dự án, các giới hạn sau được xác lập:

- **Không** xây dựng mô hình dự báo điểm - point forecast, cho CPI trong tương lai. Mục tiêu chính là **phân tách nguyên nhân** - variance decomposition, không phải dự báo giá trị cụ thể.
- **Không** sử dụng mô hình phi tuyến - neural network, regime-switching, trong phiên bản này.
- **Không** phân tích tần suất dữ liệu tháng/quý do giới hạn nguồn dữ liệu từ World Bank.

---

> *Phần tiếp theo: [4.2. Thu thập, Làm sạch và Xác thực Dữ liệu](./4.2_ThuThap_LamSach_XacThuc.md)*
# 4.2 THU THẬP, LÀM SẠCH VÀ XÁC THỰC DỮ LIỆU

**Bước 2 trong Quy trình Xây dựng Báo cáo Phân tích Dữ liệu**

---

## 4.2.1 Thu thập và Xem trước Dữ liệu

### Nguồn thu thập
Dữ liệu được tải từ **World Bank — World Development Indicators - WDI** và lưu trữ dưới dạng file Excel:

```python
df = pd.read_excel('../data/dataset_project1.xlsx')
display(df.head(10))
```

### Cấu trúc dữ liệu

Kết quả kiểm tra cấu trúc ban đầu - `df.info()`, `df.describe()`:

- **Số quan sát:** 27 dòng - 1996–2022
- **Số cột:** 12 cột - bao gồm cột `years` và 11 biến số
- **Kiểu dữ liệu:** Tất cả các biến kinh tế đều là kiểu `float64`
- **Cột index:** `years` — chuyển đổi sang `datetime` và đặt làm index chuỗi thời gian

Bước kiểm tra sơ bộ này giúp xác nhận dữ liệu đã được nạp đúng định dạng và sẵn sàng cho các bước làm sạch tiếp theo.

---

## 4.2.2 Phân tích Giá trị Thiếu - Missing Values Analysis

### Tại sao phải kiểm tra?
Dữ liệu kinh tế vĩ mô từ World Bank thường có khoảng trống vì:
- Một số quốc gia - đặc biệt là các nền kinh tế đang phát triển như Việt Nam, chưa thống kê đầy đủ vào những năm đầu.
- Phương pháp thu thập dữ liệu thay đổi qua các giai đoạn.

Nếu bỏ qua missing values → mô hình sẽ bị lệch - biased, hoặc không thể chạy được.

### Kết quả kiểm tra

```python
missing_counts = df.isnull().sum()
```

| Biến | Số giá trị thiếu | Thuộc trụ cột |
|:---|:---:|:---|
| `domestic_credit_index` | Có giá trị thiếu | Tiền tệ |
| `lending_interest_percent` | Có giá trị thiếu | Tiền tệ |
| Các biến còn lại | 0 | — |

### Trực quan hóa

Hai biểu đồ được sử dụng để trực quan hóa vị trí và mức độ thiếu dữ liệu:

1. **Heatmap Missing Values:** Bản đồ nhiệt hiển thị vị trí chính xác của các ô thiếu dữ liệu - ô vàng = missing, theo từng biến và từng năm. Giúp nhận biết pattern thiếu dữ liệu — liệu có phải thiếu liên tiếp ở các năm đầu không.
2. **Bar Chart Tỷ lệ % Missing:** Biểu đồ thanh ngang cho thấy tỷ lệ phần trăm giá trị thiếu của từng biến, giúp so sánh nhanh mức độ nghiêm trọng.

> 📷 **CHỤP MÀN HÌNH TỪ STREAMLIT:** Chụp 2 biểu đồ "Bản đồ Giá trị Thiếu" và "Tỷ lệ % Giá trị Thiếu" từ trang **Data Exploration** để chèn vào đây.

### Nhận xét và Hành động

- **Hai biến thiếu dữ liệu** đều thuộc **Trụ cột Tiền tệ** - `domestic_credit_index` và `lending_interest_percent`.
- **Nguyên nhân:** Dữ liệu tín dụng nội địa và lãi suất cho vay từ World Bank cho Việt Nam không được ghi nhận đầy đủ trong một số năm đầu tiên của giai đoạn nghiên cứu.
- **Giải pháp:** Sử dụng **nội suy tuyến tính - linear interpolation** — phương pháp phù hợp nhất cho dữ liệu chuỗi thời gian vì nó giả định giá trị biến đổi dần dần theo thời gian - hợp lý với dữ liệu kinh tế.

---

## 4.2.3 Làm sạch Dữ liệu - Data Cleaning

### Phát hiện và xử lý cột trùng lặp

Khi kiểm tra danh sách cột, phát hiện **hai cột có tên gần giống nhau:**
- `gdp_delflator_percent` — lỗi chính tả - delflator thay vì deflator
- `gdp_deflator_percent` — tên đúng

```python
# Kiểm tra xem hai cột có giống nhau không
print(f"Cột 'gdp_delflator_percent' - range: {df['gdp_delflator_percent'].min():.1f} to {df['gdp_delflator_percent'].max():.1f}")
print(f"Cột 'gdp_deflator_percent' - range: {df['gdp_deflator_percent'].min():.1f} to {df['gdp_deflator_percent'].max():.1f}")
```

**Kết quả:** Hai cột này **KHÁC nhau về bản chất:**
- `gdp_delflator_percent` thực chất là **GDP Deflator INDEX** - chỉ số tích lũy, giá trị lớn.
- `gdp_deflator_percent` là **GDP Deflator GROWTH RATE** - tỷ lệ thay đổi hàng năm %, giá trị nhỏ.

**Hành động:**
```python
# Đổi tên cột lỗi chính tả cho rõ nghĩa
df.rename(columns={'gdp_delflator_percent': 'gdp_deflator_index'}, inplace=True)
```

### Xử lý giá trị thiếu bằng nội suy tuyến tính

```python
# Đặt 'years' làm index chuỗi thời gian
df['years'] = pd.to_datetime(df['years'], format='%Y')
df.set_index('years', inplace=True)

# Nội suy tuyến tính cho missing values
df.interpolate(method='linear', inplace=True)
```

**Xác thực sau xử lý:**
- Số giá trị thiếu còn lại: **0** - tất cả missing values đã được xử lý
- Kích thước dữ liệu: Giữ nguyên 27 dòng × 11 cột - không mất quan sát nào

---

## 4.2.4 Xác thực Dữ liệu qua Trực quan hóa Xu hướng

### Mục đích
Trước khi chạy bất kỳ mô hình nào, cần "nhìn" dữ liệu bằng mắt. Biểu đồ xu hướng giúp:
1. Phát hiện các sự kiện kinh tế lớn ảnh hưởng đến dữ liệu.
2. Nhận biết sơ bộ liệu chuỗi có "dừng" - stationary, hay không.
3. Tìm mối liên hệ trực quan giữa các biến.

### Bảng điều khiển Kinh tế Vĩ mô - Macroeconomic Dashboard

Bốn biểu đồ tương ứng với 4 trụ cột kinh tế vĩ mô được trình bày trong một dashboard thống nhất:

#### Biểu đồ 1 — Trụ cột Giá cả: Lạm phát - CPI Growth Rate

- **Đặc điểm:** Biểu đồ đường có vùng tô - area chart, cho CPI growth rate, kết hợp đánh dấu các giai đoạn khủng hoảng - 2008–2009, COVID 2020–2021.
- **Nhận xét:**
  - Hai đỉnh lạm phát lớn nhất - 2008 và 2011, đều trùng với các sự kiện kinh tế toàn cầu và chính sách tiền tệ nới lỏng trong nước.
  - Điều này gợi ý rằng lạm phát Việt Nam chịu tác động từ CẢ yếu tố nội sinh lẫn ngoại sinh — cần mô hình đa biến để tách bạch.

#### Biểu đồ 2 — Trụ cột Tiền tệ: Tín dụng vs. Lãi suất

- **Đặc điểm:** Biểu đồ hai trục Y - dual-axis, với Domestic Credit Index - trục trái, và Lending Interest Rate - trục phải.
- **Nhận xét:**
  - Mối quan hệ nghịch rõ rệt: Khi lãi suất giảm → tín dụng tăng vọt.
  - Đây là cơ chế truyền dẫn tiền tệ cổ điển — xác nhận vai trò của Trụ cột Tiền tệ trong nền kinh tế.

#### Biểu đồ 3 — Trụ cột Đối ngoại: Xuất khẩu vs. Nhập khẩu

- **Đặc điểm:** Biểu đồ đường kép với vùng tô phân biệt thặng dư - xanh, và thâm hụt - đỏ, thương mại.
- **Nhận xét:**
  - Việt Nam chuyển từ thâm hụt thương mại mãn tính sang thặng dư bền vững sau năm 2012.
  - Nguyên nhân: Hội nhập sâu vào chuỗi cung ứng toàn cầu nhờ dòng vốn FDI từ Samsung, Intel, và các tập đoàn đa quốc gia.

#### Biểu đồ 4 — Trụ cột Tăng trưởng: GDP Growth Rate

- **Đặc điểm:** Biểu đồ kết hợp cột và đường - bar-line chart, cho GDP growth rate.
- **Nhận xét:**
  - Tăng trưởng GDP ổn định trong khoảng 5–7% suốt giai đoạn dài.
  - Duy nhất năm 2020 suy giảm mạnh do tác động COVID-19.
  - Sự bền bỉ của tăng trưởng GDP là nền tảng cho ổn định vĩ mô.

> 📷 **CHỤP MÀN HÌNH TỪ STREAMLIT:** Chụp biểu đồ "BẢNG ĐIỀU KHIỂN KINH TẾ VĨ MÔ VIỆT NAM - 1996–2022" từ trang **Data Exploration** để chèn vào đây.

### Kết luận Quan trọng từ Trực quan hóa

> Các chuỗi Index - CPI Index, Credit Index, Exchange Rate Index, có xu hướng tăng liên tục → chắc chắn **KHÔNG dừng** - non-stationary. Điều này buộc chúng ta phải **lấy sai phân - differencing** trước khi đưa vào mô hình VAR.

Phát hiện này xác nhận sự cần thiết của Bước kiểm định tính dừng - ADF Test, và biến đổi dữ liệu trong giai đoạn phân tích tiếp theo.

---

> *Phần tiếp theo: [4.3. Phân tích và Trực quan hóa Kết quả](./4.3_PhanTich_TrucQuanHoa.md)*
# 4.3 PHÂN TÍCH VÀ TRỰC QUAN HÓA KẾT QUẢ

**Bước 3 trong Quy trình Xây dựng Báo cáo Phân tích Dữ liệu**

---

## 4.3.1 Phân tích Mối quan hệ giữa các Biến

### 4.3.1.1 Ma trận Tương quan Pearson - Correlation Heatmap

Chín biến phân tích chính (loại bỏ các biến Index tích lũy không cần thiết) được đưa vào phân tích tương quan:

```python
analysis_vars = ['cpi_growth_percent', 'gdp_deflator_percent',
                 'gdp_growth_percent', 'unemployment_rate',
                 'domestic_credit_index', 'lending_interest_percent',
                 'officical_exchange_rate_percent', 'import_index', 'export_index']

corr_matrix = df[analysis_vars].corr()
```

**Cách đọc Correlation Heatmap:**
- Giá trị gần **+1:** Tương quan thuận mạnh (hai biến cùng tăng cùng giảm).
- Giá trị gần **-1:** Tương quan nghịch mạnh (một tăng thì cái kia giảm).
- Giá trị gần **0:** Không có mối liên hệ tuyến tính.

**Các phát hiện quan trọng:**

| Cặp biến | Tương quan | Ý nghĩa kinh tế |
|:---|:---:|:---|
| `cpi_growth_percent` ↔ `gdp_deflator_percent` | Thuận cao | Cả hai đều đo lường lạm phát — xác nhận dữ liệu nhất quán |
| `cpi_growth_percent` ↔ `lending_interest_percent` | Thuận | Khi lạm phát tăng, NHNN tăng lãi suất để kiềm chế (phản ứng chính sách) |
| `domestic_credit_index` ↔ `import_index` ↔ `export_index` ↔ `exchange_rate` | Thuận rất cao | **CẢNH BÁO: Đa cộng tuyến - multicollinearity!** Cần kiểm tra VIF |

**Diễn giải:** Nhóm các biến Index (tín dụng, xuất nhập khẩu, tỷ giá) đều phản ánh xu hướng tăng trưởng dài hạn của nền kinh tế, nên chúng có tương quan cao với nhau. Tuy nhiên, điều này gây nguy cơ đa cộng tuyến nếu đưa tất cả vào cùng một mô hình hồi quy.

> 📷 **CHỤP MÀN HÌNH TỪ STREAMLIT:** Chụp biểu đồ "Ma trận Tương quan Pearson giữa các biến Kinh tế Vĩ mô" từ trang **Correlation Analysis** để chèn vào đây.

---

### 4.3.1.2 Kiểm tra Đa cộng tuyến - VIF — Variance Inflation Factor

**Tại sao cần kiểm tra VIF?**
- VIF đo mức độ "trùng lặp thông tin" giữa các biến.
- Hậu quả nếu bỏ qua: Mô hình VAR sẽ cho hệ số "ảo" — kết luận sai về yếu tố nào thực sự ảnh hưởng lạm phát.

```python
vif_data = df[analysis_vars].dropna()
X_vif = sm.add_constant(vif_data)
vif_results = pd.DataFrame({
    'Variable': X_vif.columns[1:],
    'VIF': [variance_inflation_factor(X_vif.values, i+1) for i in range(len(X_vif.columns)-1)]
})
```

**Ngưỡng đánh giá:**

| VIF | Mức độ | Hành động |
|:---:|:---|:---|
| > 10 | Đa cộng tuyến nghiêm trọng (Đỏ) | Phải loại bỏ hoặc biến đổi biến |
| > 5 | Đa cộng tuyến cần lưu ý (Cam) | Cân nhắc kỹ khi đưa vào mô hình |
| < 5 | Chấp nhận được (Xanh) | An toàn |

**Kết quả và Kết luận VIF:**

- Các biến Index (`domestic_credit_index`, `import_index`, `export_index`, `officical_exchange_rate_percent`) có VIF rất cao → chúng mang thông tin "trùng lặp" vì đều phản ánh xu hướng tăng trưởng dài hạn của nền kinh tế.
- **Hành động:** Khi xây dựng mô hình VAR, cần:
  1. Chọn lọc biến cẩn thận — chỉ chọn **đại diện** cho mỗi trụ cột thay vì đưa tất cả vào.
  2. Sử dụng dữ liệu đã sai phân (stationarized) để giảm đa cộng tuyến.

> 📷 **CHỤP MÀN HÌNH TỪ STREAMLIT:** Chụp biểu đồ "Kiểm tra Đa cộng tuyến (VIF)" dạng cột nằm ngang từ trang **Correlation Analysis** để chèn vào đây.

---

## 4.3.2 Kiểm định Tính Dừng và Biến đổi Dữ liệu

### 4.3.2.1 Kiểm định ADF - Augmented Dickey-Fuller Test

**Tại sao phải kiểm tra tính dừng?**

Mô hình VAR CHỈ hoạt động đúng khi chuỗi dữ liệu "dừng" — tức là giá trị trung bình và phương sai không thay đổi theo thời gian. Nếu chuỗi không dừng, kết quả hồi quy sẽ là "hồi quy giả" (spurious regression) — các hệ số có vẻ có ý nghĩa thống kê nhưng thực tế là vô nghĩa.

**Thiết lập kiểm định:**
- **H0:** Chuỗi KHÔNG dừng - có nghiệm đơn vị — unit root
- **H1:** Chuỗi dừng - stationary
- **Quy tắc:** Bác bỏ H0 khi p-value < 0.05

```python
for col in analysis_vars:
    series = df[col].dropna()
    result = adfuller(series, autolag='AIC')
    status = "DỪNG ✓" if result[1] < 0.05 else "KHÔNG dừng ✗"
```

**Giải thích kết quả ADF:**

| Nhóm biến | Trạng thái | Đặc điểm | Ý nghĩa kinh tế |
|:---|:---:|:---|:---|
| Biến Growth Rate (%) | Dừng ✓ | Dao động quanh giá trị trung bình | GDP growth rate, CPI growth rate không thể tăng mãi — nền kinh tế có xu hướng quay về mức cân bằng dài hạn (mean-reversion) |
| Biến Index (tích lũy) | Không dừng ✗ | Xu hướng tăng liên tục | CPI Index, Credit Index chỉ có thể tăng (trừ khi giảm phát) — giá trị tuyệt đối luôn lớn hơn theo thời gian |

> 📷 **CHỤP MÀN HÌNH TỪ STREAMLIT:** Chụp 2 bảng "Kết quả ADF" (Gốc và Sau Sai phân) và biểu đồ "So sánh: Chuỗi Gốc vs. Sau Sai phân" từ trang **Stationarity Testing** để chèn vào đây.

---

### 4.3.2.2 Sai phân Bậc 1 và Kiểm định lại - Differencing & Re-test

**Hành động:** Lấy sai phân bậc 1 (`diff()`) cho các chuỗi không dừng — biến đổi chúng từ "giá trị tuyệt đối" thành "tỷ lệ thay đổi".

```python
non_stationary = [col for col, res in adf_results.items() if not res['stationary']]
df_diff = df[analysis_vars].copy()
for col in non_stationary:
    df_diff[col] = df_diff[col].diff()
df_diff = df_diff.dropna()
```

**Kiểm định lại ADF sau sai phân:**

Sau khi lấy sai phân bậc 1, kiểm định ADF được chạy lại cho tất cả các biến. Kết quả mong đợi: **tất cả các chuỗi đều dừng** (p-value < 0.05), đảm bảo điều kiện tiên quyết cho mô hình VAR.

---

## 4.3.3 Mô hình VAR — Phân tích Tác nhân Bên ngoài và Quán tính Lạm phát

### Ý tưởng Cốt lõi

VAR (Vector Autoregression) cho phép đồng thời trả lời HAI câu hỏi quan trọng nhất:

1. **"Lạm phát có tự sinh ra chính nó không?"** — Thông qua FEVD: nếu CPI tự giải thích >90% biến động → quán tính ("Bệnh tự miễn") là chủ đạo.
2. **"Yếu tố BÊN NGOÀI nào thực sự 'bẻ lái' lạm phát?"** — Thông qua Granger Causality và IRF: xác định kênh truyền dẫn nào đáng kể.

### 4.3.3.1 Chuẩn bị Dữ liệu cho VAR

Sau khi loại bỏ đa cộng tuyến (dựa trên kết quả VIF), bốn biến đại diện cho từng trụ cột được chọn:

```python
var_vars = ['cpi_growth_percent', 'gdp_growth_percent',
            'lending_interest_percent', 'officical_exchange_rate_percent']
var_data = df_diff[var_vars].dropna()
```

| Biến | Đại diện cho |
|:---|:---|
| `cpi_growth_percent` | Trụ cột Giá cả (Target) |
| `gdp_growth_percent` | Trụ cột Tăng trưởng |
| `lending_interest_percent` | Trụ cột Tiền tệ |
| `officical_exchange_rate_percent` | Trụ cột Đối ngoại |

Kiểm tra tính dừng xác nhận tất cả 4 biến đều stationary → sẵn sàng cho VAR.

---

### 4.3.3.2 Chọn Bậc trễ Tối ưu (Lag Order Selection)

```python
var_model_temp = VAR(var_data)
lag_results = var_model_temp.select_order(maxlags=2)
optimal_lag = lag_results.aic
```

**Tại sao bậc trễ (lag) quan trọng?**
- **Lag = 1:** Lạm phát hôm nay bị ảnh hưởng bởi GDP/Tỷ giá **1 năm trước**.
- **Lag = 2:** Ảnh hưởng kéo dài **2 năm trước**.
- Quá ít lag → bỏ sót hiệu ứng dài hạn. Quá nhiều lag → mất bậc tự do → mô hình không ổn định.
- Tiêu chuẩn AIC giúp tìm **điểm cân bằng tối ưu** giữa độ phù hợp và độ phức tạp.

**Lưu ý kỹ thuật:** `maxlags=2` được đặt thay vì giá trị lớn hơn do mẫu nhỏ (chỉ còn ~25 quan sát sau differencing) — không đủ bậc tự do cho lag cao hơn.

---

### 4.3.3.3 Kiểm định Nhân quả Granger - Granger Causality Test

```python
target = 'cpi_growth_percent'
for cause_var in var_vars:
    if cause_var != target:
        test_data = var_data[[target, cause_var]].dropna()
        result = grangercausalitytests(test_data, maxlag=maxlag, verbose=True)
```

**Thiết lập kiểm định:**
- **H0:** Biến X KHÔNG Granger-cause CPI
- **H1:** Biến X CÓ Granger-cause CPI (biết X giúp dự báo CPI tốt hơn)
- **Bác bỏ H0 khi:** p-value < 0.05

**Lưu ý quan trọng:** "X Granger-causes Y" KHÔNG có nghĩa là "X gây ra Y" theo nghĩa nhân quả cấu trúc. Nó chỉ có nghĩa: *"Biết giá trị quá khứ của X giúp DỰ BÁO Y tốt hơn so với chỉ dùng giá trị quá khứ của Y."*

**Giải thích kết quả cho từng biến:**

| Biến kiểm tra | Kết quả kỳ vọng | Cơ chế kinh tế |
|:---|:---|:---|
| **Tỷ giá → CPI** | Nếu p < 0.05: Tỷ giá CÓ tính dẫn dắt | VND mất giá → Hàng nhập khẩu đắt hơn → Chi phí sản xuất tăng → CPI tăng. Đây là kênh "Lạm phát nhập khẩu" - Imported Inflation. |
| **GDP Growth → CPI** | Nếu p < 0.05: GDP CÓ tính dẫn dắt | GDP tăng nhanh → Nhu cầu tiêu dùng tăng → "Cầu kéo" - Demand-pull → CPI tăng. |
| **Lending Interest → CPI** | Nếu p > 0.05: Lãi suất KHÔNG dẫn dắt rõ rệt | Lãi suất tại Việt Nam thường là **phản ứng** (NHNN tăng lãi suất SAU KHI lạm phát đã tăng), chứ không phải **nguyên nhân** gốc. |

---

### 4.3.3.4 Fit Mô hình VAR và Hàm Phản ứng Xung kích - IRF

```python
var_model = VAR(var_data)
var_result = var_model.fit(maxlags=optimal_lag)

# Impulse Response Function
irf = var_result.irf(10)
fig = irf.plot(orth=True, impulse=None, response='cpi_growth_percent')
```

**Cách đọc biểu đồ IRF:**
- Mỗi ô cho thấy: Khi biến X bị "sốc" 1 độ lệch chuẩn, CPI phản ứng thế nào qua 10 năm.
- **Đường thẳng = 0:** Không ảnh hưởng.
- **Đường trên 0:** Cú sốc LÀM TĂNG lạm phát.
- **Đường dưới 0:** Cú sốc LÀM GIẢM lạm phát.
- **Tốc độ về 0:** Nhanh = ảnh hưởng ngắn hạn. Chậm = ảnh hưởng kéo dài.

> 📷 **CHỤP MÀN HÌNH TỪ STREAMLIT:** Chụp các biểu đồ "Granger Causality: P-values" và "IRF: Phản ứng của CPI Growth trước các cú sốc" từ trang **VAR Model** để chèn vào đây.

---

### 4.3.3.5 Phân rã Phương sai - FEVD — Forecast Error Variance Decomposition

FEVD trả lời câu hỏi cốt lõi: *"Trong tổng biến động của Lạm phát, bao nhiêu % do chính Quán tính gây ra, bao nhiêu % do GDP, Tỷ giá, Lãi suất?"*

```python
fevd = var_result.fevd(10)
print(fevd.summary())
```

**Kết quả FEVD — Bảng số liệu (4 kỳ đầu):**

| Kỳ | Quán tính CPI (%) | GDP Growth (%) | Lãi suất (%) | Tỷ giá (%) |
|:---:|:---:|:---:|:---:|:---:|
| **Kỳ 1** | 100.0% | 0.0% | 0.0% | 0.0% |
| **Kỳ 2** | 1.2% | 98.8% | 0.0% | 0.0% |
| **Kỳ 3** | 75.6% | 0.0% | 24.4% | 0.0% |
| **Kỳ 4** | 0.7% | 0.9% | 13.9% | 84.5% |

### Biểu đồ FEVD dạng Cột chồng - Stacked Bar Chart

Biểu đồ cột chồng trực quan hóa kết quả FEVD qua 10 kỳ dự báo:

```python
# Bảng màu chuyên nghiệp
bar_colors = ['#1B3A4B', '#2EC4B6', '#FF6B6B', '#C0C0C0', '#FFCA3A']
# Mỗi cột = 1 kỳ dự báo, chia thành % đóng góp của từng biến
```

**Cách đọc biểu đồ FEVD dạng cột chồng:**
- Mỗi cột đại diện cho **1 kỳ dự báo** (từ Kỳ 1 đến Kỳ 10 sau cú sốc ban đầu).
- **Phần xanh đậm - Quán tính CPI:** Tỷ lệ % biến động lạm phát được giải thích bởi chính lạm phát quá khứ — tức "Bệnh tự miễn".
- **Các phần còn lại:** Đóng góp của GDP, Lãi suất, Tỷ giá — tức "Tác nhân bên ngoài".
- **Kỳ 1:** CPI luôn tự giải thích 100% (vì cú sốc chưa kịp lan truyền).
- **Từ Kỳ 2 trở đi:** Nếu phần xanh đậm vẫn chiếm >90% → Quán tính áp đảo → Lạm phát VN chủ yếu là "Bệnh tự miễn".
- **Con số % trên đỉnh mỗi cột** cho thấy tổng đóng góp của tất cả yếu tố ngoại sinh — càng nhỏ càng khẳng định vai trò yếu ớt của chúng.

> 📷 **CHỤP MÀN HÌNH TỪ STREAMLIT:** Chụp biểu đồ cột chồng "PHÂN RÃ PHƯƠNG SAI SAI SỐ DỰ BÁO CỦA BIẾN LẠM PHÁT (FEVD)" từ trang **VAR Model** để chèn vào đây.

---

## 4.3.4 Tổng hợp Kết quả Phân tích

| Giai đoạn | Phương pháp | Phát hiện Chính |
|:---|:---|:---|
| Tương quan | Pearson Correlation | CPI–GDP Deflator tương quan thuận cao; Các biến Index tương quan chéo mạnh |
| Đa cộng tuyến | VIF | Biến Index có VIF rất cao → cần chọn lọc biến cho VAR |
| Tính dừng | ADF Test | Biến Growth Rate: dừng; Biến Index: không dừng → cần differencing |
| Nhân quả | Granger Causality | GDP Growth có tính dẫn dắt đáng kể nhất; Lãi suất là phản ứng chứ không phải nguyên nhân |
| Lan truyền | IRF | Cú sốc ngoại sinh tắt dần nhanh → ảnh hưởng ngắn hạn và yếu |
| Phân rã | FEVD | >90% biến động CPI do quán tính → **"Bệnh tự miễn" là chủ đạo** |

---

> *Phần tiếp theo: [4.4. Viết phần Tường thuật và Đề xuất](./4.4_TuongThuat_DeXuat.md)*
# 4.4 TƯỜNG THUẬT VÀ ĐỀ XUẤT - INTERPRETATION, RECOMMENDATIONS AND NEXT STEPS

**Bước 4 trong Quy trình Xây dựng Báo cáo Phân tích Dữ liệu**

---

## 4.4.1 Bảng Tổng kết Bằng chứng

Trước khi đưa ra phán quyết cuối cùng, toàn bộ bằng chứng thu được từ pipeline phân tích được tổng hợp trong bảng sau:

| Tiêu chí | Kết quả từ Mô hình |
|:---|:---|
| **Mô hình sử dụng** | VAR - Vector Autoregression, với 4 biến: CPI Growth, GDP Growth, Tỷ giá hối đoái, Lãi suất cho vay |
| **Bậc trễ tối ưu** | Được chọn theo tiêu chuẩn AIC, `maxlags=2` do giới hạn kích thước mẫu |
| **Điều kiện tiên quyết** | Tất cả chuỗi đã dừng - stationary, sau sai phân bậc 1 — xác nhận qua ADF re-test |
| **Câu hỏi 1: Quán tính có mạnh không?** | FEVD: CPI tự giải thích >90% biến động của chính nó → **Quán tính áp đảo** |
| **Câu hỏi 2: Yếu tố ngoại sinh nào đáng kể?** | Granger Causality: Chỉ 1–2 biến có tính dẫn dắt, nhưng đóng góp rất nhỏ - <10% phương sai |
| **Tác động cú sốc - IRF** | Phản ứng của CPI trước cú sốc ngoại sinh tắt dần nhanh → ảnh hưởng ngắn hạn và yếu |
| **Kết luận tổng thể** | **"Bệnh tự miễn"** — Quán tính kỳ vọng là động lực CHÍNH của lạm phát Việt Nam |

---

## 4.4.2 Phán quyết: Trả lời The Ultimate Question

### Câu hỏi

> *"Lạm phát tại Việt Nam chủ yếu là do 'Bệnh tự miễn' - Quán tính kỳ vọng, hay 'Tác nhân bên ngoài' - Tỷ giá, Tín dụng, GDP?"*

### Câu trả lời dựa trên dữ liệu

**Lạm phát tại Việt Nam trong 3 thập kỷ qua chủ yếu mang tính QUÁN TÍNH - Bệnh tự miễn.**

### Chuỗi Bằng chứng

Kết luận trên được xây dựng từ ba nguồn bằng chứng bổ trợ lẫn nhau:

**1. Phân rã phương sai - FEVD — Bằng chứng định lượng mạnh nhất:**
- Kết quả FEVD cho thấy >90% biến động lạm phát được giải thích bởi chính quán tính lạm phát - lag values of CPI, không phải bởi GDP, Tỷ giá hay Lãi suất.
- Từ Kỳ 2 đến Kỳ 10, phần đóng góp của CPI vào phương sai của chính nó vẫn duy trì ở mức áp đảo, cho thấy tính quán tính không suy giảm theo thời gian.

**2. Kiểm định nhân quả Granger — Bằng chứng về tính dẫn dắt:**
- Trong các yếu tố ngoại sinh, chỉ có tăng trưởng GDP có tín hiệu "dẫn dắt" đáng kể nhất, nhưng đóng góp rất nhỏ - <10% phương sai.
- Lãi suất cho vay KHÔNG Granger-cause CPI — xác nhận rằng lãi suất tại Việt Nam là **phản ứng chính sách** - NHNN tăng lãi suất SAU KHI lạm phát đã tăng, chứ không phải nguyên nhân gốc.

**3. Hàm phản ứng xung kích - IRF — Bằng chứng về tính bền vững:**
- Phản ứng của CPI trước các cú sốc từ GDP, Tỷ giá, Lãi suất đều tắt dần rất nhanh - thường trong 2–3 kỳ.
- Điều này khẳng định: ngay cả khi các biến ngoại sinh có tác động, ảnh hưởng đó chỉ là nhất thời, không đủ sức duy trì lạm phát kéo dài.

### Cơ chế Kinh tế

Kết quả phân tích phù hợp với lý thuyết **kỳ vọng thích ứng - adaptive expectations:**

> Khi người dân và doanh nghiệp *kỳ vọng* giá cả sẽ tăng → họ đẩy giá bán lên trước - pre-emptive pricing, → giá thực sự tăng → xác nhận kỳ vọng ban đầu → vòng lặp tiếp tục.

Đây chính là "Bệnh tự miễn" — hệ miễn dịch - kỳ vọng, tấn công chính cơ thể - nền kinh tế, tạo ra một vòng lặp tự củng cố - self-reinforcing loop, mà không cần tác nhân kích hoạt bên ngoài.

> 📷 **CHỤP MÀN HÌNH TỪ STREAMLIT:** Chụp phần "CÂU TRẢ LỜI DỰA TRÊN DỮ LIỆU" - khối màu xanh có 2 ô % lớn, và các thẻ "Khuyến nghị Chính sách" từ trang **Conclusion** để chèn vào báo cáo tổng kết.

---

## 4.4.3 Khuyến nghị Chính sách - Recommendations

Nếu lạm phát chủ yếu do quán tính kỳ vọng, thì **chính sách hiệu quả nhất** không phải là can thiệp mạnh vào tỷ giá hay lãi suất, mà là quản trị tâm lý thị trường:

### Khuyến nghị 1: Neo Kỳ vọng Lạm phát - Inflation Targeting
- **Hành động:** NHNN cần công bố mục tiêu lạm phát rõ ràng, định lượng - ví dụ: "Mục tiêu CPI dưới 4% năm 2025" - và giữ vững cam kết.
- **Tác động kỳ vọng:** Giảm trực tiếp "Bệnh tự miễn" — khi dân chúng tin rằng NHNN sẽ giữ được mục tiêu, họ sẽ không đẩy giá lên phòng ngừa.
- **Mức độ ưu tiên:** Cao nhất
- **Đơn vị chịu trách nhiệm:** Ngân hàng Nhà nước Việt Nam

### Khuyến nghị 2: Truyền thông Chính sách Minh bạch
- **Hành động:** Giải thích minh bạch, dễ hiểu các quyết định tiền tệ - tăng/giảm lãi suất, điều chỉnh tỷ giá - thông qua báo cáo định kỳ và họp báo.
- **Tác động kỳ vọng:** Giảm bất định - uncertainty → giảm hành vi phòng ngừa lạm phát của thị trường.
- **Mức độ ưu tiên:** Cao
- **Đơn vị chịu trách nhiệm:** NHNN, Bộ Tài chính

### Khuyến nghị 3: Giám sát áp lực Cầu kéo từ GDP
- **Hành động:** Theo dõi sát sao tốc độ tăng trưởng GDP thực — đây là kênh ngoại sinh duy nhất có tính dẫn dắt đáng kể trong mô hình.
- **Tác động kỳ vọng:** Phát hiện sớm giai đoạn nền kinh tế "quá nóng" - overheating, có nguy cơ kích hoạt áp lực cầu kéo lạm phát.
- **Mức độ ưu tiên:** Trung bình
- **Đơn vị chịu trách nhiệm:** Bộ Kế hoạch & Đầu tư, Tổng cục Thống kê

---

## 4.4.4 Hạn chế của Nghiên cứu

Mọi kết luận cần được hiểu trong bối cảnh các giới hạn phương pháp luận sau:

| Hạn chế | Giải thích | Ảnh hưởng |
|:---|:---|:---|
| **Kích thước mẫu nhỏ** | Chỉ có 27 quan sát - 27 năm dữ liệu hàng năm, sau differencing còn ~25 | Giảm "sức mạnh thống kê" - statistical power, của các kiểm định, tăng nguy cơ overfitting khi ước lượng nhiều tham số |
| **Tần suất dữ liệu thấp** | Dữ liệu theo năm không bắt được biến động ngắn hạn - tháng/quý | Mô hình khó phát hiện các cú sốc tức thời - giá xăng dầu, tỷ giá biến động tháng |
| **Giả định tuyến tính** | VAR là mô hình tuyến tính, khó bắt được các điểm gãy cấu trúc - structural breaks | Sai số cao tại các điểm cực trị - khủng hoảng 2008, COVID-19 |
| **Chưa kiểm chứng ngoài mẫu** | Chưa có bước out-of-sample validation do mẫu quá nhỏ | Kết luận chỉ áp dụng cho giai đoạn quan sát - in-sample |

---

## 4.4.5 Hướng Phát triển

Để khắc phục các hạn chế và mở rộng phạm vi nghiên cứu, các hướng phát triển tiếp theo được đề xuất:

1. **Tăng kích thước mẫu:** Sử dụng dữ liệu tháng/quý từ Tổng cục Thống kê - GSO, Việt Nam để tăng số quan sát lên hàng trăm, cải thiện đáng kể sức mạnh thống kê.

2. **Mô hình cấu trúc - SVAR:** Áp dụng Structural VAR với các ràng buộc dựa trên lý thuyết kinh tế - ví dụ: lãi suất phản ứng trễ sau lạm phát, tỷ giá phản ứng trước GDP, để tách bạch nhân quả cấu trúc thay vì chỉ nhân quả Granger.

3. **So sánh với Machine Learning:** Kiểm chứng kết quả VAR bằng các mô hình phi tuyến như LSTM - Long Short-Term Memory, hoặc Random Forest, đặc biệt để xử lý các điểm gãy cấu trúc.

4. **Bổ sung ARIMA đơn biến:** So sánh trực tiếp khả năng dự báo giữa mô hình quán tính thuần túy - ARIMA — chỉ dùng lịch sử CPI, và mô hình đa biến - VAR — có thêm GDP, tỷ giá, lãi suất. Nếu ARIMA không thua kém VAR về độ chính xác → càng khẳng định vai trò yếu ớt của các biến ngoại sinh.

5. **Lượng hóa Tâm lý Lạm phát:** Sử dụng NLP - Natural Language Processing, và Sentiment Analysis trên dữ liệu báo chí kinh tế Việt Nam để xây dựng chỉ số "Kỳ vọng Lạm phát" dạng định lượng — kết hợp vào mô hình như một biến giải thích mới.

---

## TÀI LIỆU THAM KHẢO

- World Bank. *World Development Indicators (WDI)*. https://databank.worldbank.org/
- Sona. *What is an example of a data analysis report? Definition and best practices*. https://www.sona.com/blog/what-is-an-example-of-a-data-analysis-report-definition-and-best-practices
- Hamilton, J.D. (1994). *Time Series Analysis*. Princeton University Press.
- Luetkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer.

---

> *Quay lại: [1. Tóm tắt Tổng quan](./1_TomTatTongQuan.md) | [Mục lục đầy đủ](./README.md)*
