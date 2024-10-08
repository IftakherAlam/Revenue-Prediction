import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def train_arima_model(data_path):
    df = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')
    
    
    df = df.sort_index()

    
    model = ARIMA(df['Revenue'], order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=12)
    
    return forecast
