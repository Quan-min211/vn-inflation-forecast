# Product Requirements Document (PRD)
# Vietnam Inflation Forecast Project

## 1. Project Objective
Build an analytical pipeline and time series forecasting model to determine the core drivers of inflation in Vietnam (1996-2022) and project the CPI growth trend for the near future (up to 2024-2025).

## 2. Problem Statement
**"Trong 3 thập kỷ qua, Lạm phát tại Việt Nam chủ yếu là do 'Bệnh tự miễn' (Quán tính tự sinh ra do tâm lý kỳ vọng) hay do 'Tác nhân bên ngoài' (Tỷ giá, Tín dụng, Tăng trưởng GDP)? Cần can thiệp vào đâu để kiểm soát nó?"**

## 3. Target Audience
- Academic instructors and review boards (HCMUTE DAAN course).
- Economists and financial analysts studying the Vietnamese market.

## 4. Functional Requirements

### 4.1 Data Processing
- Load data from the provided Excel file.
- Perform necessary imputation for missing macroeconomic data.
- Output clean, indexed time series DataFrames.

### 4.2 Statistical Analysis
- The system must verify the stationarity of all time series using the ADF test.
- The system must evaluate multicollinearity using VIF.

### 4.3 Modeling
- **Univariate Forecasting:** Implement ARIMA to isolate the inertial component of inflation.
- **Multivariate Forecasting:** Implement VAR to measure the impact of external pillars (Growth, Monetary, Foreign Affairs).
- The system must output standard evaluation metrics (RMSE, MAPE) for comparison.

### 4.4 Visualization
- Generate Python-based plots (matplotlib/seaborn) to display the historical trends, ACF/PACF diagnostics, IRF, and forecast trajectories with confidence intervals.

## 5. Success Criteria
- The models must successfully run and converge on the provided dataset.
- The ARIMA model should provide a mathematically sound baseline forecast.
- The VAR model must clearly demonstrate whether external factors significantly Grager-cause inflation compared to internal inertia.
- The analysis must yield a conclusive answer to the "Ultimate Question".