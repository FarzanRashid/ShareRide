FROM python:3.10-alpine

RUN mkdir -p /ShareRide

COPY . /ShareRide

WORKDIR /ShareRide

RUN pip install -r requirements.txt

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
