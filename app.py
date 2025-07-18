import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from User Auth Service'

if __name__ == "__main__":
    app.run(port=5001, debug=True)