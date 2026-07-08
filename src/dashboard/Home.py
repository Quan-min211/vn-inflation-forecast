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
