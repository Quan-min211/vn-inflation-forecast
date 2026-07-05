"""
utils.py — Module xử lý dữ liệu dùng chung cho Streamlit Dashboard.
Tất cả các hàm đều sử dụng Streamlit cache để tránh recompute khi chuyển trang.
"""
import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

from statsmodels.tsa.stattools import adfuller, grangercausalitytests
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tsa.vector_ar.var_model import VAR

import warnings
warnings.filterwarnings('ignore')

# ---------------------------------------------------------------------------
# Path resolution
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # src/dashboard -> src -> project root
DATA_PATH = PROJECT_ROOT / "data" / "dataset_project1.xlsx"

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
ANALYSIS_VARS = [
    'cpi_growth_percent', 'gdp_deflator_percent',
    'gdp_growth_percent', 'unemployment_rate',
    'domestic_credit_index', 'lending_interest_percent',
    'officical_exchange_rate_percent', 'import_index', 'export_index'
]

VAR_VARS = [
    'cpi_growth_percent', 'gdp_growth_percent',
    'lending_interest_percent', 'officical_exchange_rate_percent'
]

VAR_LABELS_VN = {
    'cpi_growth_percent': 'Quán tính tự thân (CPI)',
    'gdp_growth_percent': 'Tăng trưởng kinh tế (GDP)',
    'lending_interest_percent': 'Lãi suất cho vay (IR)',
    'officical_exchange_rate_percent': 'Tỷ giá hối đoái (EX)'
}

PILLAR_COLORS = {
    'prices': '#E24A33',
    'monetary': '#348ABD',
    'foreign': '#FBC15E',
    'growth': '#4682B4',
}

# ---------------------------------------------------------------------------
# Data loading & cleaning
# ---------------------------------------------------------------------------
@st.cache_data
def load_raw_data() -> pd.DataFrame:
    """Load the raw Excel dataset without any transformations."""
    df = pd.read_excel(DATA_PATH)
    return df


@st.cache_data
def clean_data() -> pd.DataFrame:
    """
    Full cleaning pipeline:
    1. Rename typo column gdp_delflator_percent -> gdp_deflator_index
    2. Set datetime index
    3. Linear interpolation for missing values
    """
    df = load_raw_data().copy()

    # Rename typo column
    if 'gdp_delflator_percent' in df.columns:
        df.rename(columns={'gdp_delflator_percent': 'gdp_deflator_index'}, inplace=True)

    # Set datetime index
    df['years'] = pd.to_datetime(df['years'], format='%Y')
    df.set_index('years', inplace=True)

    # Interpolate missing values
    df.interpolate(method='linear', inplace=True)

    return df


# ---------------------------------------------------------------------------
# Statistical tests
# ---------------------------------------------------------------------------
@st.cache_data
def run_adf_tests(data: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Run ADF test on each column; return a DataFrame of results."""
    rows = []
    for col in columns:
        series = data[col].dropna()
        result = adfuller(series, autolag='AIC')
        rows.append({
            'Biến': col,
            'ADF Statistic': round(result[0], 4),
            'P-value': round(result[1], 4),
            'Lags Used': result[2],
            'Observations': result[3],
            'Dừng': result[1] < 0.05
        })
    return pd.DataFrame(rows)


@st.cache_data
def compute_vif(data: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Compute Variance Inflation Factor for each column."""
    vif_data = data[columns].dropna()
    X = sm.add_constant(vif_data)
    rows = []
    for i, col in enumerate(columns):
        vif_val = variance_inflation_factor(X.values, i + 1)
        rows.append({'Variable': col, 'VIF': round(vif_val, 2)})
    df_vif = pd.DataFrame(rows).sort_values('VIF', ascending=False)
    return df_vif


@st.cache_data
def prepare_var_data() -> pd.DataFrame:
    """
    Prepare stationary data for VAR:
    1. Run ADF on analysis vars
    2. Difference non-stationary series
    3. Return subset of VAR_VARS
    """
    df = clean_data()
    adf = run_adf_tests(df, ANALYSIS_VARS)
    non_stationary = adf.loc[~adf['Dừng'], 'Biến'].tolist()

    df_diff = df[ANALYSIS_VARS].copy()
    for col in non_stationary:
        df_diff[col] = df_diff[col].diff()
    df_diff = df_diff.dropna()

    return df_diff[VAR_VARS]


# ---------------------------------------------------------------------------
# VAR model — use cache_resource because the fitted model is not serializable
# ---------------------------------------------------------------------------
@st.cache_resource
def fit_var_model():
    """
    Fit a VAR model and return (var_result, optimal_lag, var_data).
    Uses cache_resource to avoid re-fitting on every page load.
    """
    var_data = prepare_var_data()
    model_temp = VAR(var_data)
    lag_results = model_temp.select_order(maxlags=2)
    optimal_lag = lag_results.aic

    model = VAR(var_data)
    var_result = model.fit(maxlags=optimal_lag)

    return var_result, optimal_lag, var_data


@st.cache_data
def run_granger_tests(_var_data_values, _var_data_columns, optimal_lag):
    """
    Run Granger Causality tests for each variable against CPI.
    Returns a list of dicts with results.
    """
    var_data = pd.DataFrame(_var_data_values, columns=_var_data_columns)
    target = 'cpi_growth_percent'
    maxlag = min(optimal_lag + 1, 3)
    results = []
    for cause_var in VAR_VARS:
        if cause_var == target:
            continue
        try:
            test_data = var_data[[target, cause_var]].dropna()
            gc = grangercausalitytests(test_data, maxlag=maxlag, verbose=False)
            # Extract min p-value across all lags
            min_p = min(gc[lag][0]['ssr_ftest'][1] for lag in gc)
            best_lag = min(gc, key=lambda lag: gc[lag][0]['ssr_ftest'][1])
            f_stat = gc[best_lag][0]['ssr_ftest'][0]
            results.append({
                'Biến': cause_var,
                'Nhãn': VAR_LABELS_VN.get(cause_var, cause_var),
                'F-statistic': round(f_stat, 4),
                'P-value': round(min_p, 4),
                'Best Lag': best_lag,
                'Granger-cause CPI': min_p < 0.05
            })
        except Exception:
            results.append({
                'Biến': cause_var,
                'Nhãn': VAR_LABELS_VN.get(cause_var, cause_var),
                'F-statistic': None,
                'P-value': None,
                'Best Lag': None,
                'Granger-cause CPI': False
            })
    return results


# ---------------------------------------------------------------------------
# Page config helper
# ---------------------------------------------------------------------------
def setup_page(title: str, icon: str = "📊"):
    """Common page configuration."""
    st.set_page_config(
        page_title=f"{title} — Lạm phát VN",
        page_icon=icon,
        layout="wide",
        initial_sidebar_state="expanded"
    )
    # Sidebar branding
    st.sidebar.markdown("### 🇻🇳 Phân tích Lạm phát VN")
    st.sidebar.markdown("**Nhóm 02** — DAAN436277_02")
    st.sidebar.divider()
