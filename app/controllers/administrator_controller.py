from flask import Blueprint, jsonify
from app.controllers.user_controller import UserController

admin_bp = Blueprint('admin_bp', __name__)


class AdministratorController(UserController):

    @staticmethod
    def create_user():
        # Lógica Aqui
        return jsonify({"msg": "Player created!"}), 200

    @staticmethod
    def get_all_users():
        # Lógica Aqui
        return jsonify({"msg": "All players"}), 200

    @staticmethod
    def edit_user(user_id):
        # Lógica Aqui
        return jsonify({"msg": f"Player {user_id} updated!"}), 200

    @staticmethod
    def delete_user(user_id):
        # Lógica Aqui
        return jsonify({"msg": f"Player {user_id} deleted!"}), 200


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
