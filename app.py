import streamlit as st
from landing_page import show_landing_page
from app_stock_prediction import show_stock_prediction_page
from app_esg import show_esg_page
from chatbot import show_chatbot_page
from article_suggestion import show_article_suggestions_page
from app_stock_price_prediction import show_stock_price_prediction_page

# Set up the main configuration
st.set_page_config(page_title="Sustainable Investing Management", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
            padding: 20px;
        }
        .sidebar .sidebar-content .block-container {
            padding: 20px;
        }
        .sidebar .sidebar-content .stButton button {
            width: 100%;
            padding: 10px;
            font-size: 16px;
        }
        .stTitle {
            color: #2c3e50;
            text-align: center;
        }
        .stHeader {
            color: #34495e;
        }
        .stText {
            color: #2c3e50;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
pages = ["Landing Page", "Stock Prediction", "Stock Price Prediction", "ESG Data", "Chatbot", "Article Suggestions"]
page = st.sidebar.radio("Go to", pages)

# Page routing
if page == "Landing Page":
    show_landing_page()
elif page == "Stock Prediction":
    show_stock_prediction_page()
elif page == "Stock Price Prediction":
    show_stock_price_prediction_page()
elif page == "ESG Data":
    show_esg_page()
elif page == "Chatbot":
    show_chatbot_page()
elif page == "Article Suggestions":
    show_article_suggestions_page()

# Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2024 Sustainable Investing Management. All rights reserved.")
