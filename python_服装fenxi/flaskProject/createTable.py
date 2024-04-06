from app  import app
from db import db
# from model.User import User
from model.sp_info import sp_info
from model.sp_info_1 import sp_info_1
from model.shop_info import shop_info
from model.comment import comment

app.app_context().push()
db.create_all()