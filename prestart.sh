fetch_config_from_s3 () {
  echo "Fetch the config from S3"
  curl -sS --fail -o app/configs.py https://s3.ap-south-1.amazonaws.com/flask-frame/configs.py
}

run_migrations () {
    echo 'Running migrations'
    flask db upgrade
}

fetch_config_from_s3

run_migrations
