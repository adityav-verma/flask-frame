FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./app /app

# Install dependencies
RUN pip install -r requirements.txt
