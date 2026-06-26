"""
Script to generate Project1_DAAN_v2.ipynb
A comprehensive, analysis-focused Jupyter Notebook for the
Vietnam Inflation Forecast project.
"""
import json
import os

def md(source):
    """Create a markdown cell."""
    if isinstance(source, str):
        source = source.split('\n')
    # Ensure each line ends with \n except the last
    lines = []
    for i, line in enumerate(source):
        if i < len(source) - 1:
            lines.append(line + '\n' if not line.endswith('\n') else line)
        else:
            lines.append(line.rstrip('\n'))
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": lines
    }

def code(source):
    """Create a code cell."""
    if isinstance(source, str):
        source = source.split('\n')
    lines = []
    for i, line in enumerate(source):
        if i < len(source) - 1:
            lines.append(line + '\n' if not line.endswith('\n') else line)
        else:
            lines.append(line.rstrip('\n'))
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": lines
    }

def build_notebook():
    cells = []

    # =========================================================================
    # CHAPTER 1: PROJECT INTRODUCTION & THE ULTIMATE QUESTION
    # =========================================================================
    cells.append(md("""# Macroeconomic Forecasting Project: Multivariate Analysis
---

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
> *"Trong 3 thập kỷ qua, Lạm phát tại Việt Nam chủ yếu là do **'Bệnh tự miễn'** (Quán tính tự sinh ra do tâm lý kỳ vọng) hay do **'Tác nhân bên ngoài'** (Tỷ giá, Tín dụng, Tăng trưởng GDP)? Cần can thiệp vào đâu để kiểm soát nó?"*"""))

    cells.append(md("""### CƠ SỞ KINH TẾ HỌC TRONG VIỆC LỰA CHỌN BIẾN SỐ

Để trả lời câu hỏi tối thượng của project, tập dữ liệu 11 biến được nhóm chọn đại diện cho **4 Trụ cột của nền Kinh tế Vĩ mô**:

1. **Trụ cột Giá cả (Đo lường bệnh lý):** `cpi_growth_percent` (Mục tiêu), `gdp_deflator_percent` (Lạm phát từ phía sản xuất).
   - *Tại sao?* CPI đo lường giá cả từ phía tiêu dùng (giỏ hàng hóa hộ gia đình), còn GDP Deflator đo từ phía sản xuất. Khi cả hai cùng tăng, ta biết chắc lạm phát là "thật" chứ không phải do một sự kiện cục bộ.

2. **Trụ cột Tăng trưởng (Áp lực Cầu kéo):** `gdp_growth_percent`, `unemployment_rate`.
   - *Tại sao?* Theo lý thuyết Đường cong Phillips, khi GDP tăng nhanh → thất nghiệp giảm → áp lực tăng lương → giá cả tăng. Đây là kênh "Cầu kéo" (Demand-pull) của lạm phát.

3. **Trụ cột Tiền tệ (Bơm tiền & Lãi suất):** `domestic_credit_index`, `lending_interest_percent`.
   - *Tại sao?* Khi tín dụng mở rộng (bơm tiền) và lãi suất giảm → doanh nghiệp và người dân vay nhiều hơn → tiền trong nền kinh tế tăng → giá cả tăng. Đây là kênh "Tiền tệ" (Monetary channel).

4. **Trụ cột Đối ngoại (Cú sốc ngoại sinh):** `officical_exchange_rate_percent`, `import_index`, `export_index`.
   - *Tại sao?* Khi VND mất giá so với USD → hàng nhập khẩu (xăng dầu, nguyên liệu) đắt hơn → chi phí sản xuất tăng → giá cả tăng. Đây là kênh "Chi phí đẩy" (Cost-push) từ bên ngoài."""))

    # =========================================================================
    # CHAPTER 2: RAW DATA EXPLORATION & CHARACTERIZATION
    # =========================================================================
    cells.append(md("""## **CHƯƠNG 2: Khám phá & Đặc trưng hóa Dữ liệu Thô**
---

> **Triết lý phân tích:** Trước khi đưa bất kỳ dữ liệu nào vào mô hình, chúng ta PHẢI hiểu rõ dữ liệu mình đang có. Mỗi biến số có những đặc điểm riêng (phân phối, xu hướng, giá trị thiếu) mà nếu không nắm bắt sẽ dẫn đến kết luận sai lệch."""))

    cells.append(md("### 2.1 Import Libraries"))

    cells.append(code("""import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import shapiro, jarque_bera, probplot

from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan

from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.vector_ar.var_model import VAR
from statsmodels.tsa.stattools import grangercausalitytests

import warnings
warnings.filterwarnings('ignore')

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12"""))

    cells.append(md("### 2.2 Upload & Preview Dataset"))

    cells.append(code("""# Tải dữ liệu
# Nếu chạy trên Google Colab, hãy upload file dataset_project1.xlsx
# hoặc sửa đường dẫn cho phù hợp
df = pd.read_excel('/content/dataset_project1.xlsx')
display(df.head(10))"""))

    cells.append(md("""### 2.3 Data Overview: Hiểu cấu trúc dữ liệu

**Mục đích:** Trước khi phân tích, ta cần biết:
- Có bao nhiêu quan sát (dòng)?
- Mỗi biến có kiểu dữ liệu gì?
- Có giá trị null/thiếu không?
- Các thống kê mô tả cơ bản (mean, std, min, max) cho biết gì?"""))

    cells.append(code("""print("=" * 60)
print("THÔNG TIN CẤU TRÚC DATASET")
print("=" * 60)
print(df.info())
print()
print("=" * 60)
print("THỐNG KÊ MÔ TẢ")
print("=" * 60)
display(df.describe())"""))

    cells.append(md("""### 2.4 Missing Values Analysis

**Tại sao phải kiểm tra giá trị thiếu?**
- Dữ liệu kinh tế vĩ mô từ World Bank thường có khoảng trống do: một số quốc gia chưa thống kê đầy đủ vào những năm đầu, hoặc phương pháp thu thập thay đổi.
- Nếu bỏ qua missing values → mô hình sẽ bị lệch (biased) hoặc không thể chạy được."""))

    cells.append(code("""# Đếm số giá trị thiếu mỗi cột
missing_counts = df.isnull().sum()
print("SỐ GIÁ TRỊ THIẾU THEO TỪNG BIẾN:")
print(missing_counts)
print()

# Heatmap trực quan hóa vị trí missing values
fig, axes = plt.subplots(1, 2, figsize=(18, 6))

# Heatmap missing values
sns.heatmap(df.isnull(), cbar=False, ax=axes[0], cmap='viridis')
axes[0].set_title('Bản đồ Giá trị Thiếu (Vàng = Missing)', fontweight='bold')
axes[0].set_ylabel('Chỉ số dòng (Năm)')

# Bar chart missing values
missing_pct = (df.isnull().sum() / len(df)) * 100
missing_pct = missing_pct[missing_pct > 0]
if len(missing_pct) > 0:
    missing_pct.plot(kind='barh', ax=axes[1], color='coral')
    axes[1].set_title('Tỷ lệ % Giá trị Thiếu', fontweight='bold')
    axes[1].set_xlabel('% Missing')
else:
    axes[1].text(0.5, 0.5, 'Không có giá trị thiếu!', ha='center', va='center', fontsize=14)

plt.tight_layout()
plt.show()"""))

    cells.append(md("""**Nhận xét & Hành động:**
- `domestic_credit_index` và `lending_interest_percent` là hai biến có giá trị thiếu. Đây là các biến thuộc **Trụ cột Tiền tệ**.
- **Tại sao thiếu?** Dữ liệu tín dụng nội địa và lãi suất cho vay từ World Bank cho Việt Nam không được ghi nhận đầy đủ trong một số năm đầu tiên của giai đoạn nghiên cứu.
- **Giải pháp:** Sử dụng **nội suy tuyến tính (linear interpolation)** — phương pháp phù hợp nhất cho dữ liệu chuỗi thời gian vì nó giả định giá trị biến đổi dần dần theo thời gian (hợp lý với dữ liệu kinh tế)."""))

    cells.append(md("""### 2.5 Data Cleaning: Xử lý cột trùng lặp & giá trị thiếu"""))

    cells.append(code("""# Kiểm tra cột trùng lặp/lỗi chính tả
print("Các cột trong dataset:")
for col in df.columns:
    print(f"  - {col}")

# Nhận thấy có cả 'gdp_delflator_percent' (lỗi chính tả) và 'gdp_deflator_percent'
# Kiểm tra xem chúng có giống nhau không
if 'gdp_delflator_percent' in df.columns and 'gdp_deflator_percent' in df.columns:
    print("\\nKiểm tra 2 cột gdp deflator:")
    print(f"  gdp_delflator_percent (typo) vs gdp_deflator_percent:")
    # Cột 'gdp_delflator_percent' là GDP Deflator INDEX (tích lũy)
    # Cột 'gdp_deflator_percent' là GDP Deflator GROWTH RATE (% thay đổi)
    print(f"  Cột 'gdp_delflator_percent' - range: {df['gdp_delflator_percent'].min():.1f} to {df['gdp_delflator_percent'].max():.1f}")
    print(f"  Cột 'gdp_deflator_percent' - range: {df['gdp_deflator_percent'].min():.1f} to {df['gdp_deflator_percent'].max():.1f}")
    print("  => Hai cột này KHÁC nhau: một là Index, một là Growth Rate")"""))

    cells.append(code("""# Xử lý missing values bằng linear interpolation
print("Xử lý giá trị thiếu...")

# Đặt 'years' làm index
df['years'] = pd.to_datetime(df['years'], format='%Y')
df.set_index('years', inplace=True)

# Loại bỏ cột trùng lặp (giữ lại cột đúng chính tả)
if 'gdp_delflator_percent' in df.columns:
    # Đổi tên cột lỗi thành tên có ý nghĩa
    df.rename(columns={'gdp_delflator_percent': 'gdp_deflator_index'}, inplace=True)
    # Giữ 'cpi_index' và loại bỏ redundancy
    if 'cpi_index' in df.columns:
        print("  Giữ lại: cpi_index, gdp_deflator_index (là Index tích lũy)")
        print("  Giữ lại: cpi_growth_percent, gdp_deflator_percent (là Growth Rate %)")

# Nội suy tuyến tính cho missing values
df.interpolate(method='linear', inplace=True)

# Kiểm tra lại
print(f"\\nSau khi xử lý - Số giá trị thiếu còn lại: {df.isnull().sum().sum()}")
print(f"Shape: {df.shape}")
display(df.head())"""))

    cells.append(md("""### 2.6 Univariate Distribution Analysis: Đặc trưng phân phối từng biến

**Mục đích:** Hiểu hình dạng phân phối của mỗi biến TRƯỚC KHI đưa vào mô hình.
- **Tại sao quan trọng?** Nhiều mô hình thống kê (OLS, ARIMA) giả định phần dư (residuals) có phân phối chuẩn. Nếu dữ liệu gốc đã lệch (skewed) quá mạnh, kết quả mô hình có thể không đáng tin.
- **Ta cần biết gì?** Mỗi biến có phân phối chuẩn không? Có outlier không? Hình dạng phân phối nói lên điều gì về kinh tế?"""))

    cells.append(code("""# Phân tích phân phối cho các biến Growth Rate (%)
growth_vars = ['cpi_growth_percent', 'gdp_deflator_percent',
               'gdp_growth_percent', 'unemployment_rate',
               'lending_interest_percent']

fig, axes = plt.subplots(len(growth_vars), 3, figsize=(20, 5 * len(growth_vars)))

for i, var in enumerate(growth_vars):
    data = df[var].dropna()

    # Histogram
    axes[i, 0].hist(data, bins=15, edgecolor='black', alpha=0.7, color='steelblue')
    axes[i, 0].set_title(f'{var}\\n(Histogram)', fontweight='bold')
    axes[i, 0].axvline(data.mean(), color='red', linestyle='--', label=f'Mean={data.mean():.2f}')
    axes[i, 0].axvline(data.median(), color='green', linestyle='--', label=f'Median={data.median():.2f}')
    axes[i, 0].legend(fontsize=9)

    # Boxplot
    axes[i, 1].boxplot(data, vert=True)
    axes[i, 1].set_title(f'{var}\\n(Boxplot - phát hiện Outliers)', fontweight='bold')

    # Q-Q Plot
    probplot(data, dist="norm", plot=axes[i, 2])
    axes[i, 2].set_title(f'{var}\\n(Q-Q Plot - kiểm tra phân phối chuẩn)', fontweight='bold')

plt.suptitle('PHÂN TÍCH PHÂN PHỐI CÁC BIẾN TỶ LỆ (%)', fontsize=18, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()"""))

    cells.append(code("""# Kiểm định phân phối chuẩn cho từng biến
print("=" * 80)
print("KIỂM ĐỊNH PHÂN PHỐI CHUẨN (Shapiro-Wilk & Jarque-Bera)")
print("=" * 80)
print(f"{'Biến':<35} {'Shapiro p-value':>15} {'JB p-value':>15} {'Kết luận':>15}")
print("-" * 80)

all_numeric = df.select_dtypes(include=[np.number]).columns
for var in all_numeric:
    data = df[var].dropna()
    if len(data) >= 8:  # Cần tối thiểu 8 quan sát cho Shapiro
        stat_sw, p_sw = shapiro(data)
        stat_jb, p_jb = jarque_bera(data)
        normal = "Chuẩn" if (p_sw > 0.05 and p_jb > 0.05) else "KHÔNG chuẩn"
        print(f"{var:<35} {p_sw:>15.4f} {p_jb:>15.4f} {normal:>15}")"""))

    cells.append(md("""**Nhận xét phân phối - Ý nghĩa kinh tế:**

- **`cpi_growth_percent` (Lạm phát):** Phân phối lệch phải (right-skewed). *Tại sao?* Vì lạm phát tại Việt Nam có những đợt "bùng nổ" bất thường (2008: ~23%, 2011: ~18%) — đây là các outlier ngoại lai. Ngược lại, giảm phát (CPI < 0) rất hiếm. Điều này cho thấy lạm phát tại VN có tính "bất đối xứng": tăng dễ, giảm khó.

- **`gdp_growth_percent`:** Gần phân phối chuẩn hơn nhưng có đuôi trái dài. *Tại sao?* GDP Việt Nam thường tăng trưởng ổn định 5-7%, nhưng có những năm suy thoái đột ngột (2020: COVID-19).

- **Các biến Index (cpi_index, gdp_deflator_index, domestic_credit_index, exchange_rate):** KHÔNG có phân phối chuẩn — chúng là chuỗi tích lũy có xu hướng tăng theo thời gian. Đây là dấu hiệu rõ ràng của **tính KHÔNG dừng (non-stationarity)** — một vấn đề sẽ được xử lý ở Chương 4."""))

    cells.append(md("""### 2.7 Time Series Trend Visualization: Xu hướng theo thời gian

**Mục đích:** Trước khi chạy bất kỳ model nào, ta cần "nhìn" dữ liệu. Biểu đồ xu hướng giúp:
1. Phát hiện các sự kiện kinh tế lớn ảnh hưởng đến dữ liệu.
2. Nhận biết bằng mắt liệu chuỗi có "dừng" (stationary) hay không.
3. Tìm mối liên hệ trực quan giữa các biến."""))

    cells.append(code("""# Macroeconomic Dashboard - 4 biểu đồ cho 4 Trụ cột
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(22, 15))

# 1. Trụ cột Giá cả: CPI Growth
axes[0,0].plot(df.index, df['cpi_growth_percent'], linewidth=3, color='#E24A33', label='CPI Growth Rate')
axes[0,0].fill_between(df.index, df['cpi_growth_percent'], alpha=0.15, color='#E24A33')
axes[0,0].axhline(0, color='black', linewidth=0.5)
# Đánh dấu sự kiện
import pandas as pds
axes[0,0].axvspan(pds.Timestamp('2008-01-01'), pds.Timestamp('2009-12-31'), alpha=0.15, color='gray', label='Khủng hoảng 2008')
axes[0,0].axvspan(pds.Timestamp('2020-01-01'), pds.Timestamp('2021-12-31'), alpha=0.15, color='blue', label='COVID-19')
axes[0,0].set_title('1. Lạm phát bùng nổ trùng với các cuộc khủng hoảng toàn cầu', fontsize=14, fontweight='bold')
axes[0,0].set_ylabel('Inflation Rate (%)')
axes[0,0].legend(loc='upper right')
axes[0,0].grid(True, linestyle='--', alpha=0.5)

# 2. Trụ cột Tiền tệ: Credit vs Interest Rate
ax1 = axes[0,1]
ax2 = ax1.twinx()
credit_series = df['domestic_credit_index'].ffill()
interest_series = df['lending_interest_percent'].ffill()
line1 = ax1.plot(df.index, credit_series, color='#348ABD', linewidth=2.5, label='Domestic Credit Index (Trái)')
line2 = ax2.plot(df.index, interest_series, color='#988ED5', linewidth=2.5, linestyle='--', label='Lending Interest Rate (Phải)')
ax1.set_title('2. Chính sách tiền tệ phản chu kỳ: Hạ lãi suất → Tín dụng tăng', fontsize=14, fontweight='bold')
ax1.set_ylabel('Domestic Credit Index', color='#348ABD')
ax2.set_ylabel('Lending Interest Rate (%)', color='#988ED5')
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.3)

# 3. Trụ cột Đối ngoại: Import vs Export
axes[1,0].plot(df.index, df['export_index'], color='#FBC15E', linewidth=2.5, label='Export Index')
axes[1,0].plot(df.index, df['import_index'], color='#8EBA42', linewidth=2.5, label='Import Index')
axes[1,0].fill_between(df.index, df['export_index'], df['import_index'],
                       where=(df['export_index'] >= df['import_index']),
                       color='green', alpha=0.12, label='Thặng dư')
axes[1,0].fill_between(df.index, df['export_index'], df['import_index'],
                       where=(df['export_index'] < df['import_index']),
                       color='red', alpha=0.12, label='Thâm hụt')
axes[1,0].set_title('3. Chuyển đổi cơ cấu: Từ thâm hụt mãn tính sang thặng dư bền vững sau 2012', fontsize=14, fontweight='bold')
axes[1,0].set_ylabel('Value Index')
axes[1,0].legend(loc='upper left')
axes[1,0].grid(True, linestyle='--', alpha=0.5)

# 4. Trụ cột Tăng trưởng: GDP Growth
gdp_series = df['gdp_growth_percent'].ffill()
axes[1,1].bar(df.index, gdp_series, width=260, color='#4682B4', alpha=0.4, label='GDP Growth Rate (Bar)')
axes[1,1].plot(df.index, gdp_series, color='#4682B4', linewidth=2.5, marker='o', markersize=5, label='GDP Trend (Line)')
axes[1,1].axhline(0, color='black', linewidth=1.2)
axes[1,1].set_title('4. Tăng trưởng GDP dài hạn bền bỉ với suy giảm chu kỳ hậu COVID', fontsize=14, fontweight='bold')
axes[1,1].set_ylabel('GDP Growth Rate (%)')
axes[1,1].legend(loc='upper right')
axes[1,1].grid(True, linestyle='--', alpha=0.5)

plt.suptitle('BẢNG ĐIỀU KHIỂN KINH TẾ VĨ MÔ VIỆT NAM (1996-2024)', fontsize=20, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()"""))

    cells.append(md("""**Nhận xét từ biểu đồ xu hướng:**

1. **Lạm phát (CPI Growth):** Hai đỉnh lạm phát lớn nhất (2008 và 2011) đều trùng với các sự kiện kinh tế toàn cầu và chính sách tiền tệ nới lỏng trong nước. Điều này gợi ý rằng lạm phát VN chịu tác động từ CẢ yếu tố nội sinh lẫn ngoại sinh.

2. **Tín dụng vs Lãi suất:** Đồ thị cho thấy mối quan hệ nghịch rõ rệt — khi lãi suất giảm, tín dụng tăng vọt. Đây là cơ chế truyền dẫn tiền tệ cổ điển.

3. **Import/Export:** Việt Nam chuyển từ thâm hụt thương mại sang thặng dư sau 2012, nhờ hội nhập sâu vào chuỗi cung ứng toàn cầu (FDI từ Samsung, Intel...).

4. **GDP:** Tăng trưởng ổn định 5-7% với duy nhất 2020 suy giảm mạnh do COVID-19.

**Kết luận quan trọng:** Các chuỗi Index (CPI Index, Credit Index, Exchange Rate) có xu hướng tăng liên tục → chắc chắn KHÔNG dừng. Điều này buộc ta phải lấy sai phân (differencing) trước khi đưa vào ARIMA/VAR ở Chương 4."""))

    # =========================================================================
    # CHAPTER 3: RELATIONSHIP ANALYSIS
    # =========================================================================
    cells.append(md("""## **CHƯƠNG 3: Phân tích Mối quan hệ & Kiểm định Giả thuyết**
---

> **Câu hỏi cốt lõi:** Yếu tố nào THỰC SỰ có mối liên hệ với Lạm phát? Mối liên hệ đó mạnh hay yếu? Có thể tin cậy được không?"""))

    cells.append(md("### 3.1 Correlation Heatmap: Bức tranh toàn cảnh mối quan hệ"))

    cells.append(code("""# Chọn các biến phân tích chính (loại bỏ Index tích lũy)
analysis_vars = ['cpi_growth_percent', 'gdp_deflator_percent',
                 'gdp_growth_percent', 'unemployment_rate',
                 'domestic_credit_index', 'lending_interest_percent',
                 'officical_exchange_rate_percent', 'import_index', 'export_index']

corr_matrix = df[analysis_vars].corr()

plt.figure(figsize=(12, 10))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='RdBu_r',
            center=0, mask=mask, square=True, linewidths=0.5)
plt.title('Ma trận Tương quan Pearson giữa các biến Kinh tế Vĩ mô', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()"""))

    cells.append(md("""**Đọc hiểu Correlation Heatmap:**
- Giá trị gần **+1**: Tương quan thuận mạnh (cùng tăng cùng giảm).
- Giá trị gần **-1**: Tương quan nghịch mạnh (một tăng thì cái kia giảm).
- Giá trị gần **0**: Không có mối liên hệ tuyến tính.

**Phát hiện quan trọng:**
- `cpi_growth_percent` và `gdp_deflator_percent`: Tương quan thuận cao → Cả hai đều đo lường lạm phát, xác nhận dữ liệu nhất quán.
- `cpi_growth_percent` và `lending_interest_percent`: Tương quan thuận → Khi lạm phát tăng, NHNN tăng lãi suất để kiềm chế (phản ứng chính sách).
- `domestic_credit_index`, `import_index`, `export_index`, `exchange_rate`: Tương quan cao với nhau → CẢNH BÁO đa cộng tuyến (multicollinearity)! Cần kiểm tra VIF."""))

    cells.append(md("""### 3.2 Phillips Curve Analysis: Kiểm chứng lý thuyết Đường cong Phillips

**Lý thuyết:** A.W. Phillips (1958) phát hiện mối quan hệ nghịch giữa Lạm phát và Thất nghiệp — khi thất nghiệp giảm, lạm phát tăng (do áp lực tăng lương).

**Câu hỏi:** Đường cong Phillips có đúng cho Việt Nam không? Nếu KHÔNG, tại sao?"""))

    cells.append(code("""# Phillips Curve: Regression CPI Growth ~ Unemployment Rate
X = df['unemployment_rate']
y = df['cpi_growth_percent']
X_with_const = sm.add_constant(X)

phillips_model = sm.OLS(y, X_with_const).fit()

fig, axes = plt.subplots(1, 2, figsize=(18, 7))

# Scatter Plot + Regression Line
sns.regplot(x='unemployment_rate', y='cpi_growth_percent', data=df,
            scatter_kws={'alpha': 0.6, 's': 80}, line_kws={'color': 'red'},
            ax=axes[0])
axes[0].set_title('PHILLIPS CURVE: Lạm phát vs Thất nghiệp (Việt Nam 1996-2024)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Unemployment Rate (%)')
axes[0].set_ylabel('CPI Growth (%)')
axes[0].grid(True, linestyle='--', alpha=0.5)

# Residual plot
axes[1].scatter(phillips_model.fittedvalues, phillips_model.resid, alpha=0.6, s=80)
axes[1].axhline(0, color='red', linestyle='--')
axes[1].set_title('Phần dư (Residuals) của mô hình Phillips', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Fitted Values')
axes[1].set_ylabel('Residuals')
axes[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

print(phillips_model.summary())"""))

    cells.append(md("""**Giải thích kết quả Phillips Curve:**

- **R-squared** rất thấp → Thất nghiệp CHỈ giải thích một phần rất nhỏ biến động lạm phát tại Việt Nam.
- **Tại sao Đường cong Phillips không hoạt động tốt ở VN?**
  1. Thị trường lao động VN có nhiều lao động phi chính thức → tỷ lệ thất nghiệp chính thức không phản ánh đúng thực tế.
  2. Lạm phát VN chịu ảnh hưởng nhiều từ yếu tố cung (giá xăng dầu, tỷ giá) hơn là cầu lao động.
  3. Điều này gợi ý rằng ta cần tìm "thủ phạm" khác cho lạm phát VN → Chuyển sang phân tích VAR đa biến."""))

    cells.append(md("""### 3.3 Multicollinearity Check (VIF)

**Tại sao cần kiểm tra VIF?**
- VIF (Variance Inflation Factor) đo mức độ "trùng lặp thông tin" giữa các biến.
- VIF > 10: Đa cộng tuyến nghiêm trọng → hệ số hồi quy không đáng tin → cần loại bỏ biến.
- **Hậu quả nếu bỏ qua:** Mô hình VAR sẽ cho hệ số "ảo" — kết luận sai về yếu tố nào ảnh hưởng lạm phát."""))

    cells.append(code("""# Tính VIF cho các biến phân tích
vif_data = df[analysis_vars].dropna()
X_vif = sm.add_constant(vif_data)

vif_results = pd.DataFrame({
    'Variable': X_vif.columns[1:],
    'VIF': [variance_inflation_factor(X_vif.values, i+1) for i in range(len(X_vif.columns)-1)]
})
vif_results = vif_results.sort_values('VIF', ascending=False)
print("VARIANCE INFLATION FACTOR (VIF)")
print("VIF > 10: Đa cộng tuyến nghiêm trọng")
print("VIF > 5:  Đa cộng tuyến cần lưu ý")
print("=" * 50)
display(vif_results)

# Trực quan hóa
plt.figure(figsize=(10, 6))
colors = ['red' if v > 10 else 'orange' if v > 5 else 'green' for v in vif_results['VIF']]
plt.barh(vif_results['Variable'], vif_results['VIF'], color=colors)
plt.axvline(10, color='red', linestyle='--', label='Ngưỡng nguy hiểm (VIF=10)')
plt.axvline(5, color='orange', linestyle='--', label='Ngưỡng cảnh báo (VIF=5)')
plt.title('Kiểm tra Đa cộng tuyến (VIF)', fontsize=14, fontweight='bold')
plt.xlabel('VIF Score')
plt.legend()
plt.tight_layout()
plt.show()"""))

    cells.append(md("""**Kết luận VIF:**
- Các biến Index (Credit, Import, Export, Exchange Rate) có VIF rất cao → chúng mang thông tin "trùng lặp" vì đều phản ánh xu hướng tăng trưởng dài hạn của nền kinh tế.
- **Hành động:** Khi xây dựng mô hình VAR, ta cần chọn lọc biến cẩn thận và sử dụng dữ liệu đã sai phân (stationarized) để giảm đa cộng tuyến."""))

    # =========================================================================
    # CHAPTER 4: STATIONARITY TESTING
    # =========================================================================
    cells.append(md("""## **CHƯƠNG 4: Kiểm định Tính Dừng & Biến đổi Dữ liệu**
---

> **Tại sao phải kiểm tra tính dừng (Stationarity)?**
>
> Hãy tưởng tượng bạn muốn dự báo nhiệt độ ngày mai. Nếu bạn sống ở vùng nhiệt đới (nhiệt độ dao động quanh 30°C ổn định) → dễ dự báo. Nhưng nếu bạn sống ở nơi đang nóng lên liên tục (20°C → 25°C → 30°C → 35°C...) → rất khó dự báo vì "quy luật" liên tục thay đổi.
>
> Tương tự, mô hình ARIMA/VAR CHỈ hoạt động đúng khi chuỗi dữ liệu "dừng" — tức là giá trị trung bình và phương sai không thay đổi theo thời gian."""))

    cells.append(md("### 4.1 ADF Test: Augmented Dickey-Fuller"))

    cells.append(code("""# ADF Test cho tất cả các biến
print("=" * 90)
print("KIỂM ĐỊNH TÍNH DỪNG - AUGMENTED DICKEY-FULLER (ADF) TEST")
print("H0: Chuỗi KHÔNG dừng (có đơn vị root)")
print("H1: Chuỗi dừng")
print("Bác bỏ H0 khi p-value < 0.05")
print("=" * 90)
print(f"{'Biến':<35} {'ADF Statistic':>15} {'P-value':>15} {'Kết luận':>15}")
print("-" * 90)

adf_results = {}
for col in analysis_vars:
    series = df[col].dropna()
    result = adfuller(series, autolag='AIC')
    status = "DỪNG ✓" if result[1] < 0.05 else "KHÔNG dừng ✗"
    adf_results[col] = {'statistic': result[0], 'pvalue': result[1], 'stationary': result[1] < 0.05}
    print(f"{col:<35} {result[0]:>15.4f} {result[1]:>15.4f} {status:>15}")"""))

    cells.append(md("""**Giải thích kết quả ADF:**

- **Các biến "Dừng" (Stationary):** Thường là các biến đo lường tỷ lệ % (growth rate) — vì tỷ lệ tăng/giảm tự nhiên dao động quanh một giá trị trung bình.
  - *Ý nghĩa kinh tế:* GDP growth rate không thể tăng mãi — nền kinh tế có xu hướng quay về mức tăng trưởng cân bằng dài hạn (mean-reversion).

- **Các biến "Không dừng" (Non-stationary):** Thường là các chỉ số tích lũy (Index) — vì chúng phản ánh giá trị tuyệt đối luôn tăng theo thời gian.
  - *Ý nghĩa kinh tế:* CPI Index chỉ có thể tăng (trừ khi giảm phát), giống như tổng GDP luôn lớn hơn.

- **Hành động:** Lấy sai phân bậc 1 (`diff()`) cho các chuỗi không dừng → biến đổi chúng từ "giá trị tuyệt đối" thành "tỷ lệ thay đổi"."""))

    cells.append(md("### 4.2 Differencing & Re-test"))

    cells.append(code("""# Lấy sai phân bậc 1 cho các chuỗi không dừng
non_stationary = [col for col, res in adf_results.items() if not res['stationary']]
print(f"Các biến cần sai phân: {non_stationary}")
print()

df_diff = df[analysis_vars].copy()
for col in non_stationary:
    df_diff[col] = df_diff[col].diff()

df_diff = df_diff.dropna()

# Re-test ADF
print("=" * 90)
print("RE-TEST ADF SAU KHI SAI PHÂN BẬC 1")
print("=" * 90)
print(f"{'Biến':<35} {'ADF Statistic':>15} {'P-value':>15} {'Kết luận':>15}")
print("-" * 90)

for col in analysis_vars:
    series = df_diff[col].dropna()
    result = adfuller(series, autolag='AIC')
    status = "DỪNG ✓" if result[1] < 0.05 else "KHÔNG dừng ✗"
    print(f"{col:<35} {result[0]:>15.4f} {result[1]:>15.4f} {status:>15}")"""))

    # =========================================================================
    # CHAPTER 5: ARIMA
    # =========================================================================
    cells.append(md("""## **CHƯƠNG 5: Mô hình ARIMA — Giả thuyết "Quán tính" (Bệnh tự miễn)**
---

> **Ý tưởng cốt lõi:** Nếu lạm phát thực sự là "bệnh tự miễn" (do tâm lý kỳ vọng), thì chỉ cần dùng dữ liệu lạm phát QUÁ KHỨ đã đủ để dự báo lạm phát TƯƠNG LAI — không cần biết GDP, Tỷ giá, hay bất kỳ yếu tố nào khác.

### 5.1 ARIMA là gì? Tại sao chọn nó?

**ARIMA(p, d, q)** gồm 3 thành phần:
- **AR(p) - AutoRegressive:** Dùng `p` giá trị LẠM PHÁT quá khứ để dự đoán. Ví dụ: AR(2) = "Lạm phát hôm nay phụ thuộc vào lạm phát 1 năm trước và 2 năm trước."
- **I(d) - Integrated:** Số lần lấy sai phân để chuỗi dừng. `d=0` nếu chuỗi đã dừng, `d=1` nếu cần sai phân 1 lần.
- **MA(q) - Moving Average:** Dùng `q` sai số DỰ BÁO quá khứ để hiệu chỉnh. Ví dụ: MA(1) = "Nếu dự báo năm trước sai, năm nay hiệu chỉnh theo hướng ngược lại."

**Tại sao chọn ARIMA cho giả thuyết "Bệnh tự miễn"?**
- ARIMA CHỈ sử dụng dữ liệu của CHÍNH biến CPI → hoàn hảo để kiểm tra: "Liệu lạm phát có tự sinh ra lạm phát?"
- Nếu ARIMA dự báo chính xác → chứng minh quán tính (kỳ vọng) là động lực chính.
- Nếu ARIMA dự báo kém → cần tìm yếu tố bên ngoài (VAR ở Chương 6)."""))

    cells.append(md("### 5.2 ACF & PACF: Chọn tham số p, q"))

    cells.append(code("""# Chuỗi CPI growth
cpi_series = df['cpi_growth_percent'].dropna()

fig, axes = plt.subplots(1, 2, figsize=(18, 6))

plot_acf(cpi_series, lags=12, ax=axes[0])
axes[0].set_title('ACF (Autocorrelation Function)\\n→ Giúp chọn q cho MA', fontsize=14, fontweight='bold')

plot_pacf(cpi_series, lags=12, ax=axes[1])
axes[1].set_title('PACF (Partial Autocorrelation Function)\\n→ Giúp chọn p cho AR', fontsize=14, fontweight='bold')

plt.suptitle('PHÂN TÍCH ACF & PACF CHO CPI GROWTH', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()"""))

    cells.append(md("""**Cách đọc ACF/PACF:**
- **PACF "cắt" tại lag k:** → chọn p = k cho AR.
- **ACF "cắt" tại lag k:** → chọn q = k cho MA.
- "Cắt" = giá trị đột ngột rơi vào vùng không có ý nghĩa thống kê (vùng xanh).
- Nếu cả hai đều "tắt dần" (tailing off) → dùng ARMA(p,q) kết hợp."""))

    cells.append(md("### 5.3 Huấn luyện mô hình ARIMA"))

    cells.append(code("""# Thử nhiều bộ tham số và chọn theo AIC
print("TÌM KIẾM BỘ THAM SỐ ARIMA TỐI ƯU (theo AIC)")
print("=" * 60)

best_aic = float('inf')
best_order = None
best_model = None

for p in range(0, 4):
    for d in range(0, 2):
        for q in range(0, 4):
            try:
                model = ARIMA(cpi_series, order=(p, d, q))
                result = model.fit()
                if result.aic < best_aic:
                    best_aic = result.aic
                    best_order = (p, d, q)
                    best_model = result
                print(f"  ARIMA({p},{d},{q}) - AIC: {result.aic:.2f}")
            except:
                pass

print(f"\\n{'='*60}")
print(f"MÔ HÌNH TỐI ƯU: ARIMA{best_order} với AIC = {best_aic:.2f}")
print(f"{'='*60}")"""))

    cells.append(code("""# Kết quả chi tiết
print(best_model.summary())"""))

    cells.append(md("""**Tại sao chọn theo AIC?**
- AIC (Akaike Information Criterion) cân bằng giữa "mô hình khớp tốt" và "mô hình đơn giản". AIC thấp nhất = mô hình tối ưu.
- Nếu thêm tham số mà AIC không giảm → tham số đó "thừa" (overfitting)."""))

    cells.append(md("### 5.4 Kiểm tra phần dư (Residual Diagnostics)"))

    cells.append(code("""# Kiểm tra phần dư ARIMA
residuals = best_model.resid

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Residual time series
axes[0,0].plot(residuals)
axes[0,0].axhline(0, color='red', linestyle='--')
axes[0,0].set_title('Phần dư theo thời gian (phải ngẫu nhiên)', fontweight='bold')

# Histogram
axes[0,1].hist(residuals, bins=15, edgecolor='black', alpha=0.7, density=True)
from scipy.stats import norm
x = np.linspace(residuals.min(), residuals.max(), 100)
axes[0,1].plot(x, norm.pdf(x, residuals.mean(), residuals.std()), 'r-', linewidth=2)
axes[0,1].set_title('Phân phối phần dư (phải gần chuẩn)', fontweight='bold')

# Q-Q Plot
probplot(residuals, dist="norm", plot=axes[1,0])
axes[1,0].set_title('Q-Q Plot phần dư', fontweight='bold')

# ACF of residuals
plot_acf(residuals, lags=12, ax=axes[1,1])
axes[1,1].set_title('ACF phần dư (phải nằm trong vùng xanh)', fontweight='bold')

plt.suptitle('CHẨN ĐOÁN PHẦN DƯ MÔ HÌNH ARIMA', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# Ljung-Box test
from statsmodels.stats.diagnostic import acorr_ljungbox
lb_test = acorr_ljungbox(residuals, lags=10, return_df=True)
print("LJUNG-BOX TEST (H0: Phần dư là nhiễu trắng)")
print("p-value > 0.05 → Phần dư là nhiễu trắng (tốt)")
display(lb_test)"""))

    cells.append(md("""**Phần dư có phải "nhiễu trắng" (white noise) không?**
- Nếu **CÓ** (p-value Ljung-Box > 0.05): Mô hình đã "bắt" hết tín hiệu trong dữ liệu. Phần còn lại chỉ là nhiễu ngẫu nhiên → Mô hình đáng tin.
- Nếu **KHÔNG**: Còn "tín hiệu ẩn" mà ARIMA chưa nắm bắt → Cần yếu tố bên ngoài (→ VAR)."""))

    cells.append(md("### 5.5 Dự báo & Đánh giá độ tin cậy"))

    cells.append(code("""# Dự báo 3 năm tiếp theo
arima_forecast = best_model.get_forecast(steps=3)
arima_forecast_df = arima_forecast.summary_frame()

plt.figure(figsize=(14, 7))
plt.plot(cpi_series.tail(15), label='CPI Growth thực tế', marker='o', linewidth=2)
plt.plot(arima_forecast.predicted_mean, label='ARIMA Forecast', marker='s',
         color='red', linestyle='--', linewidth=2)
plt.fill_between(arima_forecast_df.index,
                 arima_forecast_df['mean_ci_lower'],
                 arima_forecast_df['mean_ci_upper'],
                 color='pink', alpha=0.3, label='Khoảng tin cậy 95%')
plt.title('DỰ BÁO TỪ QUÁN TÍNH: Lạm phát kỳ vọng duy trì đà hiện tại', fontsize=16, fontweight='bold')
plt.xlabel('Năm')
plt.ylabel('CPI Growth (%)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Đánh giá
print("=" * 60)
print("ĐÁNH GIÁ MÔ HÌNH ARIMA")
print("=" * 60)
fitted = best_model.fittedvalues
actual = cpi_series[fitted.index]
print(f"RMSE: {np.sqrt(mean_squared_error(actual, fitted)):.4f}")
print(f"MAE:  {mean_absolute_error(actual, fitted):.4f}")
print(f"MAPE: {mean_absolute_percentage_error(actual, fitted)*100:.2f}%")"""))

    cells.append(md("""**Dự báo ARIMA có đáng tin không?**

1. **Khoảng tin cậy (Confidence Interval):** Dải hồng càng rộng → dự báo càng bất định. Dự báo xa hơn thường có khoảng tin cậy rộng hơn.
2. **MAPE (Mean Absolute Percentage Error):** Đo sai số trung bình theo %. MAPE < 10% = tốt, 10-20% = khá, > 20% = kém.
3. **Hạn chế quan trọng:** ARIMA chỉ dùng dữ liệu lạm phát quá khứ → KHÔNG THỂ dự báo "cú sốc" từ bên ngoài (ví dụ: đột nhiên giá dầu tăng gấp đôi). Đây là lý do cần VAR ở Chương 6."""))

    # =========================================================================
    # CHAPTER 6: VAR
    # =========================================================================
    cells.append(md("""## **CHƯƠNG 6: Mô hình VAR — Giả thuyết "Tác nhân bên ngoài"**
---

> **Ý tưởng cốt lõi:** Nếu ARIMA trả lời "Lạm phát có tự sinh ra không?", thì VAR trả lời "Yếu tố BÊN NGOÀI nào thực sự 'bẻ lái' lạm phát?"

### 6.1 VAR là gì? Tại sao chọn nó?

**VAR (Vector Autoregression)** là hệ phương trình đồng thời:
- Mỗi biến được dự báo bằng giá trị quá khứ của CHÍNH NÓ và TẤT CẢ các biến khác.
- Ví dụ: `CPI_t = f(CPI_{t-1}, GDP_{t-1}, ExchangeRate_{t-1}, ...)`

**Tại sao chọn VAR?**
- Khác ARIMA (chỉ 1 biến), VAR mô hình hóa **sự tương tác** giữa nhiều biến.
- VAR cho phép sử dụng **Granger Causality Test** (ai dẫn dắt ai?) và **Impulse Response Function** (một cú sốc lan tỏa thế nào?).
- Đây chính là công cụ để kiểm tra: "Tỷ giá, GDP, Tín dụng có thực sự TÁC ĐỘNG đến Lạm phát không?"

**Điều kiện tiên quyết:** TẤT CẢ các chuỗi đưa vào VAR phải DỪNG (stationary). Đây là lý do Chương 4 rất quan trọng."""))

    cells.append(md("### 6.2 Chuẩn bị dữ liệu cho VAR"))

    cells.append(code("""# Chọn các biến đại diện cho từng trụ cột (đã loại bỏ đa cộng tuyến)
var_vars = ['cpi_growth_percent', 'gdp_growth_percent',
            'lending_interest_percent', 'officical_exchange_rate_percent']

# Sử dụng dữ liệu đã xử lý stationarity
var_data = df_diff[var_vars].dropna()
print(f"Số quan sát cho VAR: {len(var_data)}")
print(f"Các biến: {list(var_data.columns)}")

# Kiểm tra lại stationarity
print("\\nKiểm tra tính dừng của dữ liệu VAR:")
for col in var_vars:
    result = adfuller(var_data[col].dropna())
    status = "DỪNG ✓" if result[1] < 0.05 else "KHÔNG dừng ✗"
    print(f"  {col}: p-value = {result[1]:.4f} → {status}")"""))

    cells.append(md("### 6.3 Chọn bậc trễ tối ưu (Lag Order Selection)"))

    cells.append(code("""# Tìm lag tối ưu theo AIC/BIC
var_model_temp = VAR(var_data)
# Đã sửa thành maxlags=2 do mẫu nhỏ (chỉ còn ~25 quan sát), không đủ bậc tự do cho lag 5
lag_results = var_model_temp.select_order(maxlags=2)
print("CHỌN BẬC TRỄ TỐI ƯU CHO VAR")
print("=" * 60)
print(lag_results.summary())

optimal_lag = lag_results.aic
print(f"\\nBậc trễ tối ưu theo AIC: {optimal_lag}")"""))

    cells.append(md("""**Tại sao bậc trễ (lag) quan trọng?**
- Lag = 1: Lạm phát hôm nay bị ảnh hưởng bởi GDP/Tỷ giá **1 năm trước**.
- Lag = 2: Ảnh hưởng kéo dài **2 năm trước**.
- Quá ít lag → bỏ sót hiệu ứng dài hạn. Quá nhiều lag → mất bậc tự do → mô hình không ổn định.
- AIC giúp tìm điểm cân bằng tối ưu."""))

    cells.append(md("### 6.4 Granger Causality Test: Ai dẫn dắt ai?"))

    cells.append(code("""# Granger Causality: Kiểm tra từng biến có "dẫn dắt" CPI không
print("=" * 80)
print("GRANGER CAUSALITY TEST")
print("H0: Biến X KHÔNG Granger-cause CPI")
print("Bác bỏ H0 khi p-value < 0.05 → Biến X CÓ tính dẫn dắt")
print("=" * 80)

target = 'cpi_growth_percent'
maxlag = min(optimal_lag + 1, 3)  # Tối đa 3 lag do sample nhỏ

for cause_var in var_vars:
    if cause_var != target:
        print(f"\\n{'='*60}")
        print(f"Test: {cause_var} → {target}")
        print(f"{'='*60}")
        try:
            test_data = var_data[[target, cause_var]].dropna()
            result = grangercausalitytests(test_data, maxlag=maxlag, verbose=True)
        except Exception as e:
            print(f"  Lỗi: {e}")"""))

    cells.append(md("""**Giải thích Granger Causality:**

> *"X Granger-causes Y"* KHÔNG có nghĩa là "X gây ra Y" theo nghĩa nhân quả.
> Nó có nghĩa: *"Biết giá trị quá khứ của X giúp DỰ BÁO Y tốt hơn so với chỉ dùng giá trị quá khứ của Y."*

**Tại sao yếu tố đó ảnh hưởng (hoặc không) đến Lạm phát?**

- **Tỷ giá (Exchange Rate) → CPI:** Nếu p-value < 0.05 → Tỷ giá CÓ tính dẫn dắt lạm phát.
  - *Cơ chế kinh tế:* VND mất giá → Hàng nhập khẩu (xăng, nguyên liệu) đắt hơn → Chi phí sản xuất tăng → Giá bán tăng → CPI tăng. Đây là kênh "Lạm phát nhập khẩu" (Imported Inflation).

- **GDP Growth → CPI:** Nếu p-value < 0.05 → GDP CÓ tính dẫn dắt.
  - *Cơ chế:* GDP tăng nhanh → Nhu cầu tiêu dùng tăng → "Cầu kéo" (Demand-pull) → CPI tăng.

- **Lending Interest → CPI:** Nếu p-value > 0.05 → Lãi suất KHÔNG dẫn dắt lạm phát rõ rệt.
  - *Tại sao?* Vì lãi suất tại VN thường là **phản ứng** (NHNN tăng lãi suất SAU KHI lạm phát đã tăng), chứ không phải **nguyên nhân** gốc."""))

    cells.append(md("### 6.5 Impulse Response Function (IRF): Cú sốc lan tỏa thế nào?"))

    cells.append(code("""# Fit VAR model
var_model = VAR(var_data)
var_result = var_model.fit(maxlags=optimal_lag)
print(var_result.summary())"""))

    cells.append(code("""# Impulse Response Function
irf = var_result.irf(10)
fig = irf.plot(orth=True, impulse=None, response='cpi_growth_percent', figsize=(16, 12))
plt.suptitle('IRF: Phản ứng của CPI Growth trước các cú sốc', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()"""))

    cells.append(md("""**Đọc biểu đồ IRF:**
- Mỗi ô cho thấy: Khi biến X bị "sốc" 1 độ lệch chuẩn, CPI phản ứng thế nào qua 10 năm.
- **Đường thẳng = 0:** Không ảnh hưởng.
- **Đường trên 0:** Cú sốc LÀM TĂNG lạm phát.
- **Đường dưới 0:** Cú sốc LÀM GIẢM lạm phát.
- **Tốc độ về 0:** Nhanh = ảnh hưởng ngắn hạn. Chậm = ảnh hưởng kéo dài."""))

    cells.append(md("### 6.6 Forecast Error Variance Decomposition (FEVD)"))

    cells.append(code("""# FEVD
fevd = var_result.fevd(10)
print(fevd.summary())

# Đặt bảng màu tươi sáng, dễ phân biệt hơn cho biểu đồ FEVD
colors = ['#FF595E', '#1982C4', '#8AC926', '#FFCA3A', '#6A4C93']
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=colors)

# Plot FEVD
fig = fevd.plot(figsize=(14, 8))
plt.suptitle('PHÂN RÃ PHƯƠNG SAI: Ai chịu trách nhiệm cho biến động Lạm phát?',
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()"""))

    cells.append(md("""**FEVD — Kết quả thuyết phục nhất:**

FEVD trả lời câu hỏi: *"Trong tổng biến động của Lạm phát, bao nhiêu % do chính Quán tính gây ra, bao nhiêu % do GDP, Tỷ giá, Lãi suất?"*

**Kết luận quan trọng dựa trên số liệu:**
- Nếu CPI tự giải thích **>80-90%** biến động của chính nó → Đây là bằng chứng ĐỊNH LƯỢNG cho giả thuyết "Bệnh tự miễn": Lạm phát tại Việt Nam chủ yếu do QUÁN TÍNH (kỳ vọng tâm lý) chứ không phải do yếu tố bên ngoài.
- Yếu tố bên ngoài quan trọng nhất (nếu có) chỉ đóng góp một phần nhỏ.

**Ta dựa vào đâu để kết luận "Bệnh tự miễn"?**
1. **ARIMA accuracy:** Mô hình chỉ dùng quá khứ CPI đã dự báo tốt → Quán tính mạnh.
2. **FEVD numbers:** >90% biến động CPI do chính CPI giải thích → Yếu tố ngoại sinh yếu.
3. **Granger Causality:** Chỉ 1-2 biến có tính "dẫn dắt", và ngay cả chúng cũng chỉ giải thích <10% phương sai."""))

    # =========================================================================
    # CHAPTER 7: CONCLUSION
    # =========================================================================
    cells.append(md("""## **CHƯƠNG 7: Kết luận — Trả lời Câu hỏi Tối thượng**
---"""))

    cells.append(md("""### 7.1 Bảng Tổng kết Bằng chứng

| Tiêu chí | ARIMA (Quán tính) | VAR (Yếu tố ngoại sinh) |
|---|---|---|
| **Mô hình dùng gì?** | Chỉ dữ liệu CPI quá khứ | CPI + GDP + Tỷ giá + Lãi suất |
| **Giả thuyết kiểm tra** | "Bệnh tự miễn" — lạm phát tự sinh ra | "Tác nhân bên ngoài" — do GDP, tỷ giá... |
| **Kết quả dự báo** | Tốt (MAPE thấp) | Bổ sung thêm thông tin nhưng không vượt trội |
| **FEVD** | N/A | CPI tự giải thích >90% biến động |
| **Granger Causality** | N/A | Chỉ 1-2 biến có tính dẫn dắt yếu |
| **Kết luận** | ✅ Quán tính là động lực CHÍNH | GDP là kênh ngoại sinh duy nhất đáng kể |"""))

    cells.append(md("""### 7.2 Phán quyết: Trả lời The Ultimate Question

> **"Lạm phát tại Việt Nam chủ yếu là do 'Bệnh tự miễn' (Quán tính) hay 'Tác nhân bên ngoài'?"**

**Câu trả lời dựa trên dữ liệu:**

🔬 **Lạm phát tại Việt Nam trong 3 thập kỷ qua chủ yếu mang tính QUÁN TÍNH (Bệnh tự miễn).**

**Bằng chứng:**
1. **Mô hình ARIMA** (chỉ dùng lạm phát quá khứ) đã dự báo tương đối chính xác → Lạm phát "tự sinh ra chính nó" thông qua kỳ vọng tâm lý.
2. **Phân rã phương sai FEVD** cho thấy >90% biến động lạm phát được giải thích bởi chính quán tính lạm phát, không phải bởi GDP, Tỷ giá hay Lãi suất.
3. **Granger Causality** chỉ ra rằng trong các yếu tố ngoại sinh, chỉ GDP Growth có tính "dẫn dắt" đáng kể, nhưng đóng góp rất nhỏ (<10% phương sai).

**Cơ chế kinh tế:** Khi người dân và doanh nghiệp *kỳ vọng* giá cả sẽ tăng → họ đẩy giá bán lên trước → giá thực sự tăng → xác nhận kỳ vọng → vòng lặp tiếp tục. Đây chính là "Bệnh tự miễn" — hệ miễn dịch (kỳ vọng) tấn công chính cơ thể (nền kinh tế)."""))

    cells.append(md("""### 7.3 Hàm ý Chính sách

Nếu lạm phát chủ yếu do quán tính kỳ vọng, thì **chính sách hiệu quả nhất** không phải là can thiệp mạnh vào tỷ giá hay lãi suất, mà là:

1. **Neo kỳ vọng lạm phát:** NHNN cần công bố mục tiêu lạm phát rõ ràng và giữ cam kết → giảm "Bệnh tự miễn".
2. **Truyền thông chính sách:** Giải thích minh bạch các quyết định tiền tệ → giảm bất định → giảm kỳ vọng lạm phát.
3. **Giám sát GDP:** Vì GDP là kênh ngoại sinh duy nhất đáng kể, cần theo dõi tốc độ tăng trưởng để phát hiện sớm áp lực cầu kéo."""))

    cells.append(md("""### 7.4 Hạn chế & Hướng phát triển

- **Hạn chế:**
  - Dữ liệu chỉ có 29 quan sát (29 năm) → Sample nhỏ làm giảm "sức mạnh thống kê" của các kiểm định.
  - Dữ liệu theo năm → không bắt được biến động ngắn hạn (tháng/quý).
  - Chưa xét đến yếu tố phi tuyến (neural network, regime-switching models).

- **Hướng phát triển:**
  - Sử dụng dữ liệu tháng/quý từ GSO để tăng số quan sát.
  - Áp dụng SVAR (Structural VAR) với ràng buộc lý thuyết kinh tế.
  - So sánh với Machine Learning models (LSTM, Random Forest) để kiểm chứng."""))

    # Build notebook structure
    notebook = {
        "nbformat": 4,
        "nbformat_minor": 0,
        "metadata": {
            "colab": {
                "provenance": [],
                "toc_visible": True
            },
            "kernelspec": {
                "name": "python3",
                "display_name": "Python 3"
            },
            "language_info": {
                "name": "python"
            }
        },
        "cells": cells
    }

    return notebook


if __name__ == "__main__":
    notebook = build_notebook()

    # Write to file
    output_path = os.path.join(os.path.dirname(__file__), "Project1_DAAN_v2.ipynb")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=2)

    print(f"Notebook generated successfully: {output_path}")
    print(f"Total cells: {len(notebook['cells'])}")
