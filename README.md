# # minimal_sklearn_model_deploy 🤖🧠☁️

## Files/Descriptions

### Python Scripts

#### [`model_build.py`](model_build.py)

A script to build the model to be deployed.  The model is built using the following from [`sklearn`](https://scikit-learn.org/): [`ColumnTransformer()`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html), [`Pipeline()`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html), and [`GridSearchCV()`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html).  The model used is a [`RandomForestClassifier()`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).  The final model is then saved to a file using [`pickle`](https://docs.python.org/3/library/pickle.html).

#### [`server.py`](server.py)

A script to server the model once on heroku (or locally).  Contents include: loading the pickled model file and creating a [`flask`](https://flask.palletsprojects.com/en/1.1.x/) app with an API endpoint to make predictions with the loaded model.

#### [`request_prediction.py`](request_prediction.py)

A script to request a prediction from the deployed REST API model using the [`requests`](https://requests.readthedocs.io/en/master/) package.

### Other Important Files

#### [`Procfile`](Procfile)

Heroku goodness (TODO: actually describe this)

#### [`requirements.txt`](requirements.txt)

Lists out the package requirements for your project (package names and versions).  [This is a good resource](https://note.nkmk.me/en/python-pip-install-requirements/) for more.  Note, your project doesn't need to be a package for this file to be useful.  Whenever starting a new project, I like to have this item of my getting started todo list.

### Data Files

#### [`data/penguins.csv`](data/penguins.csv)

The example data used to build a predictive model to predict a penguin's species.  The data is [sourced](https://github.com/mwaskom/seaborn-data/blob/master/penguins.csv) from the [`seaborn`](https://seaborn.pydata.org/index.html) package.

#### [`saved_model.pkl`](saved_model.pkl)

Pickled model file created by [`model_build.py`](model_build.py)