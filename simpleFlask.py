from time import sleep
from flask import Flask

app = Flask(__name__)

RESPONSE_DELAY=1

@app.route("/")
def hello_world():
    sleep(RESPONSE_DELAY)
    return "Returning with {} second delay".format(RESPONSE_DELAY)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

