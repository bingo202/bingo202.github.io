from random import random
from utilss.get_index_data import hao_ping_data,num_info,shengfen_num,bar_time
from utilss.get_search_data import fz_type,fz_info_data,fz_search_data
from utilss.get_comment_data import start_list,start_a_list,comment_num_data
from utilss.qinggan import get_10_word,get_test_res,search_row_word
from utilss.get_shop_data import get_shop_info,scatt_data,bar_shop,pre_data
from utilss.get_other_data import shengfen_china,word_c,word_th,bar_data_th
import random
from flask import Flask, session, render_template, redirect, Blueprint, request
from flask_paginate import Pagination, get_page_parameter


pb = Blueprint('page',__name__,url_prefix='/page',template_folder='templates')

@pb.route('/home')
def home():
    username = session.get('username')
    dict_shop_sp=hao_ping_data()
    num_dict=num_info()
    num_conm_a=shengfen_num()
    bar_info=bar_time()

    return render_template('index.html',username=username,dict_shop_sp=dict_shop_sp,num_dict=num_dict,num_conm_a=num_conm_a,bar_info=bar_info)

@pb.route('/search')
def search_all():
    username = session.get('username')
    df_sp_info_list=fz_info_data()
    random.shuffle(df_sp_info_list)

    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10  # 每页显示的数据条数
    offset = (page - 1) * per_page
    data_subset = df_sp_info_list[offset:offset + per_page]
    pagination = Pagination(page=page, total=len(df_sp_info_list), per_page=per_page, css_framework='bootstrap4')

    return render_template('search.html', username=username, df_sp_info_list=df_sp_info_list, data=data_subset, pagination=pagination)


@pb.route('/search/type', methods=['GET', 'POST'])
def search_1():
    username = session.get('username')
    type_list=fz_type()
    if request.method == 'POST':
        df_sp_info_list=fz_search_data(request.form['tyle_like'])
        page = request.args.get(get_page_parameter(), type=int, default=1)
        per_page = 10  # 每页显示的数据条数
        offset = (page - 1) * per_page
        data_subset = df_sp_info_list[offset:offset + per_page]
        pagination = Pagination(page=page, total=len(df_sp_info_list), per_page=per_page, css_framework='bootstrap4')
        keyword = request.form['tyle_like']
    else:
        df_sp_info_list = fz_search_data('毛衣')
        page = request.args.get(get_page_parameter(), type=int, default=1)
        per_page = 10  # 每页显示的数据条数
        offset = (page - 1) * per_page
        data_subset = df_sp_info_list[offset:offset + per_page]
        pagination = Pagination(page=page, total=len(df_sp_info_list), per_page=per_page, css_framework='bootstrap4')
        keyword='毛衣'
    return render_template('search_1.html',username=username,type_list=type_list,data_subset=data_subset,pagination=pagination,keyword=keyword)

@pb.route('/comment',methods=['GET','POST'])
def comment_f():
    username = session.get('username')
    value_start = start_list()
    data_g_start=start_a_list()
    num_data=comment_num_data()
    return render_template('comment.html',username=username,value_start=value_start,data_g_start=data_g_start,num_data=num_data)

@pb.route('/qinggan')
def qinggan_all():
    username = session.get('username')
    value_index=get_10_word()
    df=get_test_res()

    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10  # 每页显示的数据条数
    offset = (page - 1) * per_page
    data_subset = df[offset:offset + per_page]
    pagination = Pagination(page=page, total=len(df), per_page=per_page, css_framework='bootstrap4')

    return render_template('qinggan.html',username=username,value_index=value_index,data_subset=data_subset,pagination=pagination)

@pb.route('/qinggan/search',methods=['GET','POST'])
def qinggan_search():
    username = session.get('username')
    type_list = fz_type()
    if request.method == 'POST':
        keyword=request.form['tyle_search']
        value_index,df=search_row_word(keyword)

        page = request.args.get(get_page_parameter(), type=int, default=1)
        per_page = 10  # 每页显示的数据条数
        offset = (page - 1) * per_page
        data_subset = df[offset:offset + per_page]
        pagination = Pagination(page=page, total=len(df), per_page=per_page, css_framework='bootstrap4')
        return render_template('qinggan_search.html',username=username,type_list=type_list,keyword=keyword,value_index=value_index,data_subset=data_subset,pagination=pagination)

    keyword = '毛衣'
    value_index, df = search_row_word(keyword)

    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10  # 每页显示的数据条数
    offset = (page - 1) * per_page
    data_subset = df[offset:offset + per_page]
    pagination = Pagination(page=page, total=len(df), per_page=per_page, css_framework='bootstrap4')
    return render_template('qinggan_search.html',username=username,type_list=type_list,keyword=keyword,value_index=value_index,data_subset=data_subset,pagination=pagination)

@pb.route('/shop',methods=['GET','POST'])
def shop_info():
    username = session.get('username')
    df_shop=get_shop_info()
    random.shuffle(df_shop)

    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10  # 每页显示的数据条数
    offset = (page - 1) * per_page
    data_subset = df_shop[offset:offset + per_page]
    pagination = Pagination(page=page, total=len(df_shop), per_page=per_page, css_framework='bootstrap4')

    return render_template('shop.html',username=username,df_shop=data_subset,pagination=pagination)

@pb.route('/shop/views')
def shop_views():
    username=session.get('username')
    data_dict = scatt_data()
    bar_data=bar_shop()
    pre_dict=pre_data()
    return render_template('shop_views.html',username=username,data_dict=data_dict,bar_data=bar_data,pre_dict=pre_dict)


@pb.route('/other')
def other_view():
    username=session.get('username')
    num_conm_a=shengfen_china()
    bar_data=bar_data_th()
    # word_th()
    # word_c()
    return render_template('other_view.html',username=username,num_conm_a=num_conm_a,bar_data=bar_data)


