from flask import Blueprint, request, jsonify
from app.controllers.user_controller import UserController
from app.models.user import User
from app.extensions import db
from app.utils.decorators import admin_required  # ajuste o path conforme seu projeto

admin_bp = Blueprint('admin_bp', __name__)


class AdministratorController(UserController):

    @staticmethod
    @admin_required
    def create_user():
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        dateofbirth = data.get("dateofbirth")
        is_adm = data.get("is_adm", False)

        if not name or not email or not password or not dateofbirth:
            return jsonify({"msg": "Todos os campos são obrigatórios"}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({"msg": "Email já registrado"}), 409

        new_user = User(
            name=name,
            email=email,
            dateofbirth=dateofbirth,
            is_adm=is_adm
        )
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"msg": "Usuário criado com sucesso", "user_id": new_user.id}), 201

    @staticmethod
    @admin_required
    def get_all_users():
        users = User.query.all()
        result = []
        for user in users:
            result.append({
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "dateofbirth": str(user.dateofbirth),
                "is_adm": user.is_adm
            })
        return jsonify({"users": result}), 200

    @staticmethod
    @admin_required
    def edit_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"msg": "Usuário não encontrado"}), 404

        data = request.get_json()

        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        user.dateofbirth = data.get("dateofbirth", user.dateofbirth)
        user.is_adm = data.get("is_adm", user.is_adm)

        db.session.commit()

        return jsonify({"msg": f"Usuário {user_id} atualizado com sucesso"}), 200

    @staticmethod
    @admin_required
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"msg": "Usuário não encontrado"}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({"msg": f"Usuário {user_id} deletado com sucesso"}), 200



# Herdados
admin_bp.add_url_rule('/register', view_func=AdministratorController.register, methods=['POST'])
admin_bp.add_url_rule('/login', view_func=AdministratorController.login, methods=['POST'])
admin_bp.add_url_rule('/delete', view_func=AdministratorController.delete_account, methods=['DELETE'])
admin_bp.add_url_rule('/edit', view_func=AdministratorController.edit_account, methods=['PUT'])
admin_bp.add_url_rule('/details', view_func=AdministratorController.details_account, methods=['GET'])

# Novos métodos
admin_bp.add_url_rule('/create_user', view_func=AdministratorController.create_user, methods=['POST'])
admin_bp.add_url_rule('/get_all_users', view_func=AdministratorController.get_all_users, methods=['GET'])
admin_bp.add_url_rule('/edit_user/<int:user_id>', view_func=AdministratorController.edit_user, methods=['PUT'])
admin_bp.add_url_rule('/delete_player/<int:user_id>', view_func=AdministratorController.delete_user, methods=['DELETE'])
