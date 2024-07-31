import streamlit as st

# Define pages as functions
def show_company_page():
    st.header("Companies Seeking Sustainability Goals")
    st.write("""
    **Welcome Companies!**  
    Here you can find resources and support to help meet your sustainability goals. 
    We offer guidance on ESG compliance, sustainable practices, and more.
    
    - Explore best practices in sustainability.
    - Connect with experts for tailored advice.
    - Access tools to measure and track your ESG performance.
    """)
    
def show_investor_page():
    st.header("Investors Looking for Sustainable Options")
    st.write("""
    **Welcome Investors!**  
    Explore a range of investment options that prioritize sustainability and ethical practices. 
    Our platform offers insights into sustainable funds, green bonds, and ESG-compliant companies.
    
    - Discover top-performing sustainable investments.
    - Access detailed ESG ratings and reports.
    - Receive personalized investment recommendations based on your sustainability goals.
    """)

# Title of the app
st.title("Sustainable Investing Management")

# Introduction section
st.header("Welcome to Your Sustainable Investing Dashboard")
st.write("""

""")

# Benefits of sustainable investing
st.header("Why Sustainable Investing?")
st.write("""
### 1. Positive Environmental Impact
Investing in sustainable projects helps in reducing carbon footprint and promoting renewable energy.

### 2. Social Responsibility
Support companies and projects that prioritize ethical practices and contribute to social well-being.

### 3. Long-term Financial Returns
Sustainable investments often lead to better financial performance due to their focus on long-term growth and risk management.

### 4. Regulatory Compliance
Stay ahead of regulatory requirements by investing in companies that comply with environmental, social, and governance (ESG) standards.
""")

# Display buttons to navigate to different sections
if st.button("Companies Seeking Sustainability Goals"):
    show_company_page()

elif st.button("Investors Looking for Sustainable Options"):
    show_investor_page()

# Footer
st.markdown("---")
st.write("© 2024 Sustainable Investing Management. All rights reserved.")
