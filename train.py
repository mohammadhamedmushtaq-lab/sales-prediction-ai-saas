import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data.csv")

X = df.drop("target", axis=1)
y = df["target"]

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=8,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "model.pkl")

print("✅ Stable sellable model trained")