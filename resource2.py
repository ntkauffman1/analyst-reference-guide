import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 Analyst Reference", layout="wide")

# 1. Expanded Knowledge Base
data = {
    "Tool": [
        "SQL", "SQL", "SQL", "SQL", 
        "Python", "Python", "Python", "Python",
        "PowerBI", "PowerBI", "PowerBI",
        "Excel", "Excel", "Excel"
    ],
    "Category": [
        "Window Functions", "Cleaning", "Logic", "Aggregates",
        "Pandas", "Pandas", "Pandas", "Time Series",
        "DAX", "DAX", "Time Intelligence",
        "Lookup", "Arrays", "Cleaning"
    ],
    "Function": [
        "RANK() / ROW_NUMBER()", "TRIM / REPLACE", "COALESCE", "HAVING",
        "df.groupby().agg()", "df.merge()", "df.pivot_table()", "pd.to_datetime()",
        "CALCULATE", "DIVIDE", "SAMEPERIODLASTYEAR",
        "XLOOKUP", "UNIQUE / FILTER", "TEXTBEFORE / TEXTAFTER"
    ],
    "Snippet": [
        "RANK() OVER (PARTITION BY category ORDER BY sales DESC)",
        "SELECT TRIM(REPLACE(column, 'Old', 'New'))",
        "SELECT COALESCE(bonus, 0) + salary",
        "GROUP BY 1 HAVING SUM(sales) > 1000",
        "df.groupby('cat')['val'].agg(['sum', 'mean'])",
        "pd.merge(df1, df2, on='id', how='left')",
        "df.pivot_table(index='date', columns='cat', values='rev')",
        "df['date'] = pd.to_datetime(df['date'])",
        "CALCULATE([Total Sales], ALL(Products))",
        "DIVIDE([Profit], [Revenue], 0)",
        "CALCULATE([Sales], SAMEPERIODLASTYEAR('Calendar'[Date]))",
        "=XLOOKUP(A2, Range1, Range2, 'Not Found')",
        "=UNIQUE(FILTER(A2:B10, B2:B10 > 100))",
        "=TEXTBEFORE(A2, '@')"
    ],
    "Notes": [
        "Essential for top-N analysis (e.g., Top 5 scores per team).",
        "Removes hidden spaces that break JOINS.",
        "Prevents math errors when dealing with NULLs.",
        "Filters aggregated data (unlike WHERE which filters rows).",
        "The 'Pivot Table' of Python.",
        "The Python version of a SQL JOIN.",
        "Reshapes data for easier visualization.",
        "Essential for trend analysis and time-based filtering.",
        "The most powerful DAX function—overrides filter context.",
        "Safe division that avoids #DIV/0! errors.",
        "Standard YoY (Year-over-Year) comparison tool.",
        "The modern, more flexible replacement for VLOOKUP.",
        "Dynamic arrays that automatically update.",
        "Cleans messy strings without complex formulas."
    ]
}

df_ref = pd.DataFrame(data)

# 2. Sidebar Navigation
st.sidebar.header("Navigation")
view = st.sidebar.radio("Go to:", ["Cheat Sheet", "Visual Practice"])
tool_filter = st.sidebar.multiselect("Select Tools", options=df_ref["Tool"].unique(), default=df_ref["Tool"].unique())

# 3. Main UI
if view == "Cheat Sheet":
    st.title("📚 Analyst Knowledge Repository")
    search = st.text_input("Search functions or keywords...")
    
    # Filtering logic
    filtered = df_ref[df_ref["Tool"].isin(tool_filter)]
    if search:
        filtered = filtered[filtered.apply(lambda row: search.lower() in row.astype(str).str.lower().to_string(), axis=1)]

    for _, row in filtered.iterrows():
        with st.expander(f"{row['Tool']} | {row['Function']}"):
            st.code(row['Snippet'])
            st.info(row['Notes'])

elif view == "Visual Practice":
    st.title("🎯 Quick Drill")
    st.write("Can you guess the tool/function based on the note?")
    random_row = df_ref.sample(1).iloc[0]
    st.subheader(f"Scenario: {random_row['Notes']}")
    
    if st.button("Reveal Answer"):
        st.success(f"Tool: {random_row['Tool']} | Function: {random_row['Function']}")
        st.code(random_row['Snippet'])