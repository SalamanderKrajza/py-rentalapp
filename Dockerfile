FROM python:3

ADD ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
ADD ./app /app/
WORKDIR /app

EXPOSE 8000
# CMD python manage.py runserver 0.0.0.0:8000
# CMD gunicorn rental.wsgi:application --bind 0.0.0.0:8000