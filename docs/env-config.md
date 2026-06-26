# Environment Configuration
# Vietnam Inflation Forecast Project

## 1. System Requirements
- **OS:** Windows, macOS, or Linux.
- **Python:** Python 3.9, 3.10, or 3.11.

## 2. Local Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd vn-inflation-forecast
   ```

2. **Set up a Virtual Environment (Recommended):**
   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment (Windows)
   venv\Scripts\activate

   # Activate the virtual environment (macOS/Linux)
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   Since the project relies on standard data science libraries, install them via pip:
   ```bash
   pip install pandas numpy scipy statsmodels scikit-learn matplotlib seaborn jupyter openpyxl
   ```

## 3. Running the Project

- Start the Jupyter Notebook server:
  ```bash
  jupyter notebook
  ```
- Navigate to `src/Project1_DAAN.ipynb` and run the cells sequentially.
- Ensure that the dataset is located at `data/dataset_project1.xlsx` relative to the project root, or update the file path in the notebook accordingly.