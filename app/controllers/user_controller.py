from flask import Blueprint, request, jsonify, current_app
from app.services.token_service import generate_token, token_validation
from app.services.user_service import login_validation, registration_validation, create_user
import jwt
from app.models.user import User


users_bp = Blueprint('users_bp', __name__)


class UserController:

    @staticmethod
    def register():
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        dateofbirth = data.get("dateofbirth")

        error_msg, status_code = registration_validation(name, email, password, dateofbirth)
        if error_msg:
            return jsonify(error_msg), status_code

        user = create_user(name, email, password, dateofbirth)

        return jsonify({
            "msg": "Usuário registrado com sucesso",
            "user_id": user.id
        }), 201

    @staticmethod
    def login():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user, error_msg, status_code = login_validation(email, password)
        if error_msg:
            return jsonify(error_msg), status_code

        token = generate_token(user.id)

        return jsonify({
            "msg": "Login realizado com sucesso",
            "token": token,
            "user_id": user.id
        }), 200



    @staticmethod
    def delete_account():
        # Lógica Aqui
        return jsonify({"msg": "Sua conta foi deletada"}), 200

    @staticmethod
    def edit_account():
        # Lógica Aqui
        return jsonify({"msg": "Seus dados foram atualizados"}), 200

    @staticmethod
    def details_account():
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"msg": "Token de autenticação não fornecido"}), 401

        user_id, error_msg, status_code = token_validation(auth_header, current_app.config['SECRET_KEY'], current_app.config['JWT_ALGORITHM'])

        if error_msg:
            return jsonify(error_msg), status_code
        
        user = User.query.get(user_id)

        if not user:
            return jsonify({"msg": "Usuário não encontrado"}), 404

        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "dateofbirth": str(user.dateofbirth)
        }

        return jsonify({"msg": "Detalhes do seu perfil", "user": user_data}), 200



users_bp.add_url_rule('/register', view_func=UserController.register, methods=['POST'])
users_bp.add_url_rule('/login', view_func=UserController.login, methods=['POST'])
users_bp.add_url_rule('/delete', view_func=UserController.delete_account, methods=['DELETE'])
users_bp.add_url_rule('/edit', view_func=UserController.edit_account, methods=['PUT'])
users_bp.add_url_rule('/details', view_func=UserController.details_account, methods=['GET'])
