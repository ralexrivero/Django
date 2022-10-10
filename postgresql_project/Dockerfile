FROM python:3.11.0rc2-alpine3.16
WORKDIR /app
COPY . .
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN python -m pip install Django
RUN pip install psycopg2
RUN pip install django-seed
CMD ["python", "manage.py", "runserver"]
