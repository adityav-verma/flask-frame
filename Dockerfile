FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY . /www/app

WORKDIR /www/app

ENV UWSGI_INI /www/app/uwsgi.ini

# Install dependencies
RUN pip install -r requirements.lock
