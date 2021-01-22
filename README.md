# Deploying a model with `sklearn` & `flask` to `heroku`.  A minimal example.

## Files

### Python Scripts

* [`model_build.py`](model_build.py) - A script to build the model to be deployed.  The model is built using the following from `sklearn`: `ColumnTransformer()`, `Pipeline()`, and `GridSearchCV()`.  The model used is a `RandomForestClassifier()`.  The final model is then saved to a file using `pickle`.
* [`server.py`](server.py) - A script to server the model once on heroku (or locally).  Contents include: loading the pickled model file and creating a `flask` app with an API endpoint to make predictions with the loaded model.
* [`request_prediction.py`](request_prediction.py) - A script to request a prediction from the deployed REST API model.

### Data Files

* [`data/penguins.csv`](data/penguins.csv) -  The example data used to build a predictive model to predict a penguin's species.  The data is sourced from the `seaborn` package.
* [`saved_model.pkl`](saved_model.pkl) - Pickled model file created by [`model_build.py`](model_build.py) 

### Other Important Files

* [`Procfile`](Procfile) - heroku goodness (TODO: actually describe this)
* [`requirements.txt`](requirements.txt) - TODO: actually describe this

## TODO:

* Add more comments to code (like really over comment)
* Put in more description and links in README.md
* Add exercises? need to come up with some acheivable ones (deploy on your own ofc, but what else?)