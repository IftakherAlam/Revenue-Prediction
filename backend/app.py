from flask import Flask, jsonify
from model import train_arima_model

app = Flask(__name__)

@app.route('/api/predict', methods=['GET'])
def predict_revenue():
    # Path to the data file (CSV containing Date and Revenue)
    data_path = r'D:\Revenue Forecasting\data.csv'
    
    # Call the function to predict future revenue
    forecast = train_arima_model(data_path)
    
    # Convert forecast to list and return as JSON
    return jsonify(forecast.tolist())

if __name__ == '__main__':
    app.run(debug=True)
