FROM python:3.7

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5002

ENTRYPOINT ["gunicorn"  , "-b", "0.0.0.0:5002", "application:app"]