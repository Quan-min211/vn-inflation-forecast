"""
VAR Model — Chapter 5: Vector Autoregression Analysis
"""
import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils import (setup_page, fit_var_model, prepare_var_data,
                   run_granger_tests, VAR_VARS, VAR_LABELS_VN)

# ---------------------------------------------------------------------------
setup_page("VAR Model", "🤖")
# ---------------------------------------------------------------------------

st.title("🤖 Chương 5: Mô hình VAR — Phân tích Tác nhân & Quán tính Lạm phát")

st.info(
    "**Ý tưởng cốt lõi:** VAR (Vector Autoregression) cho phép đồng thời trả lời HAI câu hỏi:\n\n"
    '1. **"Lạm phát có tự sinh ra chính nó không?"** → FEVD: CPI tự giải thích >90% → quán tính chủ đạo.\n\n'
    '2. **"Yếu tố BÊN NGOÀI nào bẻ lái lạm phát?"** → Granger Causality + IRF: kênh truyền dẫn đáng kể.',
    icon="🧠"
)

with st.expander("📖 Lý thuyết: VAR là gì? Tại sao chọn nó?", expanded=False):
    st.markdown("""
    **VAR (Vector Autoregression)** là hệ phương trình đồng thời:
    - Mỗi biến được dự báo bằng giá trị quá khứ của **CHÍNH NÓ** và **TẤT CẢ** các biến khác.
    - Ví dụ: `CPI_t = f(CPI_{t-1}, GDP_{t-1}, ExchangeRate_{t-1}, ...)`

    **Tại sao chọn VAR?**
    - Mô hình hóa **sự tương tác** giữa nhiều biến kinh tế vĩ mô cùng lúc.
    - Cho phép: **Granger Causality** (ai dẫn dắt ai?), **IRF** (cú sốc lan tỏa thế nào?),
      **FEVD** (ai chịu trách nhiệm cho biến động?).

    **Điều kiện tiên quyết:** TẤT CẢ các chuỗi phải **DỪNG** (stationary).
    """)

var_result, optimal_lag, var_data = fit_var_model()

st.markdown("## 5.2 – 5.3 Chuẩn bị Dữ liệu & Chọn Bậc trễ")

col_info1, col_info2, col_info3 = st.columns(3)
col_info1.metric("Số quan sát", len(var_data))
col_info2.metric("Số biến", len(VAR_VARS))
col_info3.metric("Bậc trễ tối ưu (AIC)", optimal_lag)

var_table = pd.DataFrame({
    'Biến': VAR_VARS,
    'Đại diện cho': ['Trụ cột Giá cả (Target)', 'Trụ cột Tăng trưởng',
                     'Trụ cột Tiền tệ', 'Trụ cột Đối ngoại'],
    'Nhãn': [VAR_LABELS_VN[v] for v in VAR_VARS]
})
st.dataframe(var_table, use_container_width=True, hide_index=True)

with st.expander("📖 Tại sao bậc trễ (lag) quan trọng?"):
    st.markdown("""
    - **Lag = 1:** Lạm phát bị ảnh hưởng bởi GDP/Tỷ giá **1 năm trước**.
    - **Lag = 2:** Ảnh hưởng kéo dài **2 năm trước**.
    - Quá ít lag → bỏ sót hiệu ứng. Quá nhiều lag → mất bậc tự do.
    - `maxlags=2` do mẫu nhỏ (~25 quan sát sau differencing).
    """)

# ===== 5.4: Granger Causality =====
st.divider()
st.markdown("## 5.4 Kiểm định Nhân quả Granger")

with st.expander("📖 Lý thuyết: Granger Causality", expanded=False):
    st.markdown("""
    > *"X Granger-causes Y"* **KHÔNG** có nghĩa "X gây ra Y".
    > Nó có nghĩa: *"Biết quá khứ X giúp **DỰ BÁO** Y tốt hơn."*

    - **H₀:** Biến X KHÔNG Granger-cause CPI
    - **Bác bỏ H₀ khi:** p-value < 0.05
    """)

