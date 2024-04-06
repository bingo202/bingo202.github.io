from db import db

class shop_info(db.Model):
    __tablename__='shop_info'
    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    shop_name = db.Column(db.String(255),nullable=True)
    shop_start = db.Column(db.String(255),nullable=True)
    shop_price = db.Column(db.String(255),nullable=True)
    wuliu_price = db.Column(db.String(255),nullable=True)
    shouhou_price = db.Column(db.String(255),nullable=True)
