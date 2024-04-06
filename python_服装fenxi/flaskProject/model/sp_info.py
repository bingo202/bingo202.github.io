from db import db

class sp_info(db.Model):
    __tablename__='sp_info'
    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    sp_name = db.Column(db.String(255),nullable=True)
    shop_name = db.Column(db.String(255),nullable=True)
    price = db.Column(db.Float(precision="10,2"),nullable=True)
    comment_num = db.Column(db.String(255),nullable=True)
    th = db.Column(db.String(255),nullable=True)
    img_url = db.Column(db.String(255),nullable=True)
    sp_url = db.Column(db.String(255),nullable=True)
    type_sp = db.Column(db.String(255),nullable=True)
