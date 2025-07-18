import os
import uuid
from flask import Flask, request, jsonify
from data_manager import data_manager

USERS_FILE = os.path.join(os.path.dirname(__file__), 'data', 'users.json')

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password required'}), 400

    users = data_manager.read_data(USERS_FILE)
    # Prüfe, ob der Benutzername schon existiert
    if any(user.get('username') == data['username'] for user in users):
        return jsonify({'error': 'User already exists'}), 409

    user_id = str(uuid.uuid4())
    new_user = {
        'id': user_id,
        'username': data['username'],
        'password': data['password']  # In echten Anwendungen: Passwort hashen!
    }
    users.append(new_user)
    data_manager.write_data(USERS_FILE, users)

    return jsonify({'message': 'User registered successfully', 'id': user_id}), 201

if __name__ == "__main__":
    app.run(port=5001, debug=True)