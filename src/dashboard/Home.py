import sys
from pathlib import Path

import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import clean_data, fit_var_model, get_cpi_fevd, setup_page

setup_page("Home", "📌")

st.title("Lạm phát Việt Nam: Quán tính hay tác nhân bên ngoài?")

st.markdown("""
> **Câu hỏi:** Lạm phát tại Việt Nam chủ yếu là do "Bệnh tự miễn" (quán tính/kỳ vọng)
> hay do "Tác nhân bên ngoài" (GDP, lãi suất, tỷ giá)?
""")

result, selected_lag, _, _ = fit_var_model()
fevd = get_cpi_fevd(result, periods=10)
cpi_col = "Quán tính tự thân (CPI)"
inertia_avg = fevd.loc["Kỳ 2":"Kỳ 10", cpi_col].mean()
external_avg = 100 - inertia_avg

col1, col2, col3 = st.columns(3)
col1.metric("Kết luận", "QUÁN TÍNH")
col2.metric("CPI tự giải thích", f"{inertia_avg:.1f}%")
col3.metric("Tác nhân bên ngoài", f"{external_avg:.1f}%")

st.success(
    "Câu trả lời dựa trên dữ liệu: Lạm phát tại Việt Nam trong 3 thập kỷ qua "
    "chủ yếu mang tính QUÁN TÍNH (Bệnh tự miễn)."
)

# ── PIPELINE DIAGRAM ────────────────────────────────────────────
# x range 0..1, node half-width = 0.13 so boxes are narrow
st.subheader("Pipeline Phân tích")

# (cx, cy, title, subtitle, fill_color, border_color)
NODES = [
    (0.50, 5.6, "📂 Dữ liệu Thô",       "dataset_project1.xlsx · 27 năm · 11 biến", "#1a3a5c", "#4a9fd5"),
    (0.50, 4.4, "🧹 Làm sạch",          "Nội suy missing · Giữ 4 biến",           "#1a3a5c", "#4a9fd5"),
    (0.50, 3.2, "📊 Kiểm định",         "ADF Test · VIF",                           "#1a4a1a", "#4ab04a"),
    (0.50, 2.0, "🤖 VAR(1)",           "Vector Autoregression · 4 biến",          "#4a1a1a", "#d05050"),
    (0.10, 0.8, "📉 Granger",          "Tính dẫn dắt",                             "#3a2a0a", "#c09030"),
    (0.50, 0.8, "📈 IRF",             "Phản ứng xung",                            "#3a2a0a", "#c09030"),
    (0.90, 0.8, "🔬 FEVD 10 kỳ",      "Phân rã phương sai",                       "#3a2a0a", "#e07020"),
    (0.50, -0.4, "✅ Kết luận",        f"CPI ≈ {inertia_avg:.1f}% → QUÁN TÍNH",       "#0a3a1a", "#30a060"),
]

EDGES = [(0,1),(1,2),(2,3),(3,4),(3,5),(3,6),(4,7),(5,7),(6,7)]

HW = 0.17   # half-width of each box
HH = 0.28   # half-height of each box

fig_pipe = go.Figure()

# Arrows
for si, di in EDGES:
    sx, sy = NODES[si][0], NODES[si][1]
    dx, dy = NODES[di][0], NODES[di][1]
    fig_pipe.add_annotation(
        x=dx, y=dy + HH,
        ax=sx, ay=sy - HH,
        xref="x", yref="y", axref="x", ayref="y",
        showarrow=True, arrowhead=2, arrowsize=1.2,
        arrowwidth=1.8, arrowcolor="#888888",
    )

# Nodes
for (cx, cy, title, subtitle, fill, border) in NODES:
    fig_pipe.add_shape(
        type="rect",
        x0=cx-HW, y0=cy-HH, x1=cx+HW, y1=cy+HH,
        line=dict(color=border, width=2),
        fillcolor=fill, opacity=0.95,
    )
    fig_pipe.add_annotation(
        x=cx, y=cy + 0.07,
        text=f"<b>{title}</b>",
        showarrow=False, font=dict(size=12, color="white"),
        xref="x", yref="y", align="center",
    )
    fig_pipe.add_annotation(
        x=cx, y=cy - 0.11,
        text=subtitle,
        showarrow=False, font=dict(size=9, color="#ccddee"),
        xref="x", yref="y", align="center",
    )

fig_pipe.update_layout(
    height=720,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis=dict(visible=False, range=[-0.08, 1.08]),
    yaxis=dict(visible=False, range=[-0.95, 6.1]),
    plot_bgcolor="#0e1117",
    paper_bgcolor="#0e1117",
)

st.plotly_chart(fig_pipe, use_container_width=True)

df = clean_data()
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df.index.year,
    y=df["cpi_growth_percent"],
    mode="lines+markers",
    name="CPI growth",
    line=dict(color="#003366", width=3),
))
fig.add_hline(y=df["cpi_growth_percent"].mean(), line_dash="dash", line_color="#e45756")
fig.update_layout(
    title="Chuỗi CPI growth: nền tảng để kiểm tra quán tính",
    xaxis_title="Năm",
    yaxis_title="CPI growth (%)",
    template="plotly_white",
    height=430,
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
Dashboard đã được tối giản thành 4 trang:

- **Data Exploration:** chỉ xem dữ liệu cần cho câu hỏi.
- **Stationarity Testing:** kiểm định ADF và VIF bắt buộc.
- **VAR Model:** VAR(1), dự báo ngắn hạn, FEVD 10 kỳ.
- **Conclusion:** phán quyết và hàm ý chính sách.
""")
