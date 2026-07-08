import sys
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils import (
    VAR_LABELS_VN,
    fit_var_model,
    get_cpi_fevd,
    run_granger_tests,
    setup_page,
)

setup_page("VAR Model", "📊")

st.title("VAR(1) và FEVD 10 kỳ")

result, selected_lag, lag_selection, df_var = fit_var_model()
fevd = get_cpi_fevd(result, periods=10)
cpi_col = "Quán tính tự thân (CPI)"
fevd["Tác nhân bên ngoài"] = 100 - fevd[cpi_col]

col1, col2, col3 = st.columns(3)
col1.metric("Mô hình", f"VAR({selected_lag})")
col2.metric("Số quan sát", len(df_var))
col3.metric("FEVD horizon", "10 kỳ")

st.markdown("## Dự báo ngắn hạn theo tinh thần bản v1")
forecast = result.forecast(y=df_var.values, steps=3)
forecast_index = pd.date_range(
    start=df_var.index[-1] + pd.DateOffset(years=1),
    periods=3,
    freq="YS",
)
forecast_df = pd.DataFrame(forecast, index=forecast_index.year, columns=df_var.columns)
st.dataframe(forecast_df.rename(columns=VAR_LABELS_VN).round(3), use_container_width=True)

st.markdown("## FEVD 10 kỳ: bằng chứng chính")
plot_df = fevd.drop(columns=["Tác nhân bên ngoài"])

fig = go.Figure()
colors = ["#003366", "#11a579", "#e45756", "#777777"]
for label, color in zip(plot_df.columns, colors):
    fig.add_trace(go.Bar(x=plot_df.index, y=plot_df[label], name=label, marker_color=color))

for period in fevd.index:
    fig.add_annotation(
        x=period,
        y=105,
        text=f"ngoài: {fevd.loc[period, 'Tác nhân bên ngoài']:.1f}%",
        showarrow=False,
        font=dict(size=10, color="#111111"),
    )

fig.add_hline(y=80, line_dash="dash", line_color="#e45756")
fig.update_layout(
    barmode="stack",
    title="CPI tự giải thích phần lớn sai số dự báo lạm phát",
    xaxis_title="Kỳ dự báo",
    yaxis_title="Tỷ trọng (%)",
    yaxis=dict(range=[0, 112]),
    template="plotly_white",
    height=560,
    legend=dict(orientation="h", y=-0.25),
)
st.plotly_chart(fig, use_container_width=True)

st.dataframe(fevd.round(2), use_container_width=True)

inertia_avg = fevd.loc["Kỳ 2":"Kỳ 10", cpi_col].mean()
external_avg = fevd.loc["Kỳ 2":"Kỳ 10", "Tác nhân bên ngoài"].mean()
st.error(
    f"Phán quyết FEVD: quán tính CPI trung bình kỳ 2-10 = {inertia_avg:.1f}%, "
    f"tác nhân bên ngoài = {external_avg:.1f}%."
)

st.markdown("## Kiểm tra phụ: Granger")
granger = run_granger_tests(df_var.values, list(df_var.columns))
st.dataframe(granger, use_container_width=True, hide_index=True)

with st.expander("Lag selection tham khảo"):
    st.text(lag_selection.summary().as_text())
