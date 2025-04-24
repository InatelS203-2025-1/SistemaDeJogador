from flask import Blueprint, jsonify
from app.controllers.user_controller import UserController

admin_bp = Blueprint('admin_bp', __name__)


class AdministratorController(UserController):

    @staticmethod
    def create():
        # Lógica Aqui
        return jsonify({"msg": "Player created!"}), 200

    @staticmethod
    def list():
        # Lógica Aqui
        return jsonify({"msg": "All players"}), 200

    @staticmethod
    def update(player_id):
        # Lógica Aqui
        return jsonify({"msg": f"Player {player_id} updated!"}), 200

    @staticmethod
    def delete(player_id):
        # Lógica Aqui
        return jsonify({"msg": f"Player {player_id} deleted!"}), 200


# Herdados
admin_bp.add_url_rule('/register', view_func=AdministratorController.register, methods=['POST'])
admin_bp.add_url_rule('/login', view_func=AdministratorController.login, methods=['POST'])
admin_bp.add_url_rule('/delete', view_func=AdministratorController.delete_user, methods=['DELETE'])
admin_bp.add_url_rule('/edit', view_func=AdministratorController.edit_user, methods=['PUT'])
admin_bp.add_url_rule('/details', view_func=AdministratorController.details, methods=['GET'])


# Novos métodos
admin_bp.add_url_rule('/create_player', view_func=AdministratorController.create, methods=['POST'])
admin_bp.add_url_rule('/list_players', view_func=AdministratorController.list, methods=['GET'])
admin_bp.add_url_rule('/edit_player/<int:player_id>', view_func=AdministratorController.update, methods=['PUT'])
admin_bp.add_url_rule('/delete_player/<int:player_id>', view_func=AdministratorController.delete, methods=['DELETE'])
