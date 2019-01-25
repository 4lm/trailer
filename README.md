# TrailerPress

TrailerPress is a platform for watching the lastest trailers of playing and upcoming films in German cinemas. The user can browse a catalog of trailers (also by genre) and can create an user account for rating the trailers and creating a history of rated trailers in the users profile page. TrailerPress is a demo project and was created as a student semester project by Alexis Michaltsis at the _Technische Hochschule Brandenburg - University of Applied Sciences_ under the supervision of Prof. Dr. Thomas Preuss. TrailerPress uses the Django web framework and for automated trailer data fetching the API of _The Movie Database_ (the trailer data is in following steps processed and saved to the local Django DB). TrailerPress is optimized to run on desktop, tablet and mobile. 

A running demo instance of TrailerPress can be visited [here](https://trailerpress.michaltsis.net/).

Notice (for development):

- As of today, the UI of this app is in German language. 
- In order for this app to work locally, you need an API key from [The Movie Database](https://www.themoviedb.org/faq/api).

Branch master : [![Build Status](https://travis-ci.com/4lm/trailerpress.svg?branch=master)](https://travis-ci.com/4lm/trailerpress) \
Branch develop: [![Build Status](https://travis-ci.com/4lm/trailerpress.svg?branch=develop)](https://travis-ci.com/4lm/trailerpress)

## Use of Build-in Functionality

### View Classes

This project uses, wherever it makes sense, build-in view classes, e. g. for registration, login and password reset. In some cases, if no sub class of a view class is needed the view class is directly called in the corresponding urls.py.

### Email Backend

This project uses the Django email backend for its password reset system.

### Messaging

This project makes use of the Django messaging system.

### Tests

This project uses a small set of tests. You can run the tests by typing:

```
python manage.py test
```

## Use of Third-party Libraries

### Pip and Virtualenv

This project makes use if Pip and Virtualenv. All requirements for the virtual environment can be found in the requirements.txt.

### django-star-ratings

For rating, this project uses the django app named [django-star-ratings](https://github.com/wildfish/django-star-ratings). The app is not installed in the virtual environment, but instead can be found locally in the repo of this project (/star_ratings), because the app had a bug and missed a language feature it had to be used as a fork locally in this repository. Two pull request for [bug](https://github.com/wildfish/django-star-ratings/pull/154) and [language feature](https://github.com/wildfish/django-star-ratings/pull/155) have been filed in the original django-star-ratings GitHub repository. If they are going to be accepted, this project will switch from the use of the forked django-star-ratings app to the original app (via virtual environment) and remove it from the local code base of this project.
    
### django-bootstrap4 and django-icons

This project uses Bootstrap 4 and FontAwesome icons, which are integrated via template tags of the two Django apps [django-bootstrap4](https://pypi.org/project/django-bootstrap4/) and [django-icons](https://pypi.org/project/django-icons/). 

### django-crispy-forms

For having crispy forms, this project uses [django-crispy-forms](https://pypi.org/project/django-crispy-forms/).

### python-decouple

For having a workflow for environment variables (e.g. password, secret key etc.), which works uniform on Windows, Linux and Mac, this project uses [python-decouple](https://pypi.org/project/python-decouple/). All environment variables are written to a .env file, which is NOT committed. More, on how to create a custom .env file, see section _Installation of Development Environment_ below.

### Reporting

This project uses [coverage](https://pypi.org/project/coverage/) for reporting. You can create a report by running:

```
coverage run manage.py test
coverage report -m
```

### jQuery, jQuery Add-on and video.js

This project uses jQuery, an jQuery add-on and the third-party video.js video-player library (in trailerapp/static/trailerapp/js/), which are also called by two custom JavaScript (JS) helper functions (in trailerapp/static/trailerapp/js/helpers.js). The two custom JS helper functions make, that only one video at the same time is played and that if one video is running and a second video is turned on the first video stops playing.

### Travis CI

This project uses [Travis CI](https://travis-ci.com/) for continuous integration. The config file is in the root folder of this project named .travis.yml.

## Use of Custom Shell Scripts

### setup.sh

This script is used to install a git clone of the django-star-ratings app to the repository of this project. 

### build.sh

This script installs all the needed JS libraries from local node modules, which have to be first installed via (Node and NPM have to be installed on the system):
```
npm install
```
Also in this script, the star_ratings folder in the local git clone of the django-star-ratings app is copied to the root of this project. 

### report.sh

This script runs the test set and creates a coverage report.

## Initial Data

If this project is setup locally, this project needs some initial data for the local database, which is solved with a [fixture](https://code.djangoproject.com/wiki/Fixtures) and can be found as JSON file in trailerapp/fixtures/initial_data.json.

## Installation of Development Environment

[This installation manual was tested with a GNU/Linux operating system (Ubuntu 18.04) and might be adjusted for usage with other operating systems]

- First you need Git, Python (>= 3.6) with Virtualenv and Pip installed. If you are under Linux/Mac this should be a no-brainer, if you use Windows and you don't have a Git, Python, Virtualenv and Pip workflow yet, please read this [tutorial](http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/) for Pip and Virtualenv installation/usage and visit this [link](https://git-scm.com/download/win) to download/install Git.
- If not already downloaded/installed, download/install Git, Python (>= 3.6), Pip (normally comes with Python) and Virtualenv
- Open the console (aka terminal, shell) on your computer
- Create a project directory in your terminal
- CD into your project directory (/path/to/project/)
- Download this Django project:
```
git clone https://github.com/4lm/trailerpress.git
```
- CD into the downloaded git project folder (/path/to/project/trailerpress/):
```
cd trailerpress
```
- Create a virtual environment with Virtualenv:
```
virtualenv venv --python=python3.6
```
- Activate the virtual environment:
```
source venv/bin/activate
```
- Install project requirements via pip:
```
pip install -r requirements.txt
```
- Migrate project:
```
python manage.py migrate
python manage.py loaddata initial_data.json
```
- Create a file named .env (Python decouple lib) and put it in the application root directory and fill in following constants:  
```
API_KEY=[https://www.themoviedb.org/faq/api]
LANGUAGE=de
PAGE=1
REGION=DE
EMAIL_USER=[Your email address for the email system of the app]
EMAIL_PASS=[Your email address password ]
SECRET_KEY=[Choose a secure secret key]
DEBUG=True [only for testing, choose False in production]
```
- Create an admin account:
```
python manage.py createsuperuser
```
- Start the development server:
```
python manage.py runserver
```
- Go to 127.0.0.1:8000 and log in as admin, then go to 127.0.0.1:8000/get-films and populate db with films.
