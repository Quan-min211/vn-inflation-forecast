# Master Plan & Team Structure
# Vietnam Inflation Forecast Project

## 1. Team Organization (Group 02)

| Name | Student ID | Role / Primary Responsibility |
|------|------------|-------------------------------|
| Đỗ Kiến Hưng | 23133030 | Data Cleaning, Preprocessing, EDA |
| Trần Minh Khánh | 23133035 | Statistical Testing (ADF, VIF), Stationarity |
| Nguyễn Đặng Quốc Anh | 23133004 | ARIMA Modeling & Univariate Forecasting |
| Phạm Minh Quân | 23133060 | VAR Modeling, IRF Analysis, Final Reporting |

*Note: Roles are fluid and team members collaborate on the final Jupyter Notebook.*

## 2. Execution Phases

### Phase 1: Data Cleaning & Preprocessing
- **Goal:** Import Excel data, clean missing values, and structure the time series index.
- **Deliverables:** Cleaned DataFrame, missing value heatmaps, correlation matrix.

### Phase 2: Exploratory Data Analysis & Statistical Testing
- **Goal:** Understand the relationships between the 4 macroeconomic pillars.
- **Deliverables:** Line charts of trends, ADF test results, VIF scores, differenced datasets (if required).

### Phase 3: Model 1 - ARIMA (Inertia Analysis)
- **Goal:** Model the `cpi_growth_percent` using its own history to test the "auto-immune" inflation hypothesis.
- **Deliverables:** ACF/PACF plots, selected (p,d,q) model, forecast plots with confidence intervals.

### Phase 4: Model 2 - VAR (Multivariate Analysis)
- **Goal:** Model the interactions between CPI and external factors (Exchange Rate, GDP, Credit).
- **Deliverables:** Optimal lag selection, Granger Causality results, Impulse Response Function (IRF) graphs.

### Phase 5: Synthesis & Conclusion
- **Goal:** Answer the ultimate question based on evidence from Phase 3 and Phase 4.
- **Deliverables:** Final Jupyter Notebook (`Project1_DAAN.ipynb`), presentation slides, and actionable macroeconomic policy recommendations.