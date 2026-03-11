import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Neal's Analyst Reference Guide",
    page_icon="📊",
    layout="wide"
)

# 2. Enhanced Knowledge Base
data = {
    "Tool": [
        "SQL", "SQL", "SQL", "SQL", "SQL", "SQL",
        "Python", "Python", "Python", "Python", "Python", "Python",
        "PowerBI", "PowerBI", "PowerBI", "PowerBI",
        "Excel", "Excel", "Excel", "Excel"
    ],
    "Category": [
        "Window Functions", "Cleaning", "Logic", "Aggregates", "Joins", "Subqueries",
        "Pandas", "Pandas", "Visualization", "Visualization", "Cleaning", "Time Series",
        "DAX", "DAX", "Time Intelligence", "Filtering",
        "Lookup", "Arrays", "Cleaning", "Logic"
    ],
    "Function": [
        "RANK()", "COALESCE", "CASE WHEN", "HAVING", "LEFT JOIN", "CTE (WITH)",
        "df.merge()", "df.groupby()", "sns.barplot()", "plt.title()", "df.dropna()", "pd.to_datetime()",
        "CALCULATE", "DIVIDE", "DATESYTD", "ALLSELECTED",
        "XLOOKUP", "FILTER", "TEXTSPLIT", "LAMBDA"
    ],
    "Snippet": [
        "SELECT name, RANK() OVER (ORDER BY score DESC) as rank FROM table",
        "SELECT COALESCE(column, 0) -- Replaces NULL with 0",
        "CASE WHEN sales > 100 THEN 'High' ELSE 'Low' END",
        "GROUP BY category HAVING COUNT(*) > 5",
        "SELECT a.*, b.* FROM table_a a LEFT JOIN table_b b ON a.id = b.id",
        "WITH temp_table AS (SELECT * FROM original) SELECT * FROM temp_table",
        "pd.merge(df1, df2, on='id', how='left')",
        "df.groupby('category').agg({'sales': ['sum', 'mean']})",
        "sns.barplot(x='x_col', y='y_col', data=df)",
        "plt.title('My Chart Title')\nplt.xlabel('X Axis')",
        "df.dropna(subset=['important_column'])",
        "df['date'] = pd.to_datetime(df['date'])",
        "CALCULATE([Total Sales], 'Product'[Color] = \"Red\")",
        "DIVIDE([Numerator], [Denominator], 0)",
        "CALCULATE([Total Sales], DATESYTD('Date'[Date]))",
        "CALCULATE([Sales], ALLSELECTED('Table'))",
        "=XLOOKUP(A2, Range_A, Range_B, \"Not Found\")",
        "=FILTER(A2:B10, B2:B10 > 100)",
        "=TEXTSPLIT(A2, \"@\")",
        "=MAP(A2:A10, LAMBDA(x, x*1.1))"
    ],
    "Notes": [
        "Essential for 'Top N' reports (e.g., Top 3 players per team).",
        "Prevents math errors. Always wrap bonuses/discounts in this.",
        "The standard way to create categories/buckets in SQL.",
        "Filters data *after* it has been grouped.",
        "Keeps all records from the left table, even if no match on right.",
        "Common Table Expressions make complex queries readable.",
        "The primary way to combine datasets in Python.",
        "The 'Pivot Table' equivalent for data manipulation.",
        "Clean, professional categorical charts.",
        "Never forget to label your axes in a professional report!",
        "Removes rows with missing values to clean your data.",
        "Critical for any project involving dates (like Expense Trackers).",
        "The most important DAX function. Overrides filter context.",
        "Prevents #DIV/0 errors automatically.",
        "Calculates Year-to-Date totals effortlessly.",
        "Calculates totals based on what the user has currently filtered.",
        "The most powerful lookup tool in modern Excel.",
        "Returns a dynamic array of data matching criteria.",
        "Newer function to easily split strings (like emails).",
        "Advanced Excel for creating custom, reusable logic."
    ]
}

df_ref = pd.DataFrame(data)

# 3. Sidebar
st.sidebar.title("🛠️ Tools & Navigation")
view = st.sidebar.radio("Go to:", ["Cheat Sheet", "Visual Practice", "About the Dev"])
tool_filter = st.sidebar.multiselect("Select Tools", options=df_ref["Tool"].unique(), default=df_ref["Tool"].unique())

# 4. Main App Views
if view == "Cheat Sheet":
    st.title("📚 Analyst Knowledge Repository")
    st.write("A central hub for SQL, Python, Excel, and Power BI syntax.")
    
    search = st.text_input("Search functions or keywords (e.g., 'null' or 'join')...")
    
    filtered = df_ref[df_ref["Tool"].isin(tool_filter)]
    if search:
        filtered = filtered[filtered.apply(lambda row: search.lower() in row.astype(str).str.lower().to_string(), axis=1)]

    for _, row in filtered.iterrows():
        with st.expander(f"{row['Tool']} | {row['Function']} ({row['Category']})"):
            st.code(row['Snippet'], language='python' if row['Tool'] in ['Python', 'PowerBI'] else 'sql')
            st.info(row['Notes'])

elif view == "Visual Practice":
    st.title("🎯 Interview Drill Mode")
    st.write("Test your knowledge. Read the scenario and guess the code!")
    
    if st.button("Get Random Scenario"):
        random_row = df_ref.sample(1).iloc[0]
        st.session_state.current_ask = random_row
        
    if 'current_ask' in st.session_state:
        st.subheader(f"How would you: {st.session_state.current_ask['Notes']}")
        if st.button("Reveal Answer"):
            st.success(f"Tool: {st.session_state.current_ask['Tool']} | Function: {st.session_state.current_ask['Function']}")
            st.code(st.session_state.current_ask['Snippet'])

elif view == "About the Dev":
    st.title("👨‍💻 About Neal Kauffman")
    st.markdown("""
    **Current Focus:** Pursuing Data Analytics & Computer Systems (Collin College).  
    **Certifications:** Google Data Analytics Professional Certificate (In Progress).  
    **Specialties:** * Data Cleaning & SQL Optimization
    * Python (Pandas, Streamlit, Matplotlib)
    * Business Intelligence (Power BI & Excel)
    
    ---
    ### 🚀 Featured Projects
    * **Smart Expense Tracker:** A Streamlit dashboard for personal finance.
    * **Python Scoreboard App:** Real-time game tracking with custom UI.
    * **IMDb Data Warehouse:** SQL-based storage and querying for film data.
    """)
    st.sidebar.success("Deployment Successful!")
