import pickle
import pandas as pd
from flask import Flask, request, jsonify

# Init flask app
app = Flask(__name__)

# Load the saved model from the file `saved_model.pkl`
with open("saved_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)


# The app will live behind a URL.  Let's say: myapp.com
# Adding this route at `/predict` will mean users
# will request a prediction from `myapp.com/predict`.
# This needs to a POST request that contains the
# features needed for the model to make a prediction
# (see `request_prediction.py`).
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
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

    # Extract data from JSON and convert to a DataFrame
    df = pd.DataFrame(data["data"])

    # Make predictions on new data
    y_pred = loaded_model.predict(df)

    # Put predictions into a dictionary for conversion to JSON
    predictions = {"predictions": y_pred.tolist()}

    # Make into JSON and return data to respond to user request
    return jsonify(predictions)


if __name__ == "__main__":
    # Run app on specified port to await requests
    app.run(port=5555, threaded=True)
