
import pymysql
import  pandas as pd
import re
from collections import Counter


def hao_ping_data():
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

    sorted_df_hao = df_sp_1.sort_values(by='haoping', ascending=False)[:7][['id', 'sp_url', 'haoping', 'haoping_lv']]
    df_sp=df_sp.iloc[:,1:].drop_duplicates()
    dict_shop_sp = {'sp_name': [], 'sp_shop': [], 'price': [], 'comment_num': [], 'img_url': [], 'sp_url': [],
                    'haoping': [], 'haoping_lv': []}
    for i in sorted_df_hao['sp_url']:
        dict_shop_sp['sp_shop'].append(df_sp[df_sp['sp_url'] == i].head(1)['shop_name'].values[0])
        dict_shop_sp['sp_name'].append(df_sp[df_sp['sp_url'] == i].head(1)['sp_name'].values[0])
        dict_shop_sp['price'].append(df_sp[df_sp['sp_url'] == i].head(1)['price'].values[0])
        dict_shop_sp['comment_num'].append(df_sp[df_sp['sp_url'] == i].head(1)['comment_num'].values[0][:6])
        dict_shop_sp['img_url'].append("http:" + df_sp[df_sp['sp_url'] == i].head(1)['img_url'].values[0])
        dict_shop_sp['sp_url'].append(df_sp[df_sp['sp_url'] == i].head(1)['sp_url'].values[0])

    dict_shop_sp['haoping'] = sorted_df_hao['haoping'].to_list()
    dict_shop_sp['haoping_lv'] = sorted_df_hao['haoping_lv'].to_list()

    dict_shop_sp=pd.DataFrame(dict_shop_sp)
    dict_shop_sp=dict_shop_sp.reset_index(drop=True).to_dict(orient='records')
    return dict_shop_sp

def num_info():
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
    sql = "select * from comment"
    df_comment = pd.read_sql(sql, conn)

    sql = "select * from shop_info"
    df_shop = pd.read_sql(sql, conn)

    sql = "select * from sp_info_1"
    df_sp_1 = pd.read_sql(sql, conn)
    df_sp_1['haoping_lv'] = df_sp_1['haoping_lv'].astype('int')

    return {'comment_num':len(df_comment), 'haoping_lv':int(df_sp_1['haoping_lv'].mean()), 'shop_num':len(df_shop)}

def shengfen_num():
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
    sql = "select * from comment"
    df_comment = pd.read_sql(sql, conn)
    list_a = []
    for i in df_comment['buy_info']:
        i = eval(i)
        if re.match('^[\u4e00-\u9fa5]+$', i[-1]):
            list_a.append(i[-1])
    num_conm_a = []
    element_counts = Counter(list_a)
    for element, count in element_counts.items():
        num_conm_a.append({'value': count, 'name': element})

    return num_conm_a[:5]


def bar_time():
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
    sql = "select * from comment"
    df_comment = pd.read_sql(sql, conn)
    year_time_list = []
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    for i in df_comment['buy_info']:
        i = eval(i)
        match = re.match(date_pattern, i[-2])
        if match:
            year_time_list.append(match.group())
        else:
            match = re.match(date_pattern, i[-1])
            year_time_list.append(match.group())
    time_a = pd.to_datetime(year_time_list)
    df_time = pd.DataFrame({'year': time_a.year, 'mon': time_a.month, 'day': time_a.day})
    index_year=df_time['year'].value_counts()[:4].index.tolist()
    index_year=[str(x) for x in index_year]
    index_year.append('2021之前')
    value_list_1 = df_time['year'].value_counts()[:4].values.tolist()
    value_list_1.append(sum(df_time[df_time['year'] < 2021]['year'].value_counts().values))
    value_list = []
    for a in value_list_1:
        if a == max(value_list_1):
            value_list.append({'value': a, 'itemStyle': {
                'color': '#a90000'
            }})
        else:
            value_list.append(a)
    return {'index_year':index_year,'value_list':value_list}

