# Dashboard Specification

## Purpose

The Streamlit dashboard must no longer act as a broad EDA showcase. It exists to communicate one conclusion:

> Vietnam's inflation is primarily inertial ("Bệnh tự miễn"), not primarily driven by external macro shocks.

## Pages

1. **Home**
   - Shows the research question, FEVD verdict, and CPI trend.
2. **Data Exploration**
   - Shows only the four variables used in VAR.
3. **Stationarity Testing**
   - Shows ADF before/after transformation and VIF.
4. **VAR Model**
   - Shows VAR(1), short forecast, Granger support, and FEVD over **10 periods**.
5. **Conclusion**
   - Restates the verdict and policy implications.

## Required Main Chart

The main dashboard chart is the FEVD stacked bar chart over 10 periods:

- Dark blue: CPI self-impact / inertia.
- Other colors: GDP, lending interest, exchange rate.
- Each period must show external share so the viewer can immediately see that external factors are secondary.
