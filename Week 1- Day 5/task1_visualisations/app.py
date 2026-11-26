from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Employee Salary Visualisations", layout="wide")

st.title("Employee Salary Analysis — Two Key Charts")
st.write("Two charts from our Day 5 employee salary analysis.")

figures_dir = Path(__file__).parent / "reports" / "figures"

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Salary by Employee (Bar Chart)")
    st.image(str(figures_dir / "01_bar_salary_by_employee.png"), use_container_width=True)
    st.caption("Insight: Individual salaries vary around the 68,800 INR average.")

with col2:
    st.subheader("2. Salary Spread (Box Plot)")
    st.image(str(figures_dir / "05_boxplot_salary_spread.png"), use_container_width=True)
    st.caption("Insight: Salaries stay in a compact central band with no extreme outliers.")
