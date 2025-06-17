from app.models.user import User


class UserBuilder:
    def __init__(self, original_user: User = None):
        if original_user:
            self.user = original_user
        else:
            self.user = User()

    def with_name(self, name):
        if name: self.user.name = name
        return self

    def with_email(self, email):
        if email: self.user.email = email
        return self

    def with_password(self, password):
        if password: self.user.set_password(password)
        return self

    def with_dateofbirth(self, dob):
        if dob: self.user.dateofbirth = dob
        return self

    def as_admin(self, is_admin_flag=True):
        self.user.is_adm = is_admin_flag
        return self

    def build(self) -> User:
        return self.user