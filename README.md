## Week 1 — Day 5: Employee Data Cleaning, Exploratory Analysis & Reporting

### Summary of Project Work Done
* **Task 1 — Data Cleaning (data_cleaning.py -> clean_data.csv):**
  * Standardized raw HR employee records (raw_data.csv) into a clean dataset of 5 valid employees across Engineering and Sales (0 missing values, 0 duplicates).
  * Trimmed whitespace, standardized text casing, converted numeric/date columns, imputed missing values using median/mode, flagged 1 invalid join date (Karthik Rao), and flagged 1 IQR salary outlier (Sanjay Verma at 250,000.00 INR).
* **Task 2 — Exploratory Data Analysis (exploratory_analysis.py & exploratory_analysis.ipynb):**
  * Computed summary statistics (mean, median, min, max, std) showing overall salary mean of 102,700.00 INR vs. median of 68,500.00 INR (skewed by the 250,000.00 INR outlier).
  * Compared departments via groupby().agg(): Engineering averages 130,166.67 INR (median 72,000.00 INR, n = 3) vs. Sales at 61,500.00 INR (median 61,500.00 INR, n = 2).
  * Computed numeric correlations (df.corr()) and merged department annual budgets (pd.merge), finding 43.39% budget utilization in Engineering (390,500 / 900,000 INR) and 30.75% in Sales (123,000 / 400,000 INR).
  * Answered 5 business questions (Q1–Q5) and wrote a one-page executive summary covering problem, data, 3 key insights, 2 recommendations, and limitations.
* **Task 2 — Reporting (exploratory_analysis.html):**
  * Exported the executed Jupyter Notebook into a standalone HTML report (exploratory_analysis.html) using nbconvert.

### Project Files (Week 1- Day 5)
* data_cleaning.py — End-to-end data cleaning pipeline script
* clean_data.csv — Cleaned and validated dataset (5 records)
* exploratory_analysis.py — Standalone EDA script
* exploratory_analysis.ipynb — Interactive notebook with EDA code, Q1–Q5 answers, and executive summary
* exploratory_analysis.html — Exported HTML report generated via nbconvert
* requirements.txt — Python dependencies for reproducing the environment

### How to Run the Project
1. Navigate to the project folder:
   cd "Week 1- Day 5"
2. Install dependencies:
   pip install -r requirements.txt
3. Run the data cleaning pipeline:
   python data_cleaning.py
4. Run exploratory analysis and export the HTML report:
   python exploratory_analysis.py
   python -m nbconvert --to html exploratory_analysis.ipynb
