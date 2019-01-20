# TrailerPress

Django app for watching the latest trailers.

Notice:

- As of today, the UI of this app is in German language. 
- In order for this app to work you need an api key from ["The Movie database"](https://www.themoviedb.org/faq/api).

Branch master: [![Build Status](https://travis-ci.com/4lm/trailerpress.svg?branch=master)](https://travis-ci.com/4lm/trailerpress) \
Branch develop: [![Build Status](https://travis-ci.com/4lm/trailerpress.svg?branch=develop)](https://travis-ci.com/4lm/trailerpress)

## Installation Dev Environment

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
