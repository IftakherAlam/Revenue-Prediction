from flask import Flask, jsonify
from model import train_arima_model

app = Flask(__name__)

@app.route('/api/predict', methods=['GET'])
def predict_revenue():
    data_path = r'D:\Revenue Forecasting\data.csv'
    
    
    forecast = train_arima_model(data_path)
    return jsonify(forecast.tolist())

if __name__ == '__main__':
    app.run(debug=True)
