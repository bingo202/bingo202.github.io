from flask import Flask,session,render_template,redirect,Blueprint,request
from utilss.errorResponse import *
from model.User import User
from db import db

ub = Blueprint('user',__name__,url_prefix='/user',template_folder='templates')

@ub.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(user_name=request.form['username'], user_password=request.form['password']).first()
        if user:
            session['username'] = user.user_name
            return redirect('/page/home')
        else:
            return errorResponse('输入的密码或者账号错误')
    else:
        return render_template('login.html')

@ub.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User.query.filter_by(user_name=request.form['username']).first()
        if user:
            return errorResponse('该用户已存在')
        password = request.form['password']
        qpassword = request.form['qpassword']
        if password!=qpassword:
            return errorResponse('两次密码不一致')


        newUser = User(user_name=request.form['username'],
                       user_password=request.form['password'],
                       sex=request.form['sex'],
                       like_type=request.form['tyle_like'],
                       tall=request.form['tall'],
                       weight=request.form['weight'])
        print(newUser)
        db.session.add(newUser)
        db.session.commit()
        return redirect('/user/login')

    else:
        fs_type=['上衣类','裤子类','运动装类','连衣裙类','外套类','毛衣类','西装类','T恤类','牛仔装类','泳装类']
        return render_template('register.html',fs_type=fs_type)

@ub.route('/logOut',methods=['GET','POST'])
def logOut():
    session.clear()
    return redirect('/user/login')

