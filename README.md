# Employee Workforce Segmentation

Clustering (K-Means, Hierarchical/Ward) + PCA to segment employees, find high-risk groups and support retention decisions.

## Deliverables
| Deliverable | File |
|---|---|
| Employee Segmentation Report (includes PCA Summary) | `report/Employee_Segmentation_Report.docx` |
| Analysis notebook (all code + outputs) | `Employee_Workforce_Segmentation.ipynb` |
| PCA Summary tables | `outputs/pca_summary.csv`, `outputs/pca_loadings_top4.csv` |
| Workforce Analytics Dashboard | `dashboard/workforce_dashboard.html` (open in a browser; needs internet for Chart.js) |
| Segment results | `outputs/employee_segments.csv`, `outputs/segment_profile.csv` |

## Run
```bash
pip install -r requirements.txt
python data/generate_employee_data.py      # (re)creates data/employee_data.csv
jupyter notebook Employee_Workforce_Segmentation.ipynb
```
Using a real dataset (e.g. the IBM HR Analytics CSV): put it at `data/employee_data.csv` with the same column names used in the `FEATURES` list, then re-run the notebook.

## Note
`data/employee_data.csv` is **synthetic** (IBM HR-style schema, seed 42) because no dataset file was supplied with the task.
