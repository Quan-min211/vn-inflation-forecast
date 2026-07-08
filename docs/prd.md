# Product Requirements Document

## Objective

Build a minimal academic pipeline that answers:

> Is Vietnam's inflation mainly caused by **inertia/expectations** or by **external macroeconomic factors**?

## Final Claim

The product must support this claim with data:

> Vietnam's inflation in the observed period is primarily **inertial** ("Bệnh tự miễn").

## Functional Requirements

1. Load and clean the Excel dataset locally with pandas.
2. Handle missing values in `domestic_credit_index` and `lending_interest_percent`.
3. Keep the VAR model focused on four variables:
   - CPI growth
   - GDP growth
   - lending interest
   - exchange rate
4. Run ADF and VIF before modeling.
5. Fit VAR(1).
6. Produce FEVD for **10 periods**.
7. Use FEVD as the central evidence in notebook, dashboard, and report.

## Out of Scope

- Broad correlation chapter as a standalone narrative.
- Large EDA dashboard.
- Cloud infrastructure.
- Extra ML models unless explicitly requested.
