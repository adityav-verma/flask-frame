run_migrations () {
    echo 'Running migrations'
    flask db upgrade
}

run_migrations
