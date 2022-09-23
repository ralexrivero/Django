# Django

## Environment

[![Ubuntu](https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A)](https://ubuntu.com/)<!-- ubuntu -->
[![Bash](https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A)](https://www.gnu.org/software/bash/)<!-- bash -->
[![Vim](https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A)](https://www.vim.org/)<!-- vim -->
[![VS Code](https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=007ACC&logo=Visual%20Studio%20Code&logoColor=007ACC&labelColor=2F333A)](https://code.visualstudio.com/)<!-- vs code -->
[![Pycharm](https://img.shields.io/static/v1?label=&message=Pycharm&color=000000&logo=pycharm&logoColor=000000&labelColor=f3f3f3)](https://www.jetbrains.com/pycharm/)<!-- pycharm -->
[![Git](https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A)](https://git-scm.com/)<!-- git -->
[![Github](https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A)](https://github.com)<!-- github -->
[![Docker](https://img.shields.io/static/v1?label=&message=Docker&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com)<!-- docker -->
[![Django](https://img.shields.io/static/v1?label=&message=Django&color=092E20&logo=Django&logoColor=092E20&labelColor=F5F5F5)](https://www.djangoproject.com/)<!-- Django -->

- `pip`
- `pycodestyle`

## Introduction

Django is a MTV Model Template View derived from MVC - Model View Controller.

### MVC

- Controller: as the name suggests, it controls the flow of the application. It is the part of the application that receives the user input and decides what to do with it. It is also responsible for the interaction with the model and the view. Executes all the business logic and decides what to do with the data. Controller communicates with the model
- Model: It is the part of the application that deals with the data. It is responsible for the data management and the data storage. It is the part of the application that interacts with the database. It is the part of the application that is responsible for the data management and the data storage. It is the part of the application that interacts with the database. Its conected to the database through the ORM
- View: It is the part of the application that deals with the user interface. It is responsible for the presentation of the data. It is the part of the application that interacts with the user. It is the part of the application that deals with the user interface. It is responsible for the presentation of the data. It is the part of the application that interacts with the user. The view makes the front end of the application.

- view: logic
- template: visual
- model: data

### MTV

In this model controller are called views and views are called templates.
Its a naming convention.

## Installation

- `python -m pip install Django`

## Usage

- `python -m django --version`
- `django-admin startproject helloworld`

## initial setup

- `python manage.py migrate` generates the database
- `python manage.py runserver` run development server
- `sudo chown -R ralex:ralex *` change owner of the project created with root privileges in docker container

## templates

- add `templates` folder in the project folder
- add 'DIRS': ['templates'], to the TEMPLATES section in settings.py
- create html file in the `templates` folder

### `for` and `if`

- `{{ }}` for variables
- `{% %}` for logic

### template comments

- `{# #}` one line, not rendered in the html
- `{% comment %} {% endcomment %}` multi line, not renered in the html
- <!-- comment --> html comment, rendered in the html

### filters

- `{{ variable | filter }}`
- `{{ variable | filter:argument }}`

- `length` returns the length of the list
- `lower` converts the string to lowercase
- `upper` converts the string to uppercase
- `title` converts the string to titlecase
- `cut` removes all values of arg from the given string
- `default` provides a default value if the variable is not defined
- `date` formats a date according to the given format
- `time` formats a time according to the given format
- `first` returns the first item of a list
- `last` returns the last item of a list
- `join` joins the list with the given string

## Static files

- `STATIC_URL = 'static/'`
- `INSTALLED_APPS = [ 'django.contrib.staticfiles', ]`
- add `static` folder in the project folder
- add environment variable:

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    '/var/www/static'
]
```

- {% load static %} in the template
- {% static 'path/to/file' %} in the template

## Template inheritance

- {% block content %} {% endblock %} in the template
- {% extends 'base.html' %} in the template

## urls and inclusion

- `{% url 'name' %}` in the template for a url with a name

- `{% include 'path/to/file.html' %}` in the template for including a template

## modularization

- `python manage.py startapp app_name` in the project folder
- add `app_name` to the `INSTALLED_APPS` in settings.py
- `python manage.py check app_name` to check for errors

## models

- `from django.db import models` in models.py in the app folder

- each model is a class
- add the model in `models.py`

```python
class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
```

- `python manage.py makemigrations` to create migrations
- `python manage.py migrate` to apply migrations

## Author
<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+27K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)