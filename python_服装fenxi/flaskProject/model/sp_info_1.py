from db import db

class sp_info_1(db.Model):
    __tablename__='sp_info_1'
    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    sp_url = db.Column(db.String(255),nullable=True)
    shaitu = db.Column(db.String(255),nullable=True)
    spshai = db.Column(db.String(255),nullable=True)
    zuiping = db.Column(db.String(255),nullable=True)
    haoping = db.Column(db.String(255),nullable=True)
    zhongping = db.Column(db.String(255),nullable=True)
    chaping = db.Column(db.String(255),nullable=True)
    shiyong_jijie = db.Column(db.String(255),nullable=True)
    fashion = db.Column(db.String(255),nullable=True)
    banxing = db.Column(db.String(255),nullable=True)
    shiyong_changsuo = db.Column(db.String(255),nullable=True)
    style = db.Column(db.String(255),nullable=True)
    keywords = db.Column(db.String(255),nullable=True)
    haoping_lv = db.Column(db.String(255),nullable=True)
