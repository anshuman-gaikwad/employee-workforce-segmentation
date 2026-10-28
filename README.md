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
