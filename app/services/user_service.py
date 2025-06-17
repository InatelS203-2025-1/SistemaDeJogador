from app.builders.user_builder import UserBuilder
from app.models.user import User
from app import db
from app.services.rabbitmq.publisher import publish_player_created

class UserService:

    @staticmethod
    def create_user(data: dict):
        email = data.get("email")
        if not all([data.get("name"), email, data.get("password"), data.get("dateofbirth")]):
            return None, {"msg": "Todos os campos são obrigatórios"}, 400
        if User.query.filter_by(email=email).first():
            return None, {"msg": "Email já registrado"}, 409

        new_user = (UserBuilder()
                    .with_name(data.get("name"))
                    .with_email(data.get("email"))
                    .with_password(data.get("password"))
                    .with_dateofbirth(data.get("dateofbirth"))
                    .as_admin(data.get("is_adm", False))
                    .build())

        db.session.add(new_user)
        db.session.commit()

        publish_player_created({
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "dateofbirth": str(new_user.dateofbirth),
            "is_adm": new_user.is_adm
        })

        return new_user, None, 201

    @staticmethod
    def update_user(user_to_update: User, data: dict):
        updated_user = (UserBuilder(user_to_update)
                        .with_name(data.get("name"))
                        .with_email(data.get("email"))
                        .with_dateofbirth(data.get("dateofbirth"))
                        .build())

        db.session.commit()

        user_data = {
            "id": updated_user.id, "name": updated_user.name, "email": updated_user.email,
            "dateofbirth": str(updated_user.dateofbirth), "is_adm": updated_user.is_adm
        }

        return updated_user, {"msg": "Seus dados foram atualizados", "user": user_data}, 200

    @staticmethod
    def login_validation(email, password):
        if not email or not password:
            return None, {"msg": "Email e senha são obrigatórios"}, 400

        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            return None, {"msg": "Credenciais inválidas"}, 401

        return user, None, None




