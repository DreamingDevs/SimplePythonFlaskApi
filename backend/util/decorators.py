from flask import request, jsonify
from functools import wraps

def token_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                return jsonify({'status': 'Not authorized'}), 401

            kwargs['isAuthenticated'] = True
        except Exception as e:
            return jsonify({'message': 'Token is invalid'}), 401
        return f(*args, **kwargs)

    return wrap