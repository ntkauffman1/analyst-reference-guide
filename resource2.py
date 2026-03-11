import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Neal's Analyst Reference Guide",
    page_icon="📊",
    layout="wide"
)

# 2. Comprehensive Knowledge Base
data = {
    "Tool": [
        "SQL", "SQL", "SQL", "SQL", "SQL", "SQL",
        "Python", "Python", "Python", "Python", "Python", "Python",
        "Power BI", "Power BI", "Power BI", "Power BI",
        "Tableau", "Tableau", "Tableau",
        "Excel", "Excel", "Excel", "Excel", "Excel", "Excel", "Excel", "Excel", "Excel", "Excel", "Excel", "Excel", "Excel"
    ],
    "Category": [
        "Window Functions", "Cleaning", "Logic", "Aggregates", "Joins", "Subqueries",
        "Pandas", "Pandas", "Visualization", "Visualization", "Cleaning", "Time Series",
        "DAX", "DAX", "Time Intelligence", "Filtering",
        "LOD Expressions", "Calculations", "Formatting",
        "Math & Stats", "Math & Stats", "Math & Stats", "Text", "Text", "Text", "Logic", "Logic", "Lookup", "Lookup", "Lookup", "Date", "Criteria"
    ],
    "Function": [
        "RANK()", "COALESCE", "CASE WHEN", "HAVING", "LEFT JOIN", "CTE (WITH)",
        "df.merge()", "df.groupby()", "sns.barplot()", "plt.title()", "df.dropna()", "pd.to_datetime()",
        "CALCULATE", "DIVIDE", "DATESYTD", "ALLSELECTED",
        "FIXED LOD", "ZN()", "ATTR()",
        "SUM / AVERAGE", "MIN / MAX", "COUNT / POWER", "CONCAT / TEXTJOIN", "TRIM", "LEFT / RIGHT / MID", 
        "IF / AND / OR", "UPPER / PROPER", "VLOOKUP", "HLOOKUP", "INDEX + MATCH", "TODAY / DATEDIF", "SUMIFS / COUNTIFS"
    ],
    "Snippet": [
        "SELECT name, RANK() OVER (ORDER BY score DESC) as rank FROM table",
        "SELECT COALESCE(column, 0)",
        "CASE WHEN sales > 100 THEN 'High' ELSE 'Low' END",
        "GROUP BY category HAVING COUNT(*) > 5",
        "SELECT a.*, b.* FROM table_a a LEFT JOIN table_b b ON a.id = b.id",
        "WITH temp_table AS (SELECT * FROM original) SELECT * FROM temp_table",
        "pd.merge(df1, df2, on='id', how='left')",
        "df.groupby('category').agg({'sales': ['sum', 'mean']})",
        "sns.barplot(x='x_col', y='y_col', data=df)",
        "plt.title('My Chart Title')",
        "df.dropna(subset=['important_column'])",
        "df['date'] = pd.to_datetime(df['date'])",
        "CALCULATE([Total Sales], 'Product'[Color] = \"Red\")",
        "DIVIDE([Numerator], [Denominator], 0)",
        "CALCULATE([Total Sales], DATESYTD('Date'[Date]))",
        "CALCULATE([Sales], ALLSELECTED('Table'))",
        "{ FIXED [Region] : SUM([Sales]) }",
        "ZN([Sales]) -- Returns 0 if NULL",
        "ATTR([Category]) -- Checks if 1 value exists",
        "=SUM(A2:A10) / =AVERAGE(A2:A10)",
        "=MIN(A2:A10) / =MAX(A2:A10)",
        "=COUNT(A2:A10) / =POWER(A2, 2)",
        "=CONCAT(A2, \" \", B2) or =TEXTJOIN(\" \", TRUE, A2:B2)",
        "=TRIM(A2)",
        "=LEFT(A2, 3) / =RIGHT(A2, 2) / =MID(A2, 3, 4)",
        "=IF(AND(A2>=70, B2=\"Complete\"), \"Pass\", \"Check\")",
        "=UPPER(A2) / =PROPER(A2)",
        "=VLOOKUP(A2, $D$2:$F$100, 3, FALSE)",
        "=HLOOKUP(A2, $D$1:$H$10, 3, FALSE)",
        "=INDEX(F:F, MATCH(A2, D:D, 0))",
        "=TODAY() / =DATEDIF(A2, B2, \"d\")",
        "=SUMIFS(B:B, A:A, \"North\", C:C, \">100\")"
    ],
    "Notes": [
        "Essential for ranking (e.g., Top scores per team).",
        "Replaces NULL with a default value.",
        "SQL's version of an IF statement.",
        "Filters grouped data (must come after GROUP BY).",
        "Returns all rows from left table, and matched from right.",
        "Creates a temporary result set for cleaner code.",
        "Combines dataframes (like a SQL JOIN).",
        "Aggregates data by category.",
        "Creates categorical bar charts.",
        "Professional chart labeling.",
        "Removes rows with missing data.",
        "Converts strings to date objects for analysis.",
        "The power-user function for DAX.",
        "Safe division (prevents #DIV/0!).",
        "Standard Year-to-Date calculation.",
        "Considers only the currently active filters.",
        "Level of Detail expression; ignores view dimensions.",
        "Zero Null; prevents blank marks in charts.",
        "Returns '*' if multiple values are in a single mark.",
        "Basic arithmetic and mean calculation.",
        "Finding range boundaries.",
        "Numeric counting and exponents.",
        "Merging text strings together.",
        "Removes all extra spaces from text.",
        "Extracting specific parts of a string.",
        "Multi-condition logical testing.",
        "Formatting text case for clean reports.",
        "Vertical lookup by first column.",
        "Horizontal lookup across the first row.",
        "More flexible and powerful than VLOOKUP.",
        "Dynamic dates and age/tenure calculations.",
        "Sum or count only when specific criteria are met."
    ]
}

