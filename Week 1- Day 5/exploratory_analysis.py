import numpy as np
import pandas as pd

df = pd.read_csv("clean_data.csv")
df["join_date"] = pd.to_datetime(df["join_date"])

reference_date = df["join_date"].max()
df["tenure_days"] = (reference_date - df["join_date"]).dt.days
df["join_date_missing_int"] = df["join_date_missing"].astype(int)
df["is_salary_outlier_int"] = df["is_salary_outlier"].astype(int)

numeric_cols = ["salary", "tenure_days"]
summary_stats = df[numeric_cols].agg(["mean", "median", "min", "max", "std"]).round(2)
print("=== Summary Statistics ===")
print(summary_stats.to_string())

dept_summary = (
    df.groupby("department", observed=False)
    .agg(
        employee_count=("employee_id", "count"),
        avg_salary=("salary", "mean"),
        median_salary=("salary", "median"),
        min_salary=("salary", "min"),
        max_salary=("salary", "max"),
        avg_tenure_days=("tenure_days", "mean"),
    )
    .round(2)
)
print("\n=== Group Summary by Department ===")
print(dept_summary.to_string())

corr_cols = ["salary", "tenure_days", "join_date_missing_int", "is_salary_outlier_int"]
corr_matrix = df[corr_cols].corr(numeric_only=True).round(3)
print("\n=== Correlation Matrix ===")
print(corr_matrix.to_string())

corr_pairs = []
cols = corr_matrix.columns
for i in range(len(cols)):
    for j in range(i + 1, len(cols)):
        val = corr_matrix.iloc[i, j]
        if pd.notna(val):
            corr_pairs.append((cols[i], cols[j], val, abs(val)))

corr_pairs.sort(key=lambda x: x[3], reverse=True)
print("\n=== Top 3 Numeric Relationships (by |r|) ===")
for rank, (c1, c2, r_val, _) in enumerate(corr_pairs[:3], start=1):
    print(f"{rank}. {c1} <-> {c2}: r = {r_val:.3f}")

dept_budget = pd.DataFrame({
    "department": ["Sales", "Engineering", "HR"],
    "annual_budget_inr": [400000, 900000, 300000],
})

merged_df = pd.merge(df, dept_budget, on="department", how="left")
budget_check = (
    merged_df.groupby("department", observed=False)
    .agg(
        headcount=("employee_id", "count"),
        total_salary=("salary", "sum"),
        annual_budget_inr=("annual_budget_inr", "first"),
    )
)
budget_check["budget_utilization_pct"] = (
    (budget_check["total_salary"] / budget_check["annual_budget_inr"]) * 100
).round(2)

print("\n=== Merged Department Budget vs. Actual Salary Spend ===")
print(budget_check.to_string())

q1_avg_salary = df["salary"].mean()
q1_med_salary = df["salary"].median()

q2_top_dept = dept_summary["avg_salary"].idxmax()
q2_top_dept_sal = dept_summary.loc[q2_top_dept, "avg_salary"]
q2_low_dept = dept_summary["avg_salary"].idxmin()
q2_low_dept_sal = dept_summary.loc[q2_low_dept, "avg_salary"]

q3_outlier_count = int(df["is_salary_outlier"].sum())
q3_outlier_names = df.loc[df["is_salary_outlier"], "name"].tolist()

q4_missing_date_count = int(df["join_date_missing"].sum())

q5_eng_util = budget_check.loc["Engineering", "budget_utilization_pct"]
q5_sales_util = budget_check.loc["Sales", "budget_utilization_pct"]

print("\n=== Business Questions & Answers ===")
print(f"Q1. What are the average and median salaries across cleaned employees? -> Mean: {q1_avg_salary:,.2f} INR | Median: {q1_med_salary:,.2f} INR")
print(f"Q2. Which department has the highest vs. lowest average salary? -> Highest: {q2_top_dept} ({q2_top_dept_sal:,.2f} INR) vs. Lowest: {q2_low_dept} ({q2_low_dept_sal:,.2f} INR)")
print(f"Q3. How many salary outliers exist via IQR, and who are they? -> {q3_outlier_count} outlier ({', '.join(q3_outlier_names)})")
print(f"Q4. How many employees had missing/invalid join dates flagged? -> {q4_missing_date_count} employee(s)")
print(f"Q5. How much of department budget is used by salaries in Engineering vs. Sales? -> Engineering: {q5_eng_util}% | Sales: {q5_sales_util}%")

pivot_tbl = pd.pivot_table(
    merged_df,
    values="salary",
    index="department",
    columns="is_salary_outlier",
    aggfunc="count",
    fill_value=0,
    observed=False,
)
print("\n=== Bonus: Pivot Table (Department vs. Salary Outlier Count) ===")
print(pivot_tbl.to_string())
