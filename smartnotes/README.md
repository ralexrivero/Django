# Smartnotes

## Development

### container

build docker image from python:apline and django
Run container with mounted volume from host

- `docker build -t py-dj:1.0 .`
- `docker run -d -it --rm --name py-dj-0 -v /home/ralex/code/Django/smartnotes:/code -p 000:3000 py-dj`
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

### docker compose

- `docker compose build`
- `docker compose up`
- `python -m venv env`
- `source env/bin/activate`
- `pip freeze > requirements.txt`
