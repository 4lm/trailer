# TrailerPress

Django app for watching the latest trailers.

[This project is in early stages]

master branch: [![Build Status](https://travis-ci.com/4lm/trailerpress.svg?branch=master)](https://travis-ci.com/4lm/trailerpress) \
develop branch: [![Build Status](https://travis-ci.com/4lm/trailerpress.svg?branch=develop)](https://travis-ci.com/4lm/trailerpress)

## Installation

[This installation manual was tested with a GNU/Linux operating system (Ubuntu 18.04) and might be adjusted for usage with other operating systems]

- First you need Git, Python (>= 3.6) with Virtualenv and Pip installed. If you are under Linux/Mac this should be a no-brainer, if you use Windows and you don't have a Git, Python, Virtualenv and Pip workflow yet, please read this [tutorial](http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/) for Pip and Virtualenv installation/usage and visit this [link](https://git-scm.com/download/win) do download/install Git.
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
```
- Start the development server:
```
python manage.py runserver
```
