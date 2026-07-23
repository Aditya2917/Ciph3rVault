from app.extensions import db
from app.models.user import User


def create_user(username, email, password):

    username = username.strip()
    email = email.strip().lower()

    if User.query.filter_by(username=username).first():
        return False, "Username already exists."

    if User.query.filter_by(email=email).first():
        return False, "Email already exists."

    user = User(
        username=username,
        email=email
    )

    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return True, "Registration Successful."


def authenticate_user(email, password):

    email = email.strip().lower()

    user = User.query.filter_by(email=email).first()

    if not user:
        return None

    if not user.check_password(password):
        return None

    return user