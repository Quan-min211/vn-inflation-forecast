# Master Plan & Team Structure
# Vietnam Inflation Forecast Project

## 1. Team Organization (Group 02)

| Name | Student ID | Role / Primary Responsibility |
|------|------------|-------------------------------|
| Đỗ Kiến Hưng | 23133030 | Data Cleaning, Preprocessing, EDA |
| Trần Minh Khánh | 23133035 | Statistical Testing (ADF, VIF), Stationarity |
| Nguyễn Đặng Quốc Anh | 23133004 | Data Transformation, Stationarity & Differencing |
| Phạm Minh Quân | 23133060 | VAR Modeling, IRF Analysis, Final Reporting |

*Note: Roles are fluid and team members collaborate on the final Jupyter Notebook.*

## 2. Execution Phases

### Phase 1: Data Cleaning & Preprocessing
- **Goal:** Import Excel data, clean missing values, and structure the time series index.
- **Deliverables:** Cleaned DataFrame, missing value heatmaps, correlation matrix.

### Phase 2: Exploratory Data Analysis & Statistical Testing
- **Goal:** Understand the relationships between the 4 macroeconomic pillars.
- **Deliverables:** Line charts of trends, ADF test results, VIF scores, differenced datasets (if required).

### Phase 3: Model - VAR (Multivariate Analysis)
- **Goal:** Model the interactions between CPI and external factors (Exchange Rate, GDP, Credit) and quantify inertia.
- **Deliverables:** Optimal lag selection, Granger Causality results, Impulse Response Function (IRF) graphs, and FEVD charts.

### Phase 4: Synthesis & Conclusion
- **Goal:** Answer the ultimate question based on evidence from Phase 3.
- **Deliverables:** Final Jupyter Notebook (`Project1_DAAN.ipynb`), presentation slides, and actionable macroeconomic policy recommendations.