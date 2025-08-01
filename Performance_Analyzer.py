import streamlit as st
import pandas as pd
from fpdf import FPDF
import tempfile


st.title("📊 Student Performance Analyzer")

uploaded_file = st.file_uploader("📂 Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)

    st.write("### 🧾 Uploaded Data")
    st.dataframe(dataframe)


    st.write("### 📈 Overall Bar Chart")
    st.bar_chart(dataframe.set_index("Name").drop(columns=["Student ID"], errors='ignore'))

    options = ["English", "History", "ICT","Math","Science"]
    selected_option = st.selectbox("Select an option:", options)
    st.write("You selected:", selected_option)
    if selected_option=="Math":
        st.write("### 📊 Math Performance Trend")
        st.line_chart(dataframe["Math"])
    elif selected_option=="ICT":
        st.write("### 📊 ICT Performance Trend")
        st.line_chart(dataframe["ICT"])
    elif selected_option=="Science":
        st.write("### 📊 Science Performance Trend")
        st.line_chart(dataframe["Science"])
    elif selected_option=="English":
        st.write("### 📊 English Performance Trend")
        st.line_chart(dataframe["English"])
    else:
        st.write("### 📊 History Performance Trend")
        st.line_chart(dataframe["History"])
        
    student_names = dataframe["Name"].unique()
    selected_student = st.selectbox("📛 Select a student for PDF report", student_names)
    if selected_student:
        student_row = dataframe[dataframe["Name"] == selected_student].iloc[0]
        scores = {
            "English": student_row["English"],
            "History": student_row["History"],
            "ICT": student_row["ICT"],
            "Math": student_row["Math"],
            "Science": student_row["Science"],

        }
        feedback = []
        for subject, score in scores.items():
            if score >= 80:
                feedback.append(f"Excellent in {subject}")
            elif score >= 50:
                feedback.append(f"Average in {subject}, could improve")
            else:
                feedback.append(f"Needs improvement in {subject}")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, f"Student Report: {selected_student}", ln=True, align="C")

        pdf.set_font("Arial", "", 12)
        pdf.ln(10)
        pdf.cell(200, 10, f"Student ID: {student_row.get('Student ID', 'N/A')}", ln=True)

        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, "Scores:", ln=True)
        pdf.set_font("Arial", "", 12)
        for subject, score in scores.items():
            pdf.cell(200, 10, f"{subject}: {score}", ln=True)

        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, "AI Recommendations:", ln=True)
        pdf.set_font("Arial", "", 12)
        for tip in feedback:
            pdf.cell(200, 10, f"- {tip}", ln=True)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            pdf.output(tmp_file.name)
            st.download_button(
                label="📄 Download PDF Report",
                data=open(tmp_file.name, "rb").read(),
                file_name=f"{selected_student}_report.pdf",
                mime="application/pdf"
            )







