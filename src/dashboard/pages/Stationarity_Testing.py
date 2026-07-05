"""
Stationarity Testing — Chapter 4: ADF Test & Data Transformation
"""
import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils import setup_page, clean_data, run_adf_tests, ANALYSIS_VARS

# ---------------------------------------------------------------------------
setup_page("Stationarity Testing", "📉")
# ---------------------------------------------------------------------------

st.title("📉 Chương 4: Kiểm định Tính Dừng & Biến đổi Dữ liệu")

st.info(
    "**Tại sao phải kiểm tra tính dừng (Stationarity)?**\n\n"
    "Hãy tưởng tượng bạn muốn dự báo nhiệt độ ngày mai. "
    "Nếu bạn sống ở vùng nhiệt đới (nhiệt độ dao động quanh 30°C ổn định) → dễ dự báo. "
    "Nhưng nếu bạn sống ở nơi đang nóng lên liên tục (20°C → 25°C → 30°C → 35°C...) "
    "→ rất khó dự báo vì \"quy luật\" liên tục thay đổi.\n\n"
    "Tương tự, mô hình VAR CHỈ hoạt động đúng khi chuỗi dữ liệu \"dừng\" — "
    "tức là giá trị trung bình và phương sai **không thay đổi** theo thời gian.",
    icon="💡"
)

df = clean_data()

st.markdown("## 4.1 Kiểm định ADF (Augmented Dickey-Fuller)")

with st.expander("📖 Lý thuyết: ADF Test", expanded=False):
    st.markdown("""
    **Augmented Dickey-Fuller (ADF)** là kiểm định phổ biến nhất cho tính dừng:
    - **H₀:** Chuỗi **KHÔNG dừng** (có unit root)
    - **H₁:** Chuỗi **dừng** (stationary)
    - **Quy tắc:** Bác bỏ H₀ khi **p-value < 0.05**
    """)

adf_before = run_adf_tests(df, ANALYSIS_VARS)

st.markdown("### Kết quả ADF — Dữ liệu Gốc")

def style_adf(row):
    if '✅' in row['Kết luận']:
        return ['background-color: #E8F5E9; color: black'] * len(row)
    return ['background-color: #FFEBEE; color: black'] * len(row)

adf_display = adf_before.copy()
adf_display['Kết luận'] = adf_display['Dừng'].apply(lambda x: '✅ DỪNG' if x else '❌ KHÔNG dừng')
st.dataframe(adf_display[['Biến', 'ADF Statistic', 'P-value', 'Kết luận']].style.apply(style_adf, axis=1),
             use_container_width=True, hide_index=True)

n_stationary = adf_before['Dừng'].sum()
n_non_stationary = len(adf_before) - n_stationary
col_m1, col_m2 = st.columns(2)
col_m1.metric("Chuỗi DỪNG ✅", n_stationary)
col_m2.metric("Chuỗi KHÔNG dừng ❌", n_non_stationary)

st.markdown("""
**Giải thích:**
- **Biến dừng** (Growth Rate %): Dao động quanh giá trị trung bình → mean-reversion.
- **Biến không dừng** (Index tích lũy): Giá trị tuyệt đối luôn tăng theo thời gian.
""")

st.divider()
st.markdown("## 4.2 Sai phân Bậc 1 & Kiểm định lại")

st.markdown("**Hành động:** Lấy sai phân bậc 1 (`diff()`) cho các chuỗi không dừng.")

non_stationary_vars = adf_before.loc[~adf_before['Dừng'], 'Biến'].tolist()

with st.expander(f"📋 Các biến cần sai phân ({len(non_stationary_vars)} biến)"):
    for v in non_stationary_vars:
        st.markdown(f"- `{v}`")

df_diff = df[ANALYSIS_VARS].copy()
for col in non_stationary_vars:
    df_diff[col] = df_diff[col].diff()
df_diff = df_diff.dropna()

adf_after = run_adf_tests(df_diff, ANALYSIS_VARS)

st.markdown("### Kết quả ADF — Sau Sai phân Bậc 1")
adf_after_display = adf_after.copy()
adf_after_display['Kết luận'] = adf_after_display['Dừng'].apply(lambda x: '✅ DỪNG' if x else '❌ KHÔNG dừng')
st.dataframe(adf_after_display[['Biến', 'ADF Statistic', 'P-value', 'Kết luận']].style.apply(style_adf, axis=1),
             use_container_width=True, hide_index=True)

n_stat_after = adf_after['Dừng'].sum()
st.success(f"**Sau sai phân:** {n_stat_after}/{len(ANALYSIS_VARS)} chuỗi đã dừng → sẵn sàng cho VAR!", icon="✅")

st.divider()
st.markdown("## 📊 So sánh: Chuỗi Gốc vs. Sau Sai phân")

selected_var = st.selectbox(
    "Chọn biến để so sánh:",
    non_stationary_vars if non_stationary_vars else ANALYSIS_VARS,
    format_func=lambda x: f"{x} {'(đã sai phân)' if x in non_stationary_vars else ''}"
)

fig_compare = make_subplots(rows=2, cols=1,
    subplot_titles=(f"Chuỗi Gốc: {selected_var}", f"Sau Sai phân Bậc 1: Δ{selected_var}"),
    vertical_spacing=0.15)

fig_compare.add_trace(
    go.Scatter(x=df.index, y=df[selected_var], mode='lines+markers',
               line=dict(color='#E24A33', width=2), marker=dict(size=4), name='Gốc'),
    row=1, col=1)

diff_series = df[selected_var].diff().dropna()
fig_compare.add_trace(
    go.Scatter(x=diff_series.index, y=diff_series, mode='lines+markers',
               line=dict(color='#2EC4B6', width=2), marker=dict(size=4), name='Sai phân'),
    row=2, col=1)
fig_compare.add_hline(y=0, line_dash="dash", line_color="gray", row=2, col=1)

orig_mean = df[selected_var].mean()
diff_mean = diff_series.mean()
fig_compare.add_hline(y=orig_mean, line_dash="dot", line_color="#E24A33",
                      annotation_text=f"Mean={orig_mean:.1f}", row=1, col=1)
fig_compare.add_hline(y=diff_mean, line_dash="dot", line_color="#2EC4B6",
                      annotation_text=f"Mean={diff_mean:.1f}", row=2, col=1)

fig_compare.update_layout(height=550, template="plotly_white", showlegend=False)
st.plotly_chart(fig_compare, use_container_width=True)

st.markdown("""
**Quan sát:**
- **Chuỗi gốc** (trên): Xu hướng tăng rõ rệt → mean thay đổi → KHÔNG dừng.
- **Sau sai phân** (dưới): Dao động quanh mean ≈ 0 → ổn định → DỪNG.
""")
