import streamlit as st

def show_esg_page():
    st.title("ESG Data")

    st.header("Environmental, Social, and Governance (ESG) Data")
    st.write("""
    ESG data is crucial for investors who want to make informed decisions that align with their values.
    Here, you can explore detailed ESG ratings and reports for various companies, helping you to understand their
    impact on the environment, society, and their governance practices.
    """)

    st.header("Environmental Score")
    st.write("The environmental score measures the company's impact on the environment, including their carbon footprint, waste management, and use of renewable energy.")

    st.header("Social Score")
    st.write("The social score evaluates the company's relationships with its employees, suppliers, customers, and the communities where it operates. This includes labor practices, human rights, and social impact.")

    st.header("Governance Score")
    st.write("The governance score assesses the company's leadership, executive pay, audits, internal controls, and shareholder rights.")

    # Example ESG data table
    esg_data = {
        'Company': ['Company A', 'Company B', 'Company C'],
        'Environmental Score': [85, 70, 90],
        'Social Score': [75, 80, 65],
        'Governance Score': [95, 60, 85],
        'Total ESG Score': [85, 70, 80]
    }
    st.table(esg_data)

    st.markdown("---")
    st.write("© 2024 Sustainable Investing Management. All rights reserved.")
