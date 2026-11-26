# Week 1 - Day 5: Employee Salary Visualisations & Report

## One-Page Summary of Findings

- **Problem:** Examine how employee salaries (`INR`) are distributed across team members, compare individual pay against the team average (`68,800 INR`), and check whether compensation follows employee ID order.
- **Data:** `data/employees.csv` containing 5 employee records (`id`, `name`, `city`, `salary`), with city labels normalised during analysis and visualised across five `matplotlib` chart types (`bar`, `histogram`, `scatter`, `sorted line`, and `box plot`).
- **3 Key Insights:**
  1. **Pay spread around the mean:** Salaries vary noticeably around the `68,800 INR` average, separating higher-earning records above the mean line from lower-earning records below it.
  2. **No strict ID-to-salary sequence:** Higher employee IDs do not consistently correspond to higher salaries, indicating pay is not strictly ordered by ID.
  3. **Tight central distribution:** The histogram and box plot show values clustered within a relatively narrow central range with no extreme outliers in this sample.
- **2 Recommendations:**
  1. **Define clear compensation bands by role/level:** Base pay structure and reviews on explicit role/level bands rather than sequential IDs.
  2. **Collect richer attributes and more records:** Expand the dataset and include role, experience/tenure, and department fields for deeper compensation analysis.
- **Limitations:** The dataset has only **5 rows** and lacks context such as job title, seniority, tenure, or performance ratings, limiting statistical generalisability.

## Project Structure

- `data/employees.csv` — Input employee dataset
- `notebooks/visualisations.ipynb` — Analysis notebook with 5 visualisations and insights
- `reports/figures/` — Saved PNG visualisations (`01` through `05`)
- `reports/visualisations.html` — Exported HTML report generated via `nbconvert`
- `app.py` — Streamlit bonus app displaying two charts
- `requirements.txt` — Python packages required to run the project

## How to Run

1. Open PowerShell and navigate to the Day 5 project directory:
   ```powershell
   Set-Location "C:\Users\ricky\Documents\ai-training-week1\Week 1- Day 5\task1_visualisations"