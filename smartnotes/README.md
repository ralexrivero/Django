# Smartnotes

## Development

### container

build docker image from python:apline and django
Run container with mounted volume from host

- `docker build -t py-dj .`
- `docker run -d -it --rm --name py-dj-0 -v /home/ralex/code/Django/smartnotes:/code -p 8000:8000 py-dj`
- `docker exec -it py-dj-0 sh`

### django project

- `django-admin startproject smartnotes .`
- `sudo chown -R $USER:$USER *`
- edit settings.py

```python
ALLOWED_HOSTS = ['*']
```

- `python manage.py migrate`
- `python manage.py runserver`

### docker compose

- `docker compose build`
- `docker compose up`
- `python -m venv env`
- `source env/bin/activate`
- `pip freeze > requirements.txt`
