from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db
import jwt
import datetime
from flask import current_app
users_bp = Blueprint('users_bp', __name__)


class UserController:

    @staticmethod
    @staticmethod
    def register():
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        dateofbirth = data.get("dateofbirth")

        if not name or not email or not password or not dateofbirth:
            return jsonify({"msg": "Todos os campos são obrigatórios"}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({"msg": "Email já registrado"}), 409

        new_user = User(name=name, email=email, dateofbirth=dateofbirth)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"msg": "Usuário registrado com sucesso", "user_id": new_user.id}), 201


    @staticmethod
    def login():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"msg": "Email e senha são obrigatórios"}), 400

        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            return jsonify({"msg": "Credenciais inválidas"}), 401

        token = jwt.encode(
            {
                "user_id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            },
            current_app.config['SECRET_KEY'],
            algorithm="HS256"
        )

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
        # Lógica Aqui
        return jsonify({"msg": "Detalhes do seu perfil"}), 200



users_bp.add_url_rule('/register', view_func=UserController.register, methods=['POST'])
users_bp.add_url_rule('/login', view_func=UserController.login, methods=['POST'])
users_bp.add_url_rule('/delete', view_func=UserController.delete_account, methods=['DELETE'])
users_bp.add_url_rule('/edit', view_func=UserController.edit_account, methods=['PUT'])
users_bp.add_url_rule('/details', view_func=UserController.details_account, methods=['GET'])