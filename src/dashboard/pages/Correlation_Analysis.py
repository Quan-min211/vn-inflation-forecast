"""
Correlation Analysis — Chapter 3: Relationship Analysis & Hypothesis Testing
"""
import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils import setup_page, clean_data, compute_vif, ANALYSIS_VARS

# ---------------------------------------------------------------------------
setup_page("Correlation Analysis", "🔗")
# ---------------------------------------------------------------------------

st.title("🔗 Chương 3: Phân tích Mối quan hệ & Kiểm định Giả thuyết")
st.info(
    "**Câu hỏi cốt lõi:** Yếu tố nào THỰC SỰ có mối liên hệ với Lạm phát? "
    "Mối liên hệ đó mạnh hay yếu? Có thể tin cậy được không?",
    icon="🤔"
)

df = clean_data()

# ===== 3.1: Correlation Heatmap =====
st.markdown("## 3.1 Ma trận Tương quan Pearson")

with st.expander("📖 Lý thuyết: Correlation Pearson là gì?", expanded=False):
    st.markdown("""
    **Hệ số tương quan Pearson (r)** đo mức độ và chiều hướng của mối quan hệ **tuyến tính** giữa hai biến:
    - **r ≈ +1:** Tương quan thuận mạnh (cùng tăng cùng giảm).
    - **r ≈ -1:** Tương quan nghịch mạnh (một tăng thì cái kia giảm).
    - **r ≈ 0:** Không có mối liên hệ tuyến tính.

    > **Lưu ý:** Tương quan ≠ Nhân quả. Hai biến có thể tương quan cao nhưng không có quan hệ nhân quả trực tiếp.
    """)

corr_matrix = df[ANALYSIS_VARS].corr()

mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)
corr_masked = corr_matrix.copy()
corr_masked = corr_masked.where(~mask)

short_labels = {
    'cpi_growth_percent': 'CPI Growth',
    'gdp_deflator_percent': 'GDP Deflator',
    'gdp_growth_percent': 'GDP Growth',
    'unemployment_rate': 'Unemployment',
    'domestic_credit_index': 'Credit Index',
    'lending_interest_percent': 'Lending Rate',
    'officical_exchange_rate_percent': 'Exchange Rate',
    'import_index': 'Import Index',
    'export_index': 'Export Index'
}
display_labels = [short_labels.get(v, v) for v in ANALYSIS_VARS]

fig_corr = go.Figure(data=go.Heatmap(
    z=corr_masked.values,
    x=display_labels,
    y=display_labels,
    colorscale='RdBu_r',
    zmid=0, zmin=-1, zmax=1,
    text=np.where(mask, '', corr_matrix.values.round(2).astype(str)),
    texttemplate="%{text}",
    textfont=dict(size=11),
    hovertemplate="<b>%{x}</b> vs <b>%{y}</b><br>Correlation: %{z:.3f}<extra></extra>",
    colorbar=dict(title="Pearson r")
))
fig_corr.update_layout(
    title="Ma trận Tương quan Pearson giữa các biến Kinh tế Vĩ mô",
    height=600, xaxis=dict(tickangle=45), template="plotly_white"
)
st.plotly_chart(fig_corr, use_container_width=True)

st.markdown("### 📝 Phát hiện Quan trọng")
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1:
    st.markdown("""
    <div style="background: #E8F5E9; padding: 1rem; border-radius: 8px; border-left: 4px solid #4CAF50;">
        <strong>CPI ↔ GDP Deflator</strong><br>Tương quan thuận <strong>cao</strong><br>
        <em>Cả hai đo lường lạm phát → dữ liệu nhất quán</em>
    </div>
    """, unsafe_allow_html=True)
with col_c2:
    st.markdown("""
    <div style="background: #FFF3E0; padding: 1rem; border-radius: 8px; border-left: 4px solid #FF9800;">
        <strong>CPI ↔ Lending Rate</strong><br>Tương quan thuận<br>
        <em>Lạm phát tăng → NHNN tăng lãi suất (phản ứng chính sách)</em>
    </div>
    """, unsafe_allow_html=True)
with col_c3:
    st.markdown("""
    <div style="background: #FFEBEE; padding: 1rem; border-radius: 8px; border-left: 4px solid #F44336;">
        <strong>Credit ↔ Import ↔ Export ↔ ExRate</strong><br>Tương quan <strong>rất cao</strong><br>
        <em>⚠️ CẢNH BÁO: Đa cộng tuyến!</em>
    </div>
    """, unsafe_allow_html=True)

# ===== 3.2: VIF =====
st.divider()
st.markdown("## 3.2 Kiểm tra Đa cộng tuyến (VIF)")

with st.expander("📖 Lý thuyết: VIF là gì?", expanded=False):
    st.markdown("""
    **VIF (Variance Inflation Factor)** đo mức độ "trùng lặp thông tin" giữa các biến:

    | VIF | Mức độ | Hành động |
    |:---:|:---|:---|
    | **> 10** | Đa cộng tuyến **nghiêm trọng** 🔴 | Phải loại bỏ hoặc biến đổi biến |
    | **> 5** | Đa cộng tuyến **cần lưu ý** 🟠 | Cân nhắc kỹ khi đưa vào mô hình |
    | **< 5** | **Chấp nhận được** 🟢 | An toàn |

    **Hậu quả nếu bỏ qua:** Mô hình VAR sẽ cho hệ số "ảo" — kết luận sai về yếu tố nào thực sự ảnh hưởng lạm phát.
    """)

vif_df = compute_vif(df, ANALYSIS_VARS)
vif_df['Color'] = vif_df['VIF'].apply(lambda v: '#F44336' if v > 10 else ('#FF9800' if v > 5 else '#4CAF50'))
vif_df['Status'] = vif_df['VIF'].apply(lambda v: 'Nghiêm trọng' if v > 10 else ('Cần lưu ý' if v > 5 else 'An toàn'))
vif_df['Short'] = vif_df['Variable'].map(short_labels)

fig_vif = go.Figure()
fig_vif.add_trace(go.Bar(
    y=vif_df['Short'], x=vif_df['VIF'], orientation='h',
    marker_color=vif_df['Color'], text=vif_df['VIF'].round(1), textposition='outside',
    hovertemplate="<b>%{y}</b><br>VIF: %{x:.2f}<extra></extra>"
))
fig_vif.add_vline(x=10, line_dash="dash", line_color="red", annotation_text="Ngưỡng nguy hiểm (VIF=10)")
fig_vif.add_vline(x=5, line_dash="dash", line_color="orange", annotation_text="Ngưỡng cảnh báo (VIF=5)")
fig_vif.update_layout(title="Kiểm tra Đa cộng tuyến (VIF)", xaxis_title="VIF Score",
                      height=450, template="plotly_white")
st.plotly_chart(fig_vif, use_container_width=True)

with st.expander("📋 Bảng chi tiết VIF"):
    st.dataframe(vif_df[['Variable', 'VIF', 'Status']].reset_index(drop=True),
                 use_container_width=True, hide_index=True)

st.warning(
    "**Kết luận VIF:** Các biến Index (Credit, Import, Export, Exchange Rate) có VIF rất cao "
    "→ mang thông tin \"trùng lặp\" vì đều phản ánh xu hướng tăng trưởng dài hạn. "
    "**Hành động:** Chọn lọc biến cẩn thận cho VAR + sử dụng dữ liệu đã sai phân.",
    icon="⚠️"
)
