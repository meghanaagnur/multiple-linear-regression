import pandas as pd
import math
import joblib
from sklearn.linear_model import LinearRegression

df = pd.read_csv("01-House-Price-Prediction/data/homeprice.csv")
df.columns = df.columns.str.strip()

median = math.floor(df["bedroom"].median())
df["bedroom"] = df["bedroom"].fillna(median)

reg = LinearRegression()
reg.fit(df[["area", "bedroom", "age"]], df["price"])

joblib.dump(reg, "model.pkl")

print("Model saved successfully!")