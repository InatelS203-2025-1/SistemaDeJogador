from flask import request, jsonify, current_app
from functools import wraps
from app.services.token_service import token_validation

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"msg": "Token de autenticação não fornecido"}), 401

        user_id, is_adm, error_msg, status_code = token_validation(
            auth_header,
            current_app.config['SECRET_KEY'],
            current_app.config['JWT_ALGORITHM']
        )

        if error_msg:
            return jsonify(error_msg), status_code

        if not is_adm:
            return jsonify({"msg": "Acesso restrito a administradores"}), 403

        # Passa user_id e is_adm como kwargs se quiser usar no handler
        return fn(*args, **kwargs)

    return wrapper
