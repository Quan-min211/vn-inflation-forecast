# System Architecture

## Minimal Local Pipeline

```mermaid
graph TD
    A["dataset_project1.xlsx"] --> B["pandas clean + interpolate"]
    B --> C["ADF + differencing"]
    C --> D["VIF check"]
    D --> E["VAR(1)"]
    E --> F["FEVD 10 periods"]
    F --> G["Verdict: inflation is mainly inertial"]
```

## Implementation

- Notebook source: `src/generate_notebook.py`
- Generated notebook: `src/Project1_DAAN_v2.ipynb`
- Dashboard: `src/dashboard`
- Data: `data/dataset_project1.xlsx`

The dashboard and report must follow the same flow as the notebook and avoid unrelated analysis sections.
