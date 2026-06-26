# Project Overview
# Vietnam Inflation Forecast Project

## 1. Context and Rationale
Vietnam's economy has experienced significant transformations over the past three decades (1996-2022). Throughout this period, controlling inflation (measured by CPI growth) has remained a central mandate for the State Bank of Vietnam and policymakers. However, inflation is a complex phenomenon driven by multiple interacting forces. 

This project aims to dissect the core drivers of inflation by analyzing 11 key macroeconomic variables spanning 1996 to 2022. By employing advanced time series modeling techniques, the project seeks to determine whether inflation is a self-fulfilling prophecy ("Bệnh tự miễn") driven by historical inertia, or a reaction to external macroeconomic shocks ("Tác nhân bên ngoài").

## 2. Core Methodology
The project shifts away from simple cross-sectional regression and adopts **Time Series Analysis** to capture the temporal dynamics of economic data.
- **Data:** Annual data from reliable macroeconomic sources (World Bank, SBV, GSO) stored in an Excel dataset.
- **Univariate Analysis (ARIMA):** Models the CPI growth rate purely based on its own past values and past forecast errors. A highly accurate ARIMA model suggests strong inertial inflation.
- **Multivariate Analysis (VAR):** Models the interconnectedness of 4 macroeconomic pillars (Prices, Growth, Monetary, Foreign Affairs). It analyzes how a shock in one variable (e.g., Exchange Rate) ripples through the economy to affect CPI over time.

## 3. Expected Outcomes
- A rigorous, statistically sound analysis of Vietnam's inflation drivers.
- Short-term forecasts (3-year horizon) of CPI growth.
- Clear visualizations illustrating the economic relationships and model predictions.
- Data-driven policy recommendations for inflation control.