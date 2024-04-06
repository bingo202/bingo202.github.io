
import pandas as pd
import random

def get_10_word():
    with open('./static/output/all_data/TOP10高频词.txt','r') as f:
        a=f.readlines()
    value_index=[]
    for i in a:
        b={ 'value': i.split(' ')[1], 'name': i.split(' ')[0] }
        value_index.append(b)
    return value_index

def get_test_res():
    df=pd.read_excel('./static/output/all_data/评论_情感评分结果.xlsx')
    a=df.to_dict(orient='records')
    random.shuffle(a)
    return a

def search_row_word(file_name):
   file_a='./static/output/'+file_name+'_data/'
   with open(file_a+'TOP10高频词.txt', 'r') as f:
       a = f.readlines()
   value_index = []
   for i in a:
       b = {'value': i.split(' ')[1], 'name': i.split(' ')[0]}
       value_index.append(b)
   df=pd.read_excel(file_a+'评论_情感评分结果.xlsx')
   df=df.to_dict(orient='records')
   random.shuffle(df)
   return value_index,df
