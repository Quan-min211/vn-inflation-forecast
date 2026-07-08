import sys
from pathlib import Path

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils import VAR_LABELS_VN, VAR_VARS, clean_data, load_raw_data, setup_page

setup_page("Data Exploration", "📈")

st.title("Dữ liệu tối giản cho câu hỏi nghiên cứu")

df_raw = load_raw_data()
df = clean_data()

col1, col2, col3 = st.columns(3)
col1.metric("Số năm", df.shape[0])
col2.metric("Biến dùng trong VAR", len(VAR_VARS))
col3.metric("Missing sau xử lý", int(df[VAR_VARS].isna().sum().sum()))

st.dataframe(df[VAR_VARS].rename(columns=VAR_LABELS_VN), use_container_width=True)

fig = make_subplots(rows=2, cols=2, subplot_titles=[VAR_LABELS_VN[col] for col in VAR_VARS])
colors = ["#003366", "#11a579", "#e45756", "#777777"]

for i, (col, color) in enumerate(zip(VAR_VARS, colors)):
    row = i // 2 + 1
    col_pos = i % 2 + 1
    fig.add_trace(
        go.Scatter(x=df.index.year, y=df[col], mode="lines+markers",
                   line=dict(color=color, width=2.5), name=VAR_LABELS_VN[col]),
        row=row,
        col=col_pos,
    )

fig.update_layout(
    height=650,
    template="plotly_white",
    title="Bốn chuỗi giữ lại: CPI, GDP, lãi suất, tỷ giá",
    showlegend=False,
)
st.plotly_chart(fig, use_container_width=True)

with st.expander("Dữ liệu thô"):
    st.dataframe(df_raw, use_container_width=True)
