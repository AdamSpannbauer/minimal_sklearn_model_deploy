# minimal_sklearn_model_deploy 🤖🧠☁️

Who is this for

* 🙋 You know how to build and save `sklearn` models
* 🙋‍♀️ You have a [Heroku](https://www.heroku.com/) account (or you 1 minute spare time to create one)
* 🙋‍♂️ You want to know how to deploy an sklearn model as a REST API and you're more of a doer than a reader

README Outline:
* 📝 [Process overview](#process-overview): Step-by-step instructions for creating and deploying an sklearn model to Heroku.
* 📄 [Files/descriptions](#filesdescriptions): All files used in the project laid out with descriptions of how they contribute to the model build and deploy.
  * 🐍 [Python files](#python-files): Files for building the model, serving the model, and requesting a prediction from the deployed model.
  * 🌐 [Other important files](#other-important-files): 2 files needed for deploying to Heroku.
  * 💾 [Data files](#data-files): A csv for building the example model and the saved model itself.

## Process overview

(Assumes that you'll be working in a git repo and that you have a basic knowledge of git)

1. Build and save a model to be deployed using [`sklearn`](https://scikit-learn.org/) and [`pickle`](https://docs.python.org/3/library/pickle.html) (see [`model_build.py`](model_build.py)).
2. Create a [`flask`](https://flask.palletsprojects.com/en/1.1.x/) API endpoint for users to request predictions from your model saved on a server (see [`server.py`](server.py)).
3. Deploy the model to [Heroku](https://www.heroku.com/)
   1. Create a [Heroku](https://www.heroku.com/) account if you haven't already
   2. Create a [`Procfile`](Procfile) that specifies how Heroku should run your project
      * We specify to run `server:app` - The `server` represents the file name to run (`server.py`) & the `app` corresponds to how we named the flask app object in `server.py` (`app = Flask(__name__)`)
   3. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) and run `heroku login` from the command line
   4. Run [`heroku create`](https://devcenter.heroku.com/articles/creating-apps#creating-an-app-without-a-name) from the command line to do the initial heroku app setup (running the command like this will create a random inital app name like `battery-horse-staple`).  Note that this will add remote branches to your repo; run `git remote -v` to confirm.
   5. Run `git push heroku master` (or `git push heroku main` depending on name of your repos main branch) to deploy the application to Heroku.  This will take a minute as it installs all of the requirements found in the project's [`requirements.txt`](requirements.txt) (or other python requirements file type like `Pipfile` from [`pipenv`](https://pipenv.pypa.io/en/latest/)).
   6. Locate the URL to your app from the output of running `git push heroku master` (i.e. you'll see a line like `http://frozen-island-12625.herokuapp.com/ deployed to Heroku`).
   7. Request a prediction from your deployed model (see [`request_prediction.py`](request_prediction.py)).  The URL for the request will be a combination of the URL found in step 6 and the name of the route specified in [`server.py`](server.py).  For example, the URL shown in [`request_prediction.py`](request_prediction.py) has the base URL `http://frozen-island-12625.herokuapp.com` and the route `predict` so the resulting URL is `http://frozen-island-12625.herokuapp.com/predict`.

## Files/Descriptions

Each file is heavily commented to give further insight into the contents.

### Python files

These are in order of how they should be viewed/how they should be created if redoing this process.  The model needs to be built by `model_build.py` before serving the model with `sever.py`, and the server needs to be live before requesting a prediction with `request_prediction.py`.

#### [`model_build.py`](model_build.py)

A script to build the model to be deployed.  The model is built using the following from [`sklearn`](https://scikit-learn.org/): [`ColumnTransformer()`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html), [`Pipeline()`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html), and [`GridSearchCV()`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html).  The model used is a [`RandomForestClassifier()`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).  The final model is then saved to a file using [`pickle`](https://docs.python.org/3/library/pickle.html).

#### [`server.py`](server.py)

A script to server the model once on heroku (or locally).  Contents include: loading the pickled model file and creating a [`flask`](https://flask.palletsprojects.com/en/1.1.x/) app with an API endpoint to make predictions with the loaded model.

#### [`request_prediction.py`](request_prediction.py)

A script to request a prediction from the deployed REST API model using the [`requests`](https://requests.readthedocs.io/en/master/) package.

### Other important files

#### [`Procfile`](Procfile)

How [Heroku](https://www.heroku.com/) will know how to serve your model.  In this file you specify what app to run and what file that app can be found in.  We use the [`gunicorn`](https://gunicorn.org/) package to run our app.  For a more complete discussion on the `Procfile` see [Heroku's documentation](https://devcenter.heroku.com/articles/procfile).

#### [`requirements.txt`](requirements.txt)

Lists out the requirements for your project (package names and versions).  [This is a good resource](https://note.nkmk.me/en/python-pip-install-requirements/) for more.

Note, your project doesn't need to be a deployed model for this file to be useful.  Whenever starting a new project, I like to have this item on my getting started TODO list.

### Data files

#### [`saved_model.pkl`](saved_model.pkl)

Pickled model file created by [`model_build.py`](model_build.py).  See [`pickle`'s documentation](https://docs.python.org/3/library/pickle.html#examples) for more.

#### [`data/penguins.csv`](data/penguins.csv)

The example data used to build a predictive model to predict a penguin's species.  The data is [source](https://github.com/mwaskom/seaborn-data/blob/master/penguins.csv)d from the [`seaborn`](https://seaborn.pydata.org/index.html) package.

