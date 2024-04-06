
import pymysql
import  pandas as pd
import random
def fz_type():
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
    sql = "select * from sp_info"
    df_sp = pd.read_sql(sql, conn)

    type_list=df_sp['type_sp'].value_counts().index.tolist()
    return type_list

def fz_info_data():
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")

    sql = "select * from sp_info_1"
    df_sp_1 = pd.read_sql(sql, conn)

    sql = "select * from sp_info"
    df_sp = pd.read_sql(sql, conn)

    df_sp_1['haoping'] = df_sp_1['haoping'].apply(lambda x: x[:-1])
    try:
        df_sp_1['haoping'] = df_sp_1['haoping'].astype(int)
    except ValueError:
        df_sp_1['haoping'] = pd.to_numeric(df_sp_1['haoping'], errors='coerce')
    df_sp_1 = df_sp_1.dropna()
    df_sp_info = pd.merge(df_sp_1, df_sp, on='sp_url')[
        ['sp_url', 'haoping', 'zhongping', 'chaping', 'haoping_lv', 'sp_name', 'shop_name', 'price', 'img_url']]
    df_sp_info.drop_duplicates(subset=['sp_url'], keep='first', inplace=True)
    df_sp_info_list = df_sp_info.to_dict(orient='records')
    return df_sp_info_list

def fz_search_data(type_a):
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")

    sql = "select * from sp_info_1"
    df_sp_1 = pd.read_sql(sql, conn)

    sql = "select * from sp_info where type_sp='{}'".format(type_a)
    df_sp = pd.read_sql(sql, conn)

    df_sp_info = pd.merge(df_sp_1, df_sp, on='sp_url')[
        ['sp_url', 'haoping', 'zhongping', 'chaping', 'haoping_lv', 'sp_name', 'shop_name', 'price', 'img_url','type_sp']]
    df_sp_info.drop_duplicates(subset=['sp_url'], keep='first', inplace=True)
    # df_sp_info=df_sp_info[df_sp_info['type_se']==type_a]
    df_sp_info_list = df_sp_info.to_dict(orient='records')
    random.shuffle(df_sp_info_list)
    return df_sp_info_list