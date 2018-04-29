from app.app import create_app

app = create_app()


if __name__ == '__main__':
    """
    Only to be used for Development
    """
    app.run(host='0.0.0.0', port=8001, threaded=True)
