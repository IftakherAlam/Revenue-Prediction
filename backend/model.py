import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def train_arima_model(data_path):
    # Load the dataset
    df = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')
    
    # Ensure the data is sorted by date
    df = df.sort_index()

    # Use ARIMA model for time series prediction
    model = ARIMA(df['Revenue'], order=(5, 1, 0))
    model_fit = model.fit()
    
    # Forecast the next 12 months
    forecast = model_fit.forecast(steps=12)
    
    return forecast
