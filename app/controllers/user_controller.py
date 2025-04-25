from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db

users_bp = Blueprint('users_bp', __name__)


class UserController:

    @staticmethod
    def register():
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        dateofbirth = data.get("dateofbirth")

        # Fazer tratamentos

        new_user = User(name=name, email=email, password=password, dateofbirth=dateofbirth)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"msg": "Usuário registrado com sucesso", "user_id": new_user.id}), 201

    @staticmethod
    def login():
        # Lógica Aqui
        return jsonify({"msg": "Login realizado com sucesso"}), 200

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
        # Lógica Aqui
        return jsonify({"msg": "Detalhes do seu perfil"}), 200



users_bp.add_url_rule('/register', view_func=UserController.register, methods=['POST'])
users_bp.add_url_rule('/login', view_func=UserController.login, methods=['POST'])
users_bp.add_url_rule('/delete', view_func=UserController.delete_account, methods=['DELETE'])
users_bp.add_url_rule('/edit', view_func=UserController.edit_account, methods=['PUT'])
users_bp.add_url_rule('/details', view_func=UserController.details_account, methods=['GET'])