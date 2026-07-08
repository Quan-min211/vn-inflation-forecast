"""Shared data and VAR helpers for the Streamlit dashboard."""
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
import statsmodels.api as sm
import streamlit as st
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tsa.stattools import adfuller, grangercausalitytests
from statsmodels.tsa.vector_ar.var_model import VAR

warnings.filterwarnings("ignore")

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "dataset_project1.xlsx"

VAR_VARS = [
    "cpi_growth_percent",
    "gdp_growth_percent",
    "lending_interest_percent",
    "officical_exchange_rate_percent",
]

VAR_LABELS_VN = {
    "cpi_growth_percent": "Quán tính tự thân (CPI)",
    "gdp_growth_percent": "Tăng trưởng GDP",
    "lending_interest_percent": "Lãi suất cho vay",
    "officical_exchange_rate_percent": "Tỷ giá hối đoái",
}


def setup_page(title: str, icon: str = "📊"):
    st.set_page_config(
        page_title=f"{title} - Lạm phát Việt Nam",
        page_icon=icon,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.sidebar.markdown("### Lạm phát Việt Nam")
    st.sidebar.markdown("**Câu hỏi:** Quán tính hay tác nhân bên ngoài?")
    st.sidebar.divider()


@st.cache_data
def load_raw_data() -> pd.DataFrame:
    return pd.read_excel(DATA_PATH)


@st.cache_data
def clean_data() -> pd.DataFrame:
    df = load_raw_data().copy()
    if "gdp_delflator_percent" in df.columns:
        df = df.rename(columns={"gdp_delflator_percent": "gdp_deflator_index"})
    df["years"] = pd.to_datetime(df["years"], format="%Y")
    df = df.set_index("years").sort_index()
    return df.interpolate(method="linear")


def _adf_row(series: pd.Series, name: str) -> dict:
    result = adfuller(series.dropna(), autolag="AIC")
    return {
        "Biến": name,
        "ADF Statistic": round(result[0], 4),
        "P-value": round(result[1], 4),
        "Dừng": result[1] < 0.05,
    }


@st.cache_data
def prepare_var_data():
    df = clean_data()
    adf_before = pd.DataFrame([_adf_row(df[col], col) for col in VAR_VARS])
    non_stationary = adf_before.loc[~adf_before["Dừng"], "Biến"].tolist()

    df_var = df[VAR_VARS].copy()
    for col in non_stationary:
        df_var[col] = df_var[col].diff()
    df_var = df_var.dropna()

    adf_after = pd.DataFrame([_adf_row(df_var[col], col) for col in VAR_VARS])
    X = sm.add_constant(df_var)
    vif = pd.DataFrame({
        "Biến": VAR_VARS,
        "VIF": [variance_inflation_factor(X.values, i + 1) for i in range(len(VAR_VARS))],
    }).round(2)

    return df_var, adf_before, adf_after, vif, non_stationary


@st.cache_resource
def fit_var_model():
    df_var, *_ = prepare_var_data()
    model = VAR(df_var)
    lag_selection = model.select_order(maxlags=2)
    selected_lag = 1
    result = model.fit(selected_lag)
    return result, selected_lag, lag_selection, df_var


def get_cpi_fevd(result, periods: int = 10) -> pd.DataFrame:
    names = list(result.names)
    cpi_idx = names.index("cpi_growth_percent")
    decomp = result.fevd(periods).decomp

    if decomp.shape[0] == len(names):
        matrix = decomp[cpi_idx, :, :]
    else:
        matrix = decomp[:, cpi_idx, :]

    return pd.DataFrame(
        matrix * 100,
        index=[f"Kỳ {i}" for i in range(1, periods + 1)],
        columns=[VAR_LABELS_VN.get(col, col) for col in names],
    )


@st.cache_data
def run_granger_tests(_values, _columns):
    df_var = pd.DataFrame(_values, columns=_columns)
    target = "cpi_growth_percent"
    rows = []
    for cause in [col for col in df_var.columns if col != target]:
        try:
            test_data = df_var[[target, cause]].dropna()
            result = grangercausalitytests(test_data, maxlag=1, verbose=False)
            p_value = result[1][0]["ssr_ftest"][1]
            rows.append({
                "Tác nhân bên ngoài": VAR_LABELS_VN.get(cause, cause),
                "P-value": round(p_value, 4),
                "Có tín hiệu dự báo CPI": p_value < 0.05,
            })
        except Exception:
            rows.append({
                "Tác nhân bên ngoài": VAR_LABELS_VN.get(cause, cause),
                "P-value": np.nan,
                "Có tín hiệu dự báo CPI": False,
            })
    return pd.DataFrame(rows)
