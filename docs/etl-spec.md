# ETL Specification
# Vietnam Inflation Forecast Project

This document defines the Extract, Transform, and Load (ETL) pipeline rules for the macroeconomic dataset. 
Since this project uses a local pipeline (Excel to Pandas), the "Load" step is simply the preparation of the final DataFrame for the ML models.

## 1. Extract
- **Source:** Local Excel file `data/dataset_project1.xlsx`.
- **Method:** `pandas.read_excel()`

## 2. Transform

The following transformation steps must be applied sequentially:

### 2.1 Indexing
- Set the `years` column as the DataFrame index.
- Convert the index to a proper Pandas `DateTimeIndex` or integer index suitable for time series analysis (e.g., `pd.to_datetime(df['years'], format='%Y')`).

### 2.2 Missing Value Imputation
- The dataset is known to have missing values in `domestic_credit_index` and `lending_interest_percent`.
- **Rule:** Use linear interpolation (`interpolate()`) or forward fill (`ffill()`) to handle the gaps, as macroeconomic data often exhibits trends that shouldn't be zero-filled or mean-filled.

### 2.3 Data Type Casting
Ensure all measurement columns are standard 64-bit floats.
```python
float_cols = ['cpi_growth_percent', 'cpi_index', 'gdp_deflator_percent',
              'gdp_growth_percent', 'unemployment_rate', 'domestic_credit_index',
              'lending_interest_percent', 'officical_exchange_rate_percent',
              'import_index', 'export_index']

df[float_cols] = df[float_cols].astype('float64')
```

### 2.4 Duplicate Column Handling
- Check for duplicate columns (e.g., `gdp_delflator_percent` and `gdp_deflator_percent`).
- **Rule:** Drop redundant or misspelled columns to maintain a clean schema. Keep the correctly spelled version.

## 3. Load (To Model Memory)
- The cleaned DataFrame is then passed directly to the `statsmodels` pipeline.
- Create a transformed copy of the DataFrame (`df_stationary`) where differencing or log-transformations are applied based on the ADF test results (see `ml-spec.md`). Do NOT overwrite the raw values in the main analytical DataFrame.
