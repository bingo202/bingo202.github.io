import pymysql
import  pandas as pd
import random

def start_list():
    value_start = []
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
    sql = "select * from comment"
    df_comment = pd.read_sql(sql, conn)
    df_comment['conent'] = df_comment['conent'].astype('int')
    a = df_comment.groupby(['type_sp', 'conent'])['sp_url'].count()
    a_list = a.values.tolist()

    for i in range(5):
        value_start.append(a_list[i::5])
    return value_start

def start_a_list():
    value_start=start_list()
    data_g_start = []
    name_index = ['T恤', '上衣', '外套', '毛衣', '泳装', '牛仔装', '裤子', '西装', '运动装', '连衣裙']

    for i in value_start[3:]:
        b = []
        for a in range(len(i)):
            b.append({'value': i[a], 'name': name_index[a]})
        data_g_start.append(b)

    return data_g_start

def comment_num_data():
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
    sql = "select * from sp_info"
    df_sp = pd.read_sql(sql, conn)
    comment_num = []
    for i in df_sp['comment_num']:
        if '万' not in i.split('条')[0]:
            comment_num.append('1万以下')
        else:
            comment_num.append(i.split('条')[0])
    df_sp['comment_num_s'] = comment_num
    a = df_sp['comment_num_s'].value_counts().index.tolist()
    b = df_sp['comment_num_s'].value_counts().values.tolist()

    a[1], a[2] = a[2], a[1]
    b[1], b[2] = b[2], b[1]
    return {'a':a,'b':b}