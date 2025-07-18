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

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400
    
    if username in users:
        return jsonify({'error': 'User already exists'}), 409
    
    user_id = str(uuid.uuid4())
    users[username] = {
        'id': user_id,
        'password': password
    }
        
    data_manager.write_data(USERS_FILE, users)

    return jsonify({
        'message': 'User registered successfully',
        'id': user_id
    }), 201


if __name__ == "__main__":
    app.run(port=5001, debug=True)