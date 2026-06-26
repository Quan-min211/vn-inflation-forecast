# Dashboard & Visualization Specification
# Vietnam Inflation Forecast Project

This document defines the visualization requirements for the project. While the previous architecture relied on Looker Studio and BigQuery, this project uses Python-based visualizations directly within the Jupyter Notebook (`matplotlib` and `seaborn`).

## 1. General Principles
- **Theme:** Clean, academic style suitable for reports.
- **Labels:** All axes must have clear labels with units (e.g., "%", "Index", "Year").
- **Titles:** Chart titles should convey the *insight*, not just describe the axes (e.g., "DỰ BÁO TỪ QUÁN TÍNH: Lạm phát kỳ vọng tiếp tục duy trì đà tăng nhẹ").

## 2. Required Visualizations

### 2.1 EDA (Exploratory Data Analysis)
- **Time Series Line Charts:** Trend of `cpi_growth_percent` overlaid with `gdp_growth_percent` over the 1996-2022 period to visualize the trade-off.
- **Correlation Heatmap:** A Seaborn heatmap showing the Pearson correlation coefficients between the 11 variables to identify initial collinearity.
- **Missing Values Matrix:** A heatmap showing the location of null values in the raw dataset.

### 2.2 Time Series Diagnostics
- **ACF & PACF Plots:** For the `cpi_growth_percent` series (both original and differenced) to justify the selection of ARIMA (p, q) parameters.
- **Residual Plots:** Histogram and Q-Q plots of model residuals to verify the assumption of normal distribution and white noise.

### 2.3 Model Results
- **ARIMA Forecast Plot:** 
  - Show historical actual values (solid line).
  - Show forecasted values (dashed red line).
  - Include a confidence interval band (e.g., 95% shaded region, colored pink/light red).
- **VAR Impulse Response Functions (IRF):**
  - A grid of plots showing how `cpi_growth_percent` responds to a 1-standard-deviation shock in other variables (e.g., exchange rate, credit index) over a 10-year horizon.
- **VAR Variance Decomposition:** Stacked bar chart showing the percentage of inflation variance explained by itself vs. external factors over time.
