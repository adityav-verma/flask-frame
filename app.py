from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Yo world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
