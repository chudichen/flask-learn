from flask_sqlalchemy import SQLAlchemy
from werkzeug import security

db = SQLAlchemy()


class User(db.Model):
    __table_name__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwd_hash = db.Column(db.String(54))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwd_hash = security.generate_password_hash(password)

    def check_password(self, password):
        return security.check_password_hash(self.pwd_hash, password)
