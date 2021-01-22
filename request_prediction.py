import requests
import pandas as pd

url = "http://localhost:5555/predict"

df = pd.read_csv("data/penguins.csv")
df = df.sample(2)

X = df.drop(columns="species")
y = df["species"]

# Convert data to JSON like structure
data = {"data": X.to_dict(orient="records")}

# Example data:
# {
#     "data": [
#         {
#             "island": "Torgersen",
#             "bill_length_mm": 35.1,
#             "bill_depth_mm": 19.4,
#             "flipper_length_mm": 193.0,
#             "body_mass_g": 4200.0,
#             "is_male": 1,
#         }
#     ]
# }

response = requests.post(url, json=data)
predictions = response.json()

# Example response:
# {"predictions": ["Chinstrap", "Gentoo"]}

print(f"\nRight answer(s): {y.tolist()}")
print(f"Prediction(s): {predictions['predictions']}")
