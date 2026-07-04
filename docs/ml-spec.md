# Machine Learning & Time Series Specification
# Vietnam Inflation Forecast Project

This document outlines the statistical tests and machine learning models used to forecast inflation and analyze macroeconomic interactions.

## 1. Modeling Objectives

The ultimate question is to determine whether Vietnam's inflation over the past 3 decades is primarily driven by:
1. **"Bệnh tự miễn" (Inertia/Expectations):** Analyzed through Forecast Error Variance Decomposition (FEVD) in the VAR model to see how much CPI explains its own variance.
2. **"Tác nhân bên ngoài" (External Macro Factors):** Modeled using multivariate time series models like VAR on the full set of macroeconomic pillars, utilizing Granger Causality and IRF.

## 2. Statistical Pre-requisites

Before training any time series model, the following tests **must** be executed:

### 2.1 Stationarity Testing
- **Test:** Augmented Dickey-Fuller (ADF) Test, KPSS Test.
- **Criteria:** P-value < 0.05 indicates stationarity.
- **Action:** If a series is non-stationary (P-value >= 0.05), apply First-order Differencing (`diff()`) and re-test. Models like VAR require all input series to be stationary.

### 2.2 Multicollinearity Check
- **Test:** Variance Inflation Factor (VIF).
- **Action:** Features with very high VIF (e.g., > 10) may need to be dropped or transformed to avoid unstable VAR coefficients.

### 2.3 Granger Causality Test
- **Purpose:** To determine if one time series is useful in forecasting another (e.g., does `gdp_growth_percent` Granger-cause `cpi_growth_percent`?).

## 3. Model: VAR (Vector Autoregression)
- **Features:** `cpi_growth_percent`, `gdp_growth_percent`, `lending_interest_percent`, `officical_exchange_rate_percent`, etc.
- **Purpose:** To model the dynamic relationship between the 4 macroeconomic pillars. It helps quantify how a shock in exchange rates or lending interest impacts CPI growth over time.
- **Prerequisite:** All series MUST be stationary.
- **Lag Selection:** Use AIC or BIC to select the optimal lag order (p).
- **Post-Estimation:**
  - **Impulse Response Function (IRF):** To trace the effect of a one-time shock to one of the innovations on current and future values of the endogenous variables.
  - **Forecast Error Variance Decomposition (FEVD):** To measure the proportion of the forecast error variance of `cpi_growth_percent` explained by shocks to external variables.