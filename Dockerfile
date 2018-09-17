FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY . /app

WORKDIR /app

ENV UWSGI_INI /app/uwsgi.ini

# Install dependencies
RUN pip install -r requirements.lock
