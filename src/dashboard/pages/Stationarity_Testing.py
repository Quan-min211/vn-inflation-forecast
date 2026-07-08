import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils import VAR_LABELS_VN, prepare_var_data, setup_page

setup_page("Stationarity Testing", "🧪")

st.title("Kiểm định tối thiểu trước VAR")

df_var, adf_before, adf_after, vif, non_stationary = prepare_var_data()

st.markdown("## ADF trước xử lý")
st.dataframe(adf_before.replace({"Biến": VAR_LABELS_VN}), use_container_width=True, hide_index=True)

st.markdown("## Biến đã sai phân")
st.write([VAR_LABELS_VN.get(col, col) for col in non_stationary] or "Không có")

st.markdown("## ADF sau xử lý")
st.dataframe(adf_after.replace({"Biến": VAR_LABELS_VN}), use_container_width=True, hide_index=True)

st.markdown("## VIF trên bộ biến VAR cuối cùng")
st.dataframe(vif.replace({"Biến": VAR_LABELS_VN}), use_container_width=True, hide_index=True)

st.success(
    f"Dữ liệu VAR cuối cùng có {len(df_var)} quan sát. Các kiểm định này được giữ lại "
    "vì VAR và FEVD chỉ có ý nghĩa khi dữ liệu đầu vào đã được xử lý đúng."
)
