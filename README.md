# Vietnam Inflation Forecast

## Research Question

> Is inflation in Vietnam mainly caused by **inertia/expectations** ("Bệnh tự miễn") or by **external macroeconomic factors**?

## Data-Driven Answer

> **Vietnam's inflation over the observed period is primarily inertial.**

## Current Scope

The project has been simplified. It no longer centers on broad EDA or a standalone correlation chapter. The main pipeline is:

1. Clean the Excel dataset.
2. Keep four variables: CPI growth, GDP growth, lending interest, exchange rate.
3. Run ADF and VIF checks.
4. Fit VAR(1).
5. Compute FEVD over **10 periods**.
6. Use FEVD to compare CPI self-impact against external factors.

## Run Notebook Generator

```bash
python src/generate_notebook.py
```

## Run Dashboard

```bash
python -m streamlit run src/dashboard/Home.py
```

## Main Files

- `src/generate_notebook.py`: source for the simplified notebook.
- `src/Project1_DAAN_v2.ipynb`: generated notebook.
- `src/dashboard`: Streamlit dashboard.
- `data/dataset_project1.xlsx`: source data.
