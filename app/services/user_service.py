from app.models.user import User
from app import db
from app.services.rabbitmq.publisher import publish_player_created


def registration_validation(name, email, password, dateofbirth, is_adm):
    if not name or not email or not password or not dateofbirth or not is_adm:
        return {"msg": "Todos os campos são obrigatórios"}, 400


    if User.query.filter_by(email=email).first():
        return {"msg": "Email já registrado"}, 409

    return None, None


def create_user(name, email, password, dateofbirth, is_adm):
    new_user = User(name=name, email=email, dateofbirth=dateofbirth, is_adm=is_adm)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    publish_player_created({
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email,
        "dateofbirth": str(new_user.dateofbirth),
        "is_adm": new_user.is_adm
    })

    return new_user


def login_validation(email, password):
    if not email or not password:
        return None, {"msg": "Email e senha são obrigatórios"}, 400

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return None, {"msg": "Credenciais inválidas"}, 401

    return user, None, None




