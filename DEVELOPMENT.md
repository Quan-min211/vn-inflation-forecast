# Development Workflow & Standards

## 1. Local Environment Setup

Since this project primarily utilizes Python for data processing, statistical analysis, and machine learning, you will need to set up a standard Python data science environment.

1. **Clone the repository**
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   Ensure you have the required libraries installed:
   ```bash
   pip install pandas numpy scipy statsmodels scikit-learn matplotlib seaborn jupyter openpyxl
   ```

## 2. Directory Structure Conventions

- `data/`: Contains raw datasets (`dataset_project1.xlsx`) and processed outputs. **Do not commit large data files or credentials to Git.**
- `src/`: Contains all analysis code. For this project, the core logic is in Jupyter Notebooks (e.g., `Project1_DAAN.ipynb`) or Python scripts.
- `docs/`: Contains all project specifications, data dictionaries, and architectural plans.

## 3. Data Processing Guidelines

- **Missing Values:** Ensure missing values in `domestic_credit_index` and `lending_interest_percent` are appropriately imputed or handled before modeling.
- **Data Types:** Verify that percentage and index columns are cast to `float64` and years to `int64`.

## 4. Modeling Guidelines

- Ensure statistical rigor: Always run ADF tests for stationarity before building ARIMA or VAR models.
- Handle non-stationarity explicitly using differencing techniques.
- For multivariate analysis (VAR), check for multicollinearity using VIF scores and interpret the Granger Causality tests correctly.

## 5. Git Workflow

- **Branching Strategy:** Use feature branches (e.g., `feature/eda`, `feature/arima-model`) and merge via Pull Requests.
- **Commit Messages:** Write clear, descriptive commit messages summarizing the analytical step or code fix performed.
