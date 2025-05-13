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
