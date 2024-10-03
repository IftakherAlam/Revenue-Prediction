# Revenue Prediction Web Application
This web application predicts future revenue for the next 12 months based on historical monthly revenue data. It uses a Python backend (Flask) to handle the prediction logic, and a React frontend to display the predictions visually.

# Features
Backend: Python with Flask for training the model and predicting future revenue based on historical data.
Frontend: React (with Material UI) for fetching and displaying the predicted revenue in a clean, responsive UI.
Prediction Model: Uses a simple machine learning model (e.g ARIMA) to predict future revenue.
## root/
``` ├── backend/
│   ├── app.py                # Flask app handling API requests
│   ├── model.py              # Python script for loading data, training, and predicting
│   ├── data.csv              # Historical revenue data file
│   └── requirements.txt      # Backend dependencies
├── frontend/
│   ├── public/
│   │   └── index.html        # Main HTML file
│   ├── src/
│   │   ├── App.js            # Main React component
│   │   ├── index.js          # Entry point for React app
│   │   ├── components/
│   │   │   └── Chart.js      # Component for graph/chart rendering
│   ├── package.json          # Frontend dependencies
├── README.md                 # Documentation
└── .gitignore                # Git ignore file
```

## Backend (Python - Flask)
The backend is built using Flask, a lightweight Python web framework. It is responsible for:
Data Loading: Reading historical revenue data from a CSV file.
Model Training: Using a Linear Regression model from sklearn to fit the historical data.
Making Predictions: Predicting revenue for the next 12 months.
Serving Predictions: Exposing an API endpoint (/api/predict) that returns the predicted values in JSON format.

## Frontend (React - Material UI)
The frontend is built using React and Material UI for a clean and responsive user interface. It fetches predictions from the Flask backend and displays them on the page.
