🏡 House Price Prediction using Machine Learning
This project aims to predict house prices using regression models on the King County housing dataset. It includes data preprocessing, feature transformation, model building, evaluation, and deployment using Streamlit on AWS EC2.

📌 Project Overview
🔍 Goal: Predict house prices based on features like bedrooms, bathrooms, sqft_living, location, etc.

📊 Dataset: House Sales in King County, USA (includes 21 features and 1 target price)

🛠️ ML Models Used:

Linear Regression

Random Forest Regressor (Best Performing)

📁 Folder Structure
bash
Copy
Edit
house_price_regression/
│
├── app.py               # Streamlit app script
├── model.pkl            # Pickled trained ML model
├── scaler.pkl           # Pickled StandardScaler
├── data.csv             # Cleaned dataset (optional)
├── README.md            # Project description
└── requirements.txt     # Required packages
⚙️ Tech Stack
🐍 Python (pandas, scikit-learn, numpy)

📈 Streamlit (for UI)

☁️ AWS EC2 (for deployment)

🔧 Pickle (to save model and scaler)

📌 Steps Performed
Data Cleaning:

Removed duplicates, handled nulls

Dropped irrelevant features (like id, date)

Feature Engineering:

Log/BoxCox Transformations (to fix skewness)

Removed outliers (optional)

Feature scaling using StandardScaler

Model Training:

Used train_test_split (80/20)

Trained multiple regression models

Evaluated using:

R2 Score

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

Best Model:

✅ RandomForestRegressor gave highest R² score

Saved using pickle

Deployment:

Streamlit app built with form inputs

Hosted on AWS EC2

Opened port 8501 for public access

✅ Model Performance
Model	R2 Score	MAE	RMSE
Linear Regression	0.74	0.00029	0.00039
Gradient Boosting	0.85	0.00019	0.00028
Random Forest	0.85	0.00020	0.00029

