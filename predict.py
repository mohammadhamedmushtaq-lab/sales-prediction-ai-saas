import joblib
import pandas as pd

model = joblib.load("model.pkl")

# ✔ SAME FEATURES AS TRAINING
data = pd.DataFrame([{
    "price": 25,
    "marketing": 300,
    "discount": 1,
    "category": 2,
    "customer_type": 1,
    "month": 6,
    "competition_price": 20
}])

pred = model.predict(data)[0]
features = joblib.load("features.pkl")
data = pd.DataFrame([[25,300,1,2,1,6,20]], columns=features)
print("Prediction:", pred)