granger_results = run_granger_tests(var_data.values, list(var_data.columns), optimal_lag)
granger_df = pd.DataFrame(granger_results)

def style_granger(row):
    if '✅' in row['Kết luận']:
        return ['background-color: #E8F5E9; color: black'] * len(row)
    return ['background-color: #FFEBEE; color: black'] * len(row)

granger_display = granger_df.copy()
granger_display['Kết luận'] = granger_display['Granger-cause CPI'].apply(
    lambda x: '✅ CÓ dẫn dắt' if x else '❌ KHÔNG dẫn dắt')

st.dataframe(granger_display[['Nhãn', 'F-statistic', 'P-value', 'Best Lag', 'Kết luận']].style.apply(
    style_granger, axis=1), use_container_width=True, hide_index=True)

fig_gc = go.Figure()
for _, row in granger_df.iterrows():
    color = '#4CAF50' if row['Granger-cause CPI'] else '#F44336'
    fig_gc.add_trace(go.Bar(
        x=[row['P-value']], y=[row['Nhãn']], orientation='h',
        marker_color=color, text=f"p={row['P-value']:.4f}",
        textposition='outside', showlegend=False))
fig_gc.add_vline(x=0.05, line_dash="dash", line_color="red", annotation_text="α = 0.05")
fig_gc.update_layout(title="Granger Causality: P-values", xaxis_title="P-value",
                     height=300, template="plotly_white")
st.plotly_chart(fig_gc, use_container_width=True)

st.markdown("### 📝 Giải thích Cơ chế Kinh tế")
col_g1, col_g2, col_g3 = st.columns(3)
with col_g1:
    st.markdown("**Tỷ giá → CPI**\n\nVND mất giá → nhập khẩu đắt → chi phí tăng → CPI tăng. Kênh: *Lạm phát nhập khẩu*")
with col_g2:
    st.markdown("**GDP Growth → CPI**\n\nGDP tăng nhanh → nhu cầu tăng → *Cầu kéo* → CPI tăng.")
with col_g3:
    st.markdown("**Lending Rate → CPI**\n\nLãi suất là **phản ứng** (NHNN tăng SAU KHI lạm phát tăng), không phải nguyên nhân gốc.")

# ===== 5.5: IRF =====
st.divider()
st.markdown("## 5.5 Hàm Phản ứng Xung kích (IRF)")

with st.expander("📖 Lý thuyết: IRF là gì?"):
    st.markdown("""
    **IRF:** Khi biến X bị "sốc" 1 độ lệch chuẩn, CPI phản ứng thế nào qua thời gian?
    - **Đường > 0:** Cú sốc LÀM TĂNG lạm phát.
    - **Đường < 0:** Cú sốc LÀM GIẢM lạm phát.
    - **Tốc độ về 0:** Nhanh = ngắn hạn. Chậm = kéo dài.
    """)

irf = var_result.irf(10)
fig_irf, axes_irf = plt.subplots(2, 2, figsize=(14, 10))
plt.style.use('ggplot')
cpi_idx_irf = list(var_data.columns).index('cpi_growth_percent')
periods = np.arange(11)

for idx, var_name in enumerate(VAR_VARS):
    row_i, col_i = divmod(idx, 2)
    ax = axes_irf[row_i, col_i]
    impulse_idx = list(var_data.columns).index(var_name)
    response = irf.irfs[:, cpi_idx_irf, impulse_idx]
    ax.plot(periods, response, color='#1B3A4B', linewidth=2.5, marker='o', markersize=4)
    ax.fill_between(periods, response, alpha=0.15, color='#1B3A4B')
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
    ax.set_title(f"Cú sốc: {VAR_LABELS_VN[var_name]}", fontsize=12, fontweight='bold')
    ax.set_xlabel("Kỳ (Periods)")
    ax.set_ylabel("Phản ứng CPI")
    ax.grid(True, alpha=0.3)

