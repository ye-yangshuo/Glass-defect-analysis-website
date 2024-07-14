from flask import Blueprint, request, jsonify
from app.services.authentic_service import authenticate

bp = Blueprint('authentic', __name__, url_prefix='/api')

@bp.route('/authentic', methods=['POST'])
def handle_authentication():
    auth = request.get_json()
    if not auth or 'username' not in auth or 'password' not in auth:
        return jsonify({'message': 'Invalid request. Please provide username and password.'}), 400
    
    username = auth['username']
    password = auth['password']
    print(username)
    print(password)
    user_id, error = authenticate(username, password)

    if user_id:
        return jsonify({'message': 'Authentication successful', 'user_id': user_id}), 200
    else:
        return jsonify({'message': error}), 401