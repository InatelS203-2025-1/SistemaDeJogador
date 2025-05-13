import jwt
import datetime
from flask import current_app


def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm=current_app.config['JWT_ALGORITHM'])
    return token


def token_validation(auth_header, secret_key, jwt_algorithm):
    try:
        token = auth_header.split(" ")[1]
        decoded = jwt.decode(token, secret_key, algorithms=jwt_algorithm)
        user_id = decoded["user_id"]
        return user_id, None, None
    except (IndexError, jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None, {"msg": "Token inválido ou expirado"}, 401

