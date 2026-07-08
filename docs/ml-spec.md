# Machine Learning & Time Series Specification

## Research Focus

The project is now intentionally minimal and centered on one question:

> Is inflation in Vietnam mainly driven by **inertia/expectations** ("Bệnh tự miễn") or by **external macroeconomic factors**?

The expected data-driven conclusion is:

> Vietnam's inflation over the observed period is primarily **inertial**.

## Required Pipeline

1. Load and clean `data/dataset_project1.xlsx`.
2. Keep only the variables needed for the central question:
   - `cpi_growth_percent`
   - `gdp_growth_percent`
   - `lending_interest_percent`
   - `officical_exchange_rate_percent`
3. Run ADF tests and difference non-stationary series.
4. Run VIF on the final VAR dataset as a minimal multicollinearity check.
5. Fit a compact VAR model using **VAR(1)**, following the simpler modeling idea from the original notebook.
6. Compute **FEVD for 10 periods**.
7. Use FEVD as the main evidence:
   - CPI self-explains most forecast error variance -> inertia dominates.
   - External variables explain the remaining share -> external factors are secondary.

## Secondary Checks

Granger causality and IRF are supporting checks only. They must not distract from the FEVD-based answer.
