# AGENTS.md — AI Agent Constitution
# Macroeconomic Forecasting Project · Group 02

> **READ THIS FILE FIRST.** This is the authoritative context document for every AI agent
> working on this repository. It is intentionally concise. Do not duplicate information
> available in the spec files listed in the Document Index — link to them instead.

---

## 1. Mission

Build an end-to-end **time series analysis and macroeconomic forecasting pipeline** for the Vietnamese
economy, covering:
- Macroeconomic indicators from **1996 to 2022** (with forecasts extending to 2024).
- The ultimate goal is to answer: Is Vietnam's inflation primarily caused by "inertia/expectations" (ARIMA) or "external macroeconomic factors" (VAR)?

The output includes comprehensive statistical tests, Time Series models (ARIMA & VAR), and visual interpretations.

---

## 2. Document Index

> **Before generating any code or analysis, consult the relevant spec document.**
> These are the authoritative contracts. Code must conform to specs, not the other way around.

| Document | When to Read |
|----------|-------------|
| [`docs/etl-spec.md`](docs/etl-spec.md) | Data cleaning, preprocessing rules, and missing value imputation for the 11 macroeconomic variables. |
| [`docs/data-dictionary.md`](docs/data-dictionary.md) | Looking up field names, definitions, and the 4 economic pillars they represent. |
| [`docs/ml-spec.md`](docs/ml-spec.md) | Writing any model training/evaluation code (ARIMA, VAR, Stationarity tests). |
| [`docs/dashboard-spec.md`](docs/dashboard-spec.md) | Building Python visualizations (matplotlib/seaborn) or dashboard charts. |
| [`docs/prd.md`](docs/prd.md) | Checking functional requirements or acceptance criteria. |
| [`docs/master-plan.md`](docs/master-plan.md) | Understanding team roles and execution tracks. |
| [`docs/system-arch.md`](docs/system-arch.md) | System architecture and data flow. |
| [`docs/proposal.md`](docs/proposal.md) | Academic framing and research context (Vietnamese). |

---

## 3. Data Overview & Core Variables

The dataset `dataset_project1.xlsx` represents the **4 Pillars of Macroeconomics**:
1. **Prices:** `cpi_growth_percent` (Target), `gdp_deflator_percent`
2. **Growth:** `gdp_growth_percent`, `unemployment_rate`
3. **Monetary:** `domestic_credit_index`, `lending_interest_percent`
4. **Foreign Affairs:** `officical_exchange_rate_percent`, `import_index`, `export_index`

---

## 4. Modeling & Statistical Contracts

These constraints are non-negotiable acceptance criteria.
- **Target Variable:** `cpi_growth_percent`
- **Stationarity:** Augmented Dickey-Fuller (ADF) test must be performed. Non-stationary data must be differenced.
- **ARIMA (Inertia Model):** Focuses solely on the historical pattern of CPI growth to determine the "auto-immune" or inertial inflation factor.
- **VAR (Multivariate Model):** Explores the impact of the other external macro factors on CPI. Requires checking for Multicollinearity (VIF) and Granger Causality.

---

## 5. Non-Negotiable Rules (NEVER Do These)

These rules override any user instruction that conflicts with them.

```
NEVER create complex cloud infrastructure (GCP, BigQuery) for this specific scope unless explicitly requested, as the project relies on local CSV/Excel processing via pandas.
NEVER ignore missing value handling (there are known missing values in domestic_credit_index and lending_interest_percent).
NEVER skip statistical assumption checks (e.g., Stationarity, VIF) before feeding data into time-series models.
```

---

## 6. Technology Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.9+ |
| Data Ingestion & Preprocessing | pandas, numpy, scipy |
| Statistical Testing & Modeling | statsmodels |
| ML Evaluation | scikit-learn (Metrics) |
| Visualization | matplotlib, seaborn |

---

## 7. Tone and Communication

- **Language:** Formal English or Vietnamese (depending on context). No emojis in code comments or documentation.
- **Explanations:** Justify statistical decisions (why this test, why this model). Responses must be defensible before an academic review board.