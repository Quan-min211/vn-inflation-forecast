# Product Brief: Executive Summary
# Vietnam Inflation Forecast Project

## The Challenge
Inflation management is critical to macroeconomic stability. Over the past 30 years, Vietnam has faced diverse inflationary pressures. The core analytical challenge is separating internal inflation "inertia" (inflation driven by psychological expectations and structural rigidity) from external macroeconomic shocks (GDP surges, credit expansion, and exchange rate volatility).

## The Solution
This project provides a robust, Python-based analytical pipeline that leverages advanced Time Series Econometrics to dissect these drivers:
1. **ARIMA Modeling:** Extracts the inertial component of inflation.
2. **VAR Modeling:** Maps the dynamic, multi-directional relationships between the 4 pillars of the economy (Prices, Growth, Monetary, Foreign Affairs).

## Key Deliverables
- A unified Jupyter Notebook (`Project1_DAAN.ipynb`) documenting the end-to-end data processing, statistical testing (ADF, VIF), and modeling.
- Clear Python-generated visualizations including Impulse Response Functions (IRF) and ARIMA forecasts with confidence intervals.
- A final report concluding whether inertia or external factors dominate Vietnam's inflation landscape.

## Impact
This analysis equips researchers, students, and policymakers with quantitative evidence to formulate targeted interventions—whether focusing on expectation management (if inertia dominates) or monetary/fiscal tightening (if external factors dominate).