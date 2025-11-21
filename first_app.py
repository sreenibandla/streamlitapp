import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="School App", page_icon="🏫", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Student Enrollment"])

if page == "Home":
    st.title("School Dashboard")
    st.write("Welcome to the School Dashboard")

    # Key metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students", "1,234")
    col2.metric("New Enrollments (30 days)", "45")
    col3.metric("Attendance", "92%")

    st.markdown("---")

    # Enrollment trend (sample data)
    months = pd.date_range(end=pd.Timestamp.today(), periods=6, freq="M")
    enrollments = np.random.randint(20, 120, size=6)
    df_trend = pd.DataFrame({"Month": months, "Enrollments": enrollments}).set_index("Month")
    st.subheader("Enrollment Trend")
    st.line_chart(df_trend)

    # Sample breakdown
    st.subheader("Grade Distribution (sample)")
    grades = pd.DataFrame({"Grade": [f"Grade {i}" for i in range(1, 7)],
                           "Students": np.random.randint(50, 200, size=6)})
    st.bar_chart(grades.set_index("Grade"))

elif page == "Student Enrollment":
    st.title("Student Enrollment")
    st.write("Manage student enrollments and view enrollment statistics.")

    with st.form("enroll_form"):
        name = st.text_input("Student name")
        grade = st.selectbox("Grade", ["1","2","3","4","5","6"])
        submitted = st.form_submit_button("Enroll")
        if submitted:
            st.success(f"Enrolled {name} to grade {grade}")

    st.markdown("---")
    st.subheader("Recent Enrollments (sample)")
    recent = pd.DataFrame({"Name": ["Alice","Bob","Charlie"], "Grade": ["3","2","1"]})
    st.table(recent)
