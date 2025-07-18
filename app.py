import os
from flask import Flask
from data_manager import data_manager

USERS_FILE = os.path.join(os.path.dirname(__file__), 'data', 'users.json')
users = data_manager.read_data(USERS_FILE)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from User Auth Service'

if __name__ == "__main__":
    app.run(port=5001, debug=True)