from . import db


class User(db.Model):
    __tablename__ = 't_user'
    uuid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.INTEGER)
