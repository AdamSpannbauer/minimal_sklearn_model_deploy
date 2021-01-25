import pickle

import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

MODEL_OUTPUT_PATH = "saved_model.pkl"

print("Reading and prepping data...")
df = pd.read_csv("data/penguins.csv")

# Separating features by data type
num_cols = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
bin_cols = ["is_male"]
cat_cols = ["island"]
drop_cats = ["Biscoe"]

# Separate input features and target -> train/test split
X = df.drop(columns="species")
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Setup up modeling pipeline and fit with grid search
print("Defining Pipeline...")
preprocessing = ColumnTransformer(
    [
        ("OneHotEncoder", OneHotEncoder(drop=drop_cats), cat_cols),
        ("Scale", StandardScaler(), num_cols),
    ],
    remainder="passthrough",
)

pipeline = Pipeline(
    [
        ("Preprocessing", preprocessing),
        ("Model", RandomForestClassifier()),
    ]
)

print("Performing GridSearchCV...")
grid = {
    "Model__n_estimators": [100, 150],
    "Model__max_depth": [3, 4, 5],
}

pipeline_cv = GridSearchCV(pipeline, grid)
pipeline_cv.fit(X_train, y_train)

print("\nModel Evaluation:")
print(f"\tTrain score: {pipeline_cv.score(X_train, y_train):.4f}")
print(f"\tTest score: {pipeline_cv.score(X_test, y_test):.4f}")
print(f"\tBest params: {pipeline_cv.best_params_}")


# Extract best estimator from GridSearchCV object
# and save as a pickled file.
print(f"\nSaving model to '{MODEL_OUTPUT_PATH}'...")
best_model = pipeline_cv.best_estimator_
with open(MODEL_OUTPUT_PATH, "wb") as f:
    pickle.dump(best_model, f)