plt.suptitle("IRF: Phản ứng của CPI Growth trước các cú sốc", fontsize=16, fontweight='bold')
plt.tight_layout()
st.pyplot(fig_irf)
plt.close()

# ===== 5.6-5.7: FEVD =====
st.divider()
st.markdown("## 5.6 – 5.7 Phân rã Phương sai (FEVD)")

st.markdown('FEVD trả lời: *"Bao nhiêu % biến động CPI do Quán tính, bao nhiêu % do GDP, Tỷ giá, Lãi suất?"*')

fevd = var_result.fevd(10)
cpi_idx = list(var_data.columns).index('cpi_growth_percent')
fevd_cpi = fevd.decomp[:, cpi_idx, :] * 100
n_periods = fevd_cpi.shape[0]
labels = [VAR_LABELS_VN.get(c, c) for c in var_data.columns]
bar_colors = ['#1B3A4B', '#2EC4B6', '#FF6B6B', '#C0C0C0']

fig_fevd = go.Figure()
for j, (label, color) in enumerate(zip(labels, bar_colors)):
    values = fevd_cpi[:, j]
    fig_fevd.add_trace(go.Bar(
        x=[f"Kỳ {i+1}" for i in range(n_periods)], y=values,
        name=label, marker_color=color,
        text=[f"{v:.1f}%" for v in values], textposition='inside',
        textfont=dict(size=10, color='white' if j == 0 else 'black'),
        hovertemplate=f"<b>{label}</b><br>Đóng góp: %{{y:.2f}}%<extra></extra>"))

fig_fevd.update_layout(
    barmode='stack',
    title=dict(text="PHÂN RÃ PHƯƠNG SAI SAI SỐ DỰ BÁO CỦA BIẾN LẠM PHÁT (FEVD)<br>"
                    "<sup>Giải mã động lực \"Bệnh tự miễn\" qua 10 kỳ</sup>", font_size=16),
    xaxis_title="Chu kỳ dự báo (Periods)", yaxis_title="Tỷ lệ đóng góp (%)",
    yaxis=dict(range=[0, 110]), height=550,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5,
                title="Nguồn gốc cú sốc:"), template="plotly_white")

for i in range(n_periods):
    cpi_pct = fevd_cpi[i, cpi_idx]
    external_pct = 100 - cpi_pct
    if external_pct > 0.5:
        fig_fevd.add_annotation(x=f"Kỳ {i+1}", y=105,
            text=f"Ngoại sinh: {external_pct:.1f}%", showarrow=False,
            font=dict(size=9, color='#2EC4B6', family='Arial Black'))

st.plotly_chart(fig_fevd, use_container_width=True)

with st.expander("📋 Bảng Số liệu FEVD"):
    fevd_df = pd.DataFrame(fevd_cpi, columns=labels,
                           index=[f"Kỳ {i+1}" for i in range(n_periods)]).round(2)
    st.dataframe(fevd_df, use_container_width=True)

st.markdown("### 📝 Đọc Biểu đồ FEVD")
st.markdown("""
- **Phần xanh đậm (Quán tính CPI):** % biến động do lạm phát quá khứ — "Bệnh tự miễn".
- **Kỳ 1:** CPI tự giải thích 100% (cú sốc chưa lan truyền).
- **Từ Kỳ 2:** Phần xanh đậm >90% → **Quán tính áp đảo**.
""")

cpi_avg = fevd_cpi[1:, cpi_idx].mean()
external_avg = 100 - cpi_avg
st.error(
    f"**KẾT LUẬN:** Quán tính CPI trung bình (Kỳ 2–10): **{cpi_avg:.1f}%** | "
    f"Ngoại sinh: **{external_avg:.1f}%** → Lạm phát VN là **\"Bệnh tự miễn\"**!",
    icon="🔥")