df_ref = pd.DataFrame(data)

# 3. Sidebar Navigation
st.sidebar.title("📊 Analyst Hub")
st.sidebar.markdown("[Go to Main Portfolio](https://data-analytics-portfolio-ntkauffman.streamlit.app/)")
st.sidebar.divider()

main_nav = st.sidebar.radio("Navigation", ["Cheat Sheet", "Visual Practice", "About Neal"])

# 4. App Views
if main_nav == "Cheat Sheet":
    st.title("📚 Knowledge Repository")
    st.write("Browse common functions organized by tool.")
    
    # Nested Tabs for Tools
    tab_sql, tab_py, tab_ex, tab_pbi, tab_tab = st.tabs(["SQL", "Python", "Excel", "Power BI", "Tableau"])
    
    search = st.text_input("Search across all categories (e.g., 'null' or 'lookup')...")

    def display_filtered_content(tool_name):
        filtered = df_ref[df_ref["Tool"] == tool_name]
        if search:
            filtered = filtered[filtered.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
        
        if filtered.empty:
            st.write("No matching functions found in this tab.")
        for _, row in filtered.iterrows():
            with st.expander(f"{row['Function']} ({row['Category']})"):
                st.code(row['Snippet'], language='python' if tool_name in ['Python', 'Power BI'] else 'sql')
                st.write(f"**Insight:** {row['Notes']}")

    with tab_sql: display_filtered_content("SQL")
    with tab_py: display_filtered_content("Python")
    with tab_ex: display_filtered_content("Excel")
    with tab_pbi: display_filtered_content("Power BI")
    with tab_tab: display_filtered_content("Tableau")

elif main_nav == "Visual Practice":
    st.title("🎯 Technical Drill")
    st.write("Test your memory! Select tools and guess the formula.")
    
    # Filter moved here per request
    tool_filter = st.sidebar.multiselect("Select Tools for Practice", options=df_ref["Tool"].unique(), default=df_ref["Tool"].unique())
    
    if st.button("New Challenge"):
        practice_df = df_ref[df_ref["Tool"].isin(tool_filter)]
        if not practice_df.empty:
            st.session_state.challenge = practice_df.sample(1).iloc[0]
        else:
            st.warning("Please select at least one tool in the sidebar.")
        
    if 'challenge' in st.session_state:
        st.info(f"**How would you:** {st.session_state.challenge['Notes']}")
        if st.button("Show Answer"):
            st.success(f"Tool: {st.session_state.challenge['Tool']} | Function: {st.session_state.challenge['Function']}")
            st.code(st.session_state.challenge['Snippet'])

elif main_nav == "About Neal":
    st.title("👨‍💻 Neal Kauffman")
    st.write("Online Data Researcher & Computer Systems Student")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Core Competencies
        * **Languages:** Python, SQL
        * **Tools:** Power BI, Tableau, Excel
        * **Education:** Collin College (Dean's List)
        * **Cert:** Google Data Analytics
        """)
    with col2:
        st.markdown("### Primary Portfolio")
        st.info("Check out my full project gallery here:")
        st.markdown("[Visit Portfolio Site](https://data-analytics-portfolio-ntkauffman.streamlit.app/)")
