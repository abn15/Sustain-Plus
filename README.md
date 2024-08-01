# SUSTAINPLUS

 A comprehensive app designed to help investors make informed decisions based on sustainability and ESG (Environmental, Social, and Governance) metrics. The app provides insights and recommendations for investments that prioritize sustainable practices and helps companies improve their ESG scores.

## Features
- **Performance Metrics:** Analyzing the companies current performance after taking various relevant fields as data and further comparing their performance against the top performer in their domain and sector, underdtanding the microparameters at which the company lacks.
- **Stock Performance Prediction:** Forecasting the relation between ESG and Stock value in long term to implement the risk management.
- **ESG Data:** Detailed ESG ratings and reports for various companies compiled and scraped from various sources.
- **Chatbot as a Consultant:** An interactive chatbot for answering queries and providing recommendations, based on data from latest public domain reports and providing smart suggstion for dealing with the new constraints.
- **Article Suggestions:** Analyzes latest data around popular consulting articles and give proper consulting using that data as a source of information.

## Installation

To set up and run the app locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/sustaininvest-pro.git
cd sustaininvest-pro
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Required Packages

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Prepare the Data

Ensure you have the necessary data files in the data directory. This includes:

esg_data.csv - ESG scores for companies.
news_data - Sentiment data for news articles.
company_data - Time series data for stock prices.


### 5. Run the Streamlit App

Start the Streamlit server to run the app:

```bash
streamlit run app.py
```

### 6. Access the App

Open your web browser and go to http://localhost:8501 to access the app.





