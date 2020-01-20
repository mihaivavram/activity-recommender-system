# Activity Recommendation System

A Machine Learning recommendation system framework that recommends new
activities for users based on a previous activity and user review feed of how
those users who engaged in those activities rated those activities.

So far, this framework can:

1. Generate a dummy user to activity to review dataset.
1. Generate new activity recommendations.

## Configuration (should only be done once)

Note that if you ever get a message that states that
`python` or `pip` is undefined, simply try `python3` or `pip3` instead.

#### For Development and Runtime
1. Clone this repo to your local machine
1. Install [Python 3](https://www.python.org/downloads/) which comes with `pip`.
1. Install [pipenv](https://pypi.org/project/pipenv/).
1. Run `pipenv shell` to create a new Python virtual environment for this
project.
1. Run `pipenv install` to install all needed dependencies for this project.

#### For Linting
1. Install `pycodestyle` with `pip install pycodestyle`.
1. Install `autopep8` with `pip install --upgrade autopep8`.

## Running the code
1. Run `pipenv shell` if you have not done so already.
1. Run `python data-generator.py` to generate a file called
`generated_activity_reviews.csv` under the `/data` folder which includes a
user and activity based information such as which user completed which
activity and the user review such activity. The columns for this
file are `user_id, activity_id, review`.
1. Run `python activity-recommendation.py --actid <id>` to generate
recommendations based on an activity id you provide,
e.g. `python activity-recommendation.py --actid 3`. For more
usage options, check out `python activity-recommendation.py --help`.

## Linting the code
1. Run `pycodestyle <filename>` to find problems with that particular file
and manually fix them if needed.
1. Run `autopep8 --in-place --aggressive <filename>` where the `--aggressive`
flag can be repeated multiple times to add the level of the aggressiveness in
changing the code (a general rule of thumb is the more complex the code is,
then the higher chances an aggressive change will break the code, so best
to do these things manually).
