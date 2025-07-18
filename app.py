import os
import uuid
from flask import Flask, request, jsonify
from data_manager import data_manager

USERS_FILE = os.path.join(os.path.dirname(__file__), 'data', 'users.json')
users = data_manager.read_data(USERS_FILE)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from User Auth Service'


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({'error': 'Username, password and email required'}), 400

    if email in users:
       return jsonify({'error': 'Email already exists'}), 409
    
    if username in users:
        return jsonify({'error': 'User already exists'}), 409
    
    users[username] = {'password': password}
    data_manager.write_data(USERS_FILE, users)

    return jsonify({'message': 'User registered successfully'}), 201

new_user_id = str(uuid.uuid4())


if __name__ == "__main__":
    app.run(port=5001, debug=True)