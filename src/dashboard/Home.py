"""
Home — Chapter 1: Project Introduction
Entry point for the Streamlit multipage dashboard.
"""
import streamlit as st
import sys
from pathlib import Path

# Ensure utils is importable
sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import setup_page

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
setup_page("Home", "📈")

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown("""
<div style="text-align: center; padding: 1rem 0;">
    <p style="font-size: 0.9rem; color: #888;">BỘ GIÁO DỤC VÀ ĐÀO TẠO</p>
    <p style="font-size: 1rem; font-weight: bold;">TRƯỜNG ĐẠI HỌC CÔNG NGHỆ KỸ THUẬT THÀNH PHỐ HỒ CHÍ MINH</p>
    <p style="font-size: 0.9rem;">KHOA CÔNG NGHỆ THÔNG TIN</p>
</div>
""", unsafe_allow_html=True)

st.title("📈 Phân tích các Yếu tố Vĩ mô Tác động đến Lạm phát tại Việt Nam")
st.caption("Giai đoạn 1996 – 2022 | Dự báo xu hướng bằng Mô hình Chuỗi thời gian")

col1, col2, col3 = st.columns(3)
col1.markdown("**Môn học:** Phân tích Dữ liệu")
col2.markdown("**Lớp:** DAAN436277_02")
col3.markdown("**GVHD:** ThS. Trần Trọng Bình")

st.divider()

# ---------------------------------------------------------------------------
# Team
# ---------------------------------------------------------------------------
with st.expander("👥 Thành viên Nhóm 02", expanded=False):
    team_data = {
        "STT": [1, 2, 3, 4],
        "Họ và tên": ["Đỗ Kiến Hưng", "Trần Minh Khánh", "Nguyễn Đặng Quốc Anh", "Phạm Minh Quân"],
        "MSSV": ["23133030", "23133035", "23133004", "23133060"]
    }
    st.table(team_data)

# ---------------------------------------------------------------------------
# The Ultimate Question
# ---------------------------------------------------------------------------
st.markdown("## 🎯 THE ULTIMATE QUESTION")

st.info(
    '**"Trong 3 thập kỷ qua, Lạm phát tại Việt Nam chủ yếu là do '
    "'Bệnh tự miễn' (Quán tính tự sinh ra do tâm lý kỳ vọng) "
    "hay do 'Tác nhân bên ngoài' (Tỷ giá, Tín dụng, Tăng trưởng GDP)? "
    'Cần can thiệp vào đâu để kiểm soát nó?"*',
    icon="❓"
)

st.markdown("""
Câu hỏi này được cụ thể hóa thành **hai giả thuyết** kiểm chứng bằng định lượng:
""")

col_h1, col_h2 = st.columns(2)

