import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st
import io

# Function to create dataset
def create_dataset(dataset, time_step=1):
    X, Y = [], []
    for i in range(len(dataset)-time_step-1):
        a = dataset[i:(i+time_step), 0]
        X.append(a)
        Y.append(dataset[i + time_step, 0])
    return np.array(X), np.array(Y)

# Function to predict future values
def predict_future(model, data, days_to_predict):
    last_100_days = data[-100:].reshape(1, -1, 1)
    future_predictions = []
    for _ in range(days_to_predict):
        next_day_prediction = model.predict(last_100_days)
        future_predictions.append(next_day_prediction[0, 0])
        last_100_days = np.roll(last_100_days, -1, axis=1)
        last_100_days[0, -1, 0] = next_day_prediction
    return np.array(future_predictions).reshape(-1, 1)

# Load data and model
def load_model_and_data(tickers):
    data = {}
    scaled_data = {}
    scalers = {}
    models = {}
    
    for ticker in tickers:
        try:
            stock_data = yf.download(ticker, start="2010-01-01", end="2023-12-31")
            if not stock_data.empty:
                df = stock_data[['Close']]
                dataset = df.values
                scaler = MinMaxScaler(feature_range=(0,1))
                scaled = scaler.fit_transform(dataset)
                data[ticker] = dataset
                scaled_data[ticker] = scaled
                scalers[ticker] = scaler
                
                # Prepare dataset for training
                all_scaled_data = scaled_data[ticker]
                training_size = int(len(all_scaled_data) * 0.65)
                train_data, test_data = all_scaled_data[0:training_size,:], all_scaled_data[training_size:len(all_scaled_data),:]
                time_step = 100
                X_train, y_train = create_dataset(train_data, time_step)
                X_test, y_test = create_dataset(test_data, time_step)
                X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
                X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

                # Create the LSTM model
                model = Sequential()
                model.add(LSTM(50, return_sequences=True, input_shape=(100, 1)))
                model.add(LSTM(50, return_sequences=True))
                model.add(LSTM(50))
                model.add(Dense(1))
                model.compile(loss='mean_squared_error', optimizer='adam')
                
                # Train the model
                model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=1, batch_size=128, verbose=0)
                models[ticker] = model
            else:
                st.warning(f"No data available for {ticker}")
        except Exception as e:
            st.error(f"Error processing {ticker}: {str(e)}")
            
    return data, scaled_data, scalers, models

# Streamlit app
def main():
    st.title("Stock Price Prediction")
    
    tickers_input = st.text_input("Enter stock tickers (comma separated):", "AAPL,MSFT,AMZN,GOOGL,META")
    tickers = [ticker.strip().upper() for ticker in tickers_input.split(",")]
    
    if st.button("Get Predictions"):
        if len(tickers) == 0:
            st.error("Please enter at least one ticker.")
            return
        
        # Load model and data
        data, scaled_data, scalers, models = load_model_and_data(tickers)
        
        if not models:
            st.error("Failed to load models or data for the provided tickers.")
            return
        
        # Predict and display results
        prediction_periods = {
            "30_days": 30,
            "3_months": 90,
            "1_year": 365
        }
        
        predictions_dict = {ticker: {} for ticker in tickers}
        for ticker in tickers:
            if ticker in scaled_data:
                for period_name, period_days in prediction_periods.items():
                    future_predictions = predict_future(models[ticker], scaled_data[ticker], period_days)
                    actual_predictions = scalers[ticker].inverse_transform(future_predictions)
                    predictions_dict[ticker][period_name] = actual_predictions
                    
                    # Display predictions
                    st.write(f"\nPredicted stock prices for {ticker} for the next {period_name.replace('_', ' ')}:")
                    predictions_df = pd.DataFrame({
                        "Day": range(1, len(actual_predictions) + 1),
                        "Predicted_Price": actual_predictions.flatten()
                    })
                    st.write(predictions_df)
                    
                    # Plot trends
                    plt.figure(figsize=(10, 5))
                    plt.plot(data[ticker], label=f"{ticker} Actual")
                    plt.plot(range(len(data[ticker]), len(data[ticker]) + period_days), actual_predictions, label=f"{ticker} {period_name.replace('_', ' ')}")
                    plt.xlabel("Days")
                    plt.ylabel("Price")
                    plt.legend()
                    plt.title(f"Stock Price Predictions for {ticker}")
                    st.pyplot(plt.gcf())
                    plt.close()

if __name__ == "__main__":
    main()
