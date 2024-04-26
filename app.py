# This is a simple flask app that displays "Hello World"

from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "<h2>Hello world - Docker Flask Deployment Lab<h2><hr/>"\


p=5000
while True:
    try:
        app.run(host="0.0.0.0", port=p)
        break
    except OSError:
        if p > 5999:
            break
        p+=1

