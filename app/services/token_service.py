import jwt
import datetime
from flask import current_app


def generate_token(user_id, is_adm):
    payload = {
        "user_id": user_id,
        "is_adm": is_adm,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm=current_app.config['JWT_ALGORITHM'])
    return token


def token_validation(auth_header, secret_key, jwt_algorithm):
    try:
        token = auth_header.split(" ")[1]
        decoded = jwt.decode(token, secret_key, algorithms=[jwt_algorithm])

        user_id = decoded["user_id"]
        is_adm = decoded.get("is_adm", False)  # Pega False se não tiver

        return user_id, is_adm, None, None

    except (IndexError, jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None, None, {"msg": "Token inválido ou expirado"}, 401