with col_h1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1B3A4B 0%, #2C5F7C 100%);
                color: white; padding: 1.5rem; border-radius: 12px; height: 100%;">
        <h3 style="color: #FFD700;">H1: "Bệnh tự miễn"</h3>
        <p>Lạm phát VN chủ yếu do <strong>quán tính nội sinh</strong> — kỳ vọng tâm lý tạo vòng lặp tự củng cố.</p>
        <p style="font-size: 0.85rem; opacity: 0.9;"><em>Kiểm chứng: FEVD — CPI tự giải thích >80% phương sai</em></p>
    </div>
    """, unsafe_allow_html=True)

with col_h2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2EC4B6 0%, #1A936F 100%);
                color: white; padding: 1.5rem; border-radius: 12px; height: 100%;">
        <h3 style="color: #FFD700;">H2: "Tác nhân bên ngoài"</h3>
        <p>Lạm phát VN chủ yếu do <strong>yếu tố kinh tế vĩ mô</strong> bên ngoài chi phối (tỷ giá, tín dụng, GDP).</p>
        <p style="font-size: 0.85rem; opacity: 0.9;"><em>Kiểm chứng: FEVD — ngoại sinh giải thích >20% phương sai</em></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")  # spacing

# ---------------------------------------------------------------------------
# 4 Pillars
# ---------------------------------------------------------------------------
st.markdown("## 🏛️ Cơ sở Kinh tế học: 4 Trụ cột Vĩ mô")

st.markdown("""
Tập dữ liệu **11 biến** được chọn đại diện cho **4 trụ cột** của nền kinh tế vĩ mô.
Mỗi trụ cột đại diện cho một **kênh truyền dẫn lạm phát** khác nhau:
""")

tab1, tab2, tab3, tab4 = st.tabs([
    "💰 Giá cả",
    "📈 Tăng trưởng",
    "🏦 Tiền tệ",
    "🌐 Đối ngoại"
])

with tab1:
    st.markdown("### Trụ cột Giá cả — Đo lường bệnh lý")
    st.markdown("""
    | Biến | Ý nghĩa |
    |:---|:---|
    | `cpi_growth_percent` | Tốc độ tăng CPI hàng năm (%) — **TARGET** |
    | `gdp_deflator_percent` | Tốc độ tăng GDP Deflator (%) |
    """)
    st.success(
        "**Tại sao?** CPI đo giá cả từ phía **tiêu dùng**, GDP Deflator đo từ phía **sản xuất**. "
        "Khi cả hai cùng tăng → lạm phát là \"thật\", không phải do sự kiện cục bộ."
    )

with tab2:
    st.markdown("### Trụ cột Tăng trưởng — Áp lực Cầu kéo (Demand-pull)")
    st.markdown("""
    | Biến | Ý nghĩa |
    |:---|:---|
    | `gdp_growth_percent` | Tốc độ tăng trưởng GDP thực (%) |
    | `unemployment_rate` | Tỷ lệ thất nghiệp (%) |
    """)
    st.success(
        "**Tại sao?** Theo lý thuyết **Đường cong Phillips**: GDP tăng nhanh → thất nghiệp giảm "
        "→ áp lực tăng lương → giá cả tăng. Đây là kênh \"Cầu kéo\"."
    )

with tab3:
    st.markdown("### Trụ cột Tiền tệ — Bơm tiền & Lãi suất (Monetary channel)")
    st.markdown("""
    | Biến | Ý nghĩa |
    |:---|:---|
    | `domestic_credit_index` | Chỉ số tín dụng nội địa (Index) |
    | `lending_interest_percent` | Lãi suất cho vay (%) |
    """)
    st.success(
        "**Tại sao?** Tín dụng mở rộng + lãi suất giảm → vay nhiều hơn "
        "→ tiền trong nền kinh tế tăng → giá cả tăng. Đây là kênh \"Tiền tệ\"."
    )

with tab4:
    st.markdown("### Trụ cột Đối ngoại — Cú sốc ngoại sinh (Cost-push)")
    st.markdown("""
    | Biến | Ý nghĩa |
    |:---|:---|
    | `officical_exchange_rate_percent` | Tỷ giá hối đoái chính thức (Index) |
    | `import_index` | Chỉ số giá trị nhập khẩu (Index) |
    | `export_index` | Chỉ số giá trị xuất khẩu (Index) |
    """)
    st.success(
        "**Tại sao?** VND mất giá → hàng nhập khẩu (xăng, nguyên liệu) đắt hơn "
        "→ chi phí sản xuất tăng → giá bán tăng. Đây là kênh \"Chi phí đẩy\"."
    )

# ---------------------------------------------------------------------------
# Navigation guide
# ---------------------------------------------------------------------------
st.divider()
st.markdown("## 🗺️ Hướng dẫn Điều hướng")
st.markdown("""
Sử dụng **thanh điều hướng bên trái** (sidebar) để truy cập từng chương phân tích:

| Trang | Nội dung |
|:---|:---|
| **Data Exploration** | EDA, Missing Values, Xu hướng 4 Trụ cột |
| **Correlation Analysis** | Correlation Heatmap, VIF (Đa cộng tuyến) |
| **Stationarity Testing** | ADF Test, Differencing, Re-test |
| **VAR Model** | Granger Causality, IRF, FEVD |
| **Conclusion** | Phán quyết Ultimate Question, Hàm ý Chính sách |
""")
