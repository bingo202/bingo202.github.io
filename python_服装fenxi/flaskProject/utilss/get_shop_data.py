import pymysql
import pandas as pd

def get_shop_info():
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
    sql = "select * from shop_info"
    df_shop = pd.read_sql(sql, conn)
    df_shop = df_shop.iloc[:, 1:].drop_duplicates()
    df_shop=df_shop.to_dict(orient='records')
    return df_shop

def scatt_data():
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
    sql = "select * from shop_info"
    df_shop = pd.read_sql(sql, conn)
    df_shop = df_shop.iloc[:, 1:].drop_duplicates()
    df_shop['shop_start_p'] = [i.split(' ')[0] for i in df_shop['shop_price']]
    df_shop['shop_start_type'] = [i.split(' ')[1] for i in df_shop['shop_price']]
    df_shop['wuliu_price_p'] = [i.split(' ')[0] for i in df_shop['wuliu_price']]
    df_shop['wuliu_price_type'] = [i.split(' ')[1] for i in df_shop['wuliu_price']]
    df_shop['shouhou_price_p'] = [i.split(' ')[0] for i in df_shop['shouhou_price']]
    df_shop['shouhou_price_type'] = [i.split(' ')[1] for i in df_shop['shouhou_price']]
    df_shop[['shop_start', 'shop_start_p', 'wuliu_price_p', 'shouhou_price_p']] = df_shop[
        ['shop_start', 'shop_start_p', 'wuliu_price_p', 'shouhou_price_p']].astype('float')
    shop_level = df_shop[['shop_start', 'shop_start_p']].values.tolist()
    wuliu_level = df_shop[['shop_start', 'wuliu_price_p']].values.tolist()
    shouhou_level = df_shop[['shop_start', 'shouhou_price_p']].values.tolist()

    return {'shop_level':shop_level,'wuliu_level':wuliu_level,'shouhou_level':shouhou_level}

def bar_shop():
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
    sql = "select * from shop_info"
    df_shop = pd.read_sql(sql, conn)
    df_shop = df_shop.iloc[:, 1:].drop_duplicates()
    df_shop['shop_start_p'] = [i.split(' ')[0] for i in df_shop['shop_price']]
    df_shop['shop_start_type'] = [i.split(' ')[1] for i in df_shop['shop_price']]
    df_shop['wuliu_price_p'] = [i.split(' ')[0] for i in df_shop['wuliu_price']]
    df_shop['wuliu_price_type'] = [i.split(' ')[1] for i in df_shop['wuliu_price']]
    df_shop['shouhou_price_p'] = [i.split(' ')[0] for i in df_shop['shouhou_price']]
    df_shop['shouhou_price_type'] = [i.split(' ')[1] for i in df_shop['shouhou_price']]
    df_shop[['shop_start', 'shop_start_p', 'wuliu_price_p', 'shouhou_price_p']] = df_shop[
        ['shop_start', 'shop_start_p', 'wuliu_price_p', 'shouhou_price_p']].astype('float')
    shop_level = df_shop[['shop_start', 'shop_start_p']].values.tolist()
    wuliu_level = df_shop[['shop_start', 'wuliu_price_p']].values.tolist()
    shouhou_level = df_shop[['shop_start', 'shouhou_price_p']].values.tolist()
    df_shop[df_shop['shop_start'] == 4.9][:6]['shop_name'].tolist()
    df_shop_data = df_shop[df_shop['shop_start'] == 4.9][:6][
        ['shop_name', 'shop_start_p', 'wuliu_price_p', 'shouhou_price_p']]
    shop_name = df_shop_data['shop_name'].tolist()
    shop_start = df_shop_data['shop_start_p'].tolist()
    wuliu_price = df_shop_data['wuliu_price_p'].tolist()
    shouhou_price = df_shop_data['shouhou_price_p'].tolist()
    return {'shop_name':shop_name,'shop_start':shop_start,'wuliu_price':wuliu_price,'shouhou_price':shouhou_price}

def pre_data():
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
    sql = "select * from shop_info"
    df_shop = pd.read_sql(sql, conn)
    df_shop = df_shop.iloc[:, 1:].drop_duplicates()
    df_shop['shop_start_p'] = [i.split(' ')[0] for i in df_shop['shop_price']]
    df_shop['shop_start_type'] = [i.split(' ')[1] for i in df_shop['shop_price']]
    df_shop['wuliu_price_p'] = [i.split(' ')[0] for i in df_shop['wuliu_price']]
    df_shop['wuliu_price_type'] = [i.split(' ')[1] for i in df_shop['wuliu_price']]
    df_shop['shouhou_price_p'] = [i.split(' ')[0] for i in df_shop['shouhou_price']]
    df_shop['shouhou_price_type'] = [i.split(' ')[1] for i in df_shop['shouhou_price']]
    df_shop[['shop_start', 'shop_start_p', 'wuliu_price_p', 'shouhou_price_p']] = df_shop[
        ['shop_start', 'shop_start_p', 'wuliu_price_p', 'shouhou_price_p']].astype('float')
    df_shop['shop_level'] = df_shop['shop_start'].apply(lambda x: '低' if x < 4.0 else ('中' if x < 4.5 else '高'))
    shop_list = []
    shop_d_list = []
    wuliu_list = []
    shouhou_list = []
    a = df_shop['shop_level'].value_counts()
    b = df_shop['shop_start_type'].value_counts()
    c = df_shop['wuliu_price_type'].value_counts()
    d = df_shop['shouhou_price_type'].value_counts()

    for i in range(len(a.index.tolist())):
        shop_list.append({'value': a.values.tolist()[i], 'name': a.index.tolist()[i]})
        shop_d_list.append({'value': b.values.tolist()[i], 'name': b.index.tolist()[i]})
        wuliu_list.append({'value': c.values.tolist()[i], 'name': c.index.tolist()[i]})
        shouhou_list.append({'value': d.values.tolist()[i], 'name': d.index.tolist()[i]})

    return {"shop_list":shop_list,'shop_d_list':shop_d_list,'wuliu_list':wuliu_list,'shouhou_list':shouhou_list}