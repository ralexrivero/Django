# Smartnotes

## Development

### container

build docker image from python:apline and django
Run container with mounted volume from host

- `docker build -t py-dj:1.0 .`
- `docker run -d -it --rm --name py-dj-0 -v /home/ralex/code/Django/smartnotes:/code -p 8000:8000 py-dj:1.0`
- `docker exec -it py-dj-0 sh`

### django project

- `django-admin startproject smartnotes .`
- `sudo chown -R $USER:$USER *`
- edit `settings.py`

```python
ALLOWED_HOSTS = ['*']
```

- `python manage.py migrate`
- `python manage.py runserver 0.0.0.0:8000`
- `curl -I localhost:8000`

### organize project

- `django-admin startapp home` to create app home
- add to `settings.py`

```python
INSTALLED_APPS = [
    'home',
]
```

## django admin

- `python manage.py createsuperuser`, create super user like admin with email and password
- visit the admin page `localhost:8000/admin`

## models

- `python manage.py makemigrations` after created models, to create the instructions
- `python manage.py migrate` to apply migrations

## static files

- add to `settings.py`

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

## extends base html

= add to `settings.py`

```python
TEMPLATES = [
    {
        'DIRS': [
            BASE_DIR / 'static/templates'
```

### Deploy to DigitalOcean

- `ssh-keygen -t rsa -b 4096`
- then, do the related staff with ssh and keys
- `ssh root@ip -i ~/.ssh/id_rsa`

### docker compose

- `docker compose build`
- `docker compose up`
- `python -m venv env`
- `source env/bin/activate`
- `pip freeze > requirements.txt`
