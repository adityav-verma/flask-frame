# flask-app
A production ready flask setup using `Docker`, `Nginx` and `uWSGI`.

## Requirements:

Docker: For creating containers. For info about installing docker visit [Docker docs](https://docs.docker.com)

## Steps
- Clone the repo
- Copy `docker-compose.yml.sample` to `docker-compose.yml`
- Copy `app/configs.py.sample` to `app/configs.py.` and add the necessary configurations
- Run `docker-compose up --build`

That's it. The flask app should be up and running.
