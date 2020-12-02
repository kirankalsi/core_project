FROM python:3.7

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5003

ENTRYPOINT ["gunicorn"  , "-b", "0.0.0.0:5003", "application:app"]