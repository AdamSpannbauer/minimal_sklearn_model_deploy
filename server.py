import pickle
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

with open("saved_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data["data"])

    y_pred = loaded_model.predict(df)
    predictions = {"predictions": y_pred.tolist()}

    return jsonify(predictions)


if __name__ == "__main__":
    app.run(port=5555, threaded=True)
