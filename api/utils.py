from flask import  request, jsonify
import jwt
from functools import  wraps
from flask import request
from app import app


# Tokeninzing the endpoints using Secret key and name of the user
def token_required(f):
    import models
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        # Using HS256 Decoding algorithm the toekn will be decoded extracting the user info based on name and Secret key
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            # Based on Secret key and name the token will be generated
            current_user = models.User.query.filter_by(name=data['name']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)
    return decorator
