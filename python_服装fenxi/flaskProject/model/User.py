from db import db

class User(db.Model):
    __tablename__='User'
    user_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    user_name = db.Column(db.String(255),nullable=True,unique=True)
    user_password = db.Column(db.String(255),nullable=True)
    sex = db.Column(db.String(255), nullable=True)
    like_type = db.Column(db.String(255), nullable=True)
    tall = db.Column(db.Float(precision="10,2"), nullable=True)
    weight = db.Column(db.Float(precision="10,2"), nullable=True)
