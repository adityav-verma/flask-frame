FROM python:3.6-slim

WORKDIR /www/app

ADD . /www/app

RUN pip install -r requirements.txt

ENV APP_ENV production

EXPOSE 80

CMD ["python", "app.py"]
