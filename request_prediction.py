import requests
import pandas as pd

# If running server locally on port 5555:
# url = "http://localhost:5555/predict"

# If running server remotely at `frozen-island-12625.herokuapp.com`
url = "http://frozen-island-12625.herokuapp.com/predict"

# Load data from file and sample records for prediction
df = pd.read_csv("data/penguins.csv")
df = df.sample(2)

# Separate input features and target
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

# Request a prediction from the model REST API
response = requests.post(url, json=data)
predictions = response.json()

# Example predictions:
# {"predictions": ["Chinstrap", "Gentoo"]}

# Display predictions and correct labels
print(f"\nRight answer(s): {y.tolist()}")
print(f"Prediction(s): {predictions['predictions']}")
