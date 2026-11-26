import pandas as pd

df = pd.read_csv("raw_data.csv")

before_rows = len(df)
before_duplicates = int(df.duplicated().sum())

df = df.drop_duplicates().copy()

df["name"] = df["name"].fillna("").astype(str).str.strip().str.title()
df["name"] = df["name"].replace("", pd.NA)

df["department"] = df["department"].fillna("").astype(str).str.strip().str.title()
df["department"] = df["department"].replace("", pd.NA)

df["email"] = df["email"].fillna("").astype(str).str.strip().str.lower()
df["email"] = df["email"].replace("", pd.NA)

df["employee_id"] = pd.to_numeric(df["employee_id"], errors="coerce").astype("Int64")
df["salary"] = pd.to_numeric(
    df["salary"].fillna("").astype(str).str.replace(r"[^0-9.]", "", regex=True),
    errors="coerce",
)
df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")

before_missing = int(df.isna().sum().sum())

df = df.dropna(subset=["employee_id"]).copy()

df["join_date_missing"] = df["join_date"].isna()
valid_dates = df["join_date"].dropna()
fill_date = valid_dates.median() if not valid_dates.empty else pd.Timestamp("2024-01-01")
df["join_date"] = df["join_date"].fillna(fill_date)

median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary if pd.notna(median_salary) else 0)

dept_modes = df["department"].dropna().mode()
mode_dept = dept_modes.iloc[0] if not dept_modes.empty else "General"
df["department"] = df["department"].fillna(mode_dept).astype("category")

df["name"] = df["name"].fillna("Unknown Employee")
df["email"] = df["email"].fillna("unknown@example.com")

q1 = df["salary"].quantile(0.25)
q3 = df["salary"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

df["is_salary_outlier"] = (df["salary"] < lower_bound) | (df["salary"] > upper_bound)

after_rows = len(df)
after_missing = int(df.isna().sum().sum())
after_duplicates = int(df.duplicated().sum())

summary = pd.DataFrame({
    "Metric": ["Rows", "Missing Values", "Duplicate Rows"],
    "Before": [before_rows, before_missing, before_duplicates],
    "After": [after_rows, after_missing, after_duplicates],
})
print(summary.to_string(index=False))

df.to_csv("clean_data.csv", index=False)
print("\nSaved clean_data.csv successfully.")