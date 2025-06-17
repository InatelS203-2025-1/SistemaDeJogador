from flask import Blueprint, request, jsonify, current_app
from app.services.token_service import TokenService
from app.services.user_service import UserService
from app.models.user import User
from app.extensions import db
from app.utils.decorators import login_required

users_bp = Blueprint('users_bp', __name__)


class UserController:


    @staticmethod
    def register():
        data = request.get_json()

        if "is_adm" in data:
            return jsonify({"msg": "Você não tem permissão para definir este campo."}), 403
        data['is_adm'] = False

        user, error_msg, status_code = UserService.create_user(data)

        if error_msg:
            return jsonify(error_msg), status_code

        return jsonify({"msg": "Usuário registrado com sucesso", "user_id": user.id}), 201

    @staticmethod
    def login():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user, error_msg, status_code = UserService.login_validation(email, password)
        if error_msg:
            return jsonify(error_msg), status_code

        token = TokenService.generate_token(user.id, user.is_adm)

        return jsonify({
            "msg": "Login realizado com sucesso",
            "token": token,
            "user_id": user.id
        }), 200

    @staticmethod
    @login_required
    def delete_account(current_user: User):
        db.session.delete(current_user)
        db.session.commit()

        return jsonify({"msg": "Sua conta foi deletada"}), 200

    @staticmethod
    @login_required
    def edit_account(current_user: User):
        data = request.get_json()
        updated_data, error_msg, status_code = UserService.update_user(current_user, data)

        if error_msg:
            return jsonify(error_msg), status_code

        return jsonify({"msg": "Seus dados foram atualizados", "user": updated_data}), 200

    @staticmethod
    @login_required
    def details_account(current_user: User):
        user_data = {
            "id": current_user.id,
            "name": current_user.name,
            "email": current_user.email,
            "dateofbirth": str(current_user.dateofbirth),
            "is_adm": current_user.is_adm
        }

        return jsonify({"msg": "Detalhes do seu perfil", "user": user_data}), 200


# Rotas
users_bp.add_url_rule('/register', view_func=UserController.register, methods=['POST'])
users_bp.add_url_rule('/login', view_func=UserController.login, methods=['POST'])
users_bp.add_url_rule('/delete', view_func=UserController.delete_account, methods=['DELETE'])
users_bp.add_url_rule('/edit', view_func=UserController.edit_account, methods=['PUT'])
users_bp.add_url_rule('/details', view_func=UserController.details_account, methods=['GET'])
