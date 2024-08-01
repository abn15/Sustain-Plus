import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import plotly.express as px

@st.cache_data
def preprocess_esg_data(esg_data):
    numeric_cols = ['environment_score', 'social_score', 'governance_score', 'total_score']
    esg_data[numeric_cols] = esg_data[numeric_cols].fillna(esg_data[numeric_cols].mean())
    return esg_data

@st.cache_data
def preprocess_sentiment_data(news_data):
    sentiment_scores = {}
    for company, data in news_data.items():
        if 'feed' in data:
            sentiments = [article['overall_sentiment_score'] for article in data['feed']]
            sentiment_scores[company] = np.mean(sentiments) if sentiments else 0
        else:
            sentiment_scores[company] = 0
    return pd.DataFrame(list(sentiment_scores.items()), columns=['Company', 'SentimentScore'])

@st.cache_data
def preprocess_time_series_data(company_data):
    price_data = {}
    for company, data in company_data.items():
        prices = [float(value['4. close']) for date, value in data['Time Series (Daily)'].items()]
        price_data[company] = np.mean(prices) if prices else 0
    return pd.DataFrame(list(price_data.items()), columns=['Company', 'AveragePrice'])

@st.cache_data
def feature_engineering(esg_data, sentiment_data, price_data):
    esg_data = esg_data.rename(columns={'ticker': 'Company'})
    esg_data['Company'] = esg_data['Company'].str.upper()
    sentiment_data['Company'] = sentiment_data['Company'].str.upper()
    price_data['Company'] = price_data['Company'].str.upper()
    merged_data = esg_data.merge(sentiment_data, on='Company').merge(price_data, on='Company')

    # Add a dummy RecommendationScore for testing
    merged_data['RecommendationScore'] = np.random.randint(1, 10, size=len(merged_data))

    return merged_data

def train_model(data):
    numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
    X = data[numeric_cols].drop(columns=['RecommendationScore'])
    y = data['RecommendationScore']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model, scaler

def predict_investments(model, scaler, data):
    numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
    X = data[numeric_cols].drop(columns=['RecommendationScore'])
    X = scaler.transform(X)
    predictions = model.predict(X)
    data['RecommendationScore'] = predictions
    result = data[['Company', 'RecommendationScore']].sort_values(by='RecommendationScore', ascending=False)
    result.columns = ['Name', 'RecommendationScore']
    return result

def plot_histogram(data):
    fig = px.histogram(data, x='RecommendationScore', nbins=10,
                       title='Distribution of Recommendation Scores',
                       color_discrete_sequence=['#1f77b4'])
    st.plotly_chart(fig)

def plot_line_chart(data):
    fig = px.line(data, x='Name', y='RecommendationScore',
                  title='Trend of Recommendation Scores',
                  markers=True, color_discrete_sequence=['#ff7f0e'])
    fig.update_layout(xaxis_title='Company', yaxis_title='Recommendation Score', xaxis_tickangle=-45)
    st.plotly_chart(fig)

def show_stock_prediction_page():
    st.title('Stock Recommendation Application')

    esg_data = pd.read_csv('esg_data.csv')

    news_data = {
        'DIS': {'feed': [{'overall_sentiment_score': 0.5}, {'overall_sentiment_score': 0.7}]},
        'GM': {'feed': [{'overall_sentiment_score': 0.6}, {'overall_sentiment_score': 0.4}]},
        'GWW': {'feed': [{'overall_sentiment_score': 0.5}, {'overall_sentiment_score': 0.5}]},
        'MHK': {'feed': [{'overall_sentiment_score': 0.4}, {'overall_sentiment_score': 0.6}]},
        'LYV': {'feed': [{'overall_sentiment_score': 0.7}, {'overall_sentiment_score': 0.5}]},
        'LVS': {'feed': [{'overall_sentiment_score': 0.6}, {'overall_sentiment_score': 0.5}]},
        'CLX': {'feed': [{'overall_sentiment_score': 0.5}, {'overall_sentiment_score': 0.7}]},
        'AACG': {'feed': [{'overall_sentiment_score': 0.5}, {'overall_sentiment_score': 0.6}]},
        'AAL': {'feed': [{'overall_sentiment_score': 0.6}, {'overall_sentiment_score': 0.4}]},
        'AAME': {'feed': [{'overall_sentiment_score': 0.5}, {'overall_sentiment_score': 0.5}]}
    }

    company_data = {
        'DIS': {'Time Series (Daily)': {'2024-07-30': {'4. close': '95.5'}, '2024-07-29': {'4. close': '96.0'}}},
        'GM': {'Time Series (Daily)': {'2024-07-30': {'4. close': '40.3'}, '2024-07-29': {'4. close': '41.0'}}},
        'GWW': {'Time Series (Daily)': {'2024-07-30': {'4. close': '500.0'}, '2024-07-29': {'4. close': '495.5'}}},
        'MHK': {'Time Series (Daily)': {'2024-07-30': {'4. close': '100.0'}, '2024-07-29': {'4. close': '101.0'}}},
        'LYV': {'Time Series (Daily)': {'2024-07-30': {'4. close': '65.0'}, '2024-07-29': {'4. close': '66.0'}}},
        'LVS': {'Time Series (Daily)': {'2024-07-30': {'4. close': '60.0'}, '2024-07-29': {'4. close': '61.0'}}},
        'CLX': {'Time Series (Daily)': {'2024-07-30': {'4. close': '150.0'}, '2024-07-29': {'4. close': '151.0'}}},
        'AACG': {'Time Series (Daily)': {'2024-07-30': {'4. close': '2.0'}, '2024-07-29': {'4. close': '2.1'}}},
        'AAL': {'Time Series (Daily)': {'2024-07-30': {'4. close': '20.0'}, '2024-07-29': {'4. close': '21.0'}}},
        'AAME': {'Time Series (Daily)': {'2024-07-30': {'4. close': '4.0'}, '2024-07-29': {'4. close': '4.1'}}}
    }

    esg_data = preprocess_esg_data(esg_data)
    sentiment_data = preprocess_sentiment_data(news_data)
    price_data = preprocess_time_series_data(company_data)
    merged_data = feature_engineering(esg_data, sentiment_data, price_data)

    st.write("### Merged Data for Stock Recommendation")
    st.dataframe(merged_data)

    model, scaler = train_model(merged_data)

    recommended_investments = predict_investments(model, scaler, merged_data)
    st.write("### Recommended Investments")
    st.dataframe(recommended_investments)

    st.write("### Data Visualization")
    plot_histogram(recommended_investments)
    plot_line_chart(recommended_investments)
