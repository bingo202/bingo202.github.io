from db import db

class comment(db.Model):
    __tablename__='comment'
    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    sp_url = db.Column(db.String(255),nullable=True)
    user_name = db.Column(db.String(255),nullable=True)
    user_start = db.Column(db.String(255),nullable=True)
    conent = db.Column(db.String(255),nullable=True)
    buy_info = db.Column(db.String(255),nullable=True)
    type_sp = db.Column(db.String(255),nullable=True)
