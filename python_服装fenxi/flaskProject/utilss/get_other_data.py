import pymysql
import pandas as pd
import re
from collections import Counter
from wordcloud import WordCloud
import jieba.analyse
import pprint
def shengfen_china():
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
    return num_conm_a

def make_wordcloud(v_str, v_stopwords, v_outfile):
    """
    绘制词云图
    :param v_str: 输入字符串
    :param v_stopwords: 停用词
    :param v_outfile: 输出文件
    :return: None
    """
    print('开始生成词云图：{}'.format(v_outfile))
    try:
        stopwords = v_stopwords  # 停用词
        wc = WordCloud(
            width=1500,  # 图宽
            height=1200,  # 图高
            max_words=1500,  # 最多字数
            font_path="C:\Windows\Fonts\simhei.ttf",
            stopwords=stopwords,  # 停用词
        )
        jieba_text = " ".join(jieba.lcut(v_str))
        wc.generate_from_text(jieba_text)
        wc.to_file(v_outfile)
        print('词云文件保存成功：{}'.format(v_outfile))
    except Exception as e:
        print('make_wordcloud except: {}'.format(str(e)))

def word_c():
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
    sql = "select * from comment"
    df_comment = pd.read_sql(sql, conn)
    text_list = [eval(i)[0] for i in df_comment['buy_info']]
    v_cmt_list = [str(i) for i in text_list]
    v_cmt_str = ' '.join(str(i) for i in v_cmt_list)

    make_wordcloud(v_str=v_cmt_str,
                   # 停用词
                   v_stopwords=['这个', '吗', '的', '啊', '她', '是', '了', '你', '我', '都', '也', '不', '在', '吧',
                                '说', '就是', '这',
                                '有', '就', '或', '哇', '哦', '这样', '真的', '还'],
                   # 词云图文件名
                   v_outfile='./static/output/颜色_词云图.jpg'
                   )

def word_th():
    conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
    sql = "select * from sp_info"
    df_sp = pd.read_sql(sql, conn)
    text_list = [i.strip() for i in df_sp['th']]
    v_cmt_list = [str(i) for i in text_list]
    v_cmt_str = ' '.join(str(i) for i in v_cmt_list)
    keywords_top10 = jieba.analyse.extract_tags(
        v_cmt_str, withWeight=True, topK=10)
    print('top10关键词及权重：')
    with open( './static/output/优惠_TOP10高频词.txt', 'w') as f:
        for i in keywords_top10:
            f.write(str(i[0]) + ' ' + str(i[1]))  # i[0]是关键词，i[1]是权重值
            f.write('\n')

    make_wordcloud(v_str=v_cmt_str,
                   # 停用词
                   v_stopwords=['这个', '吗', '的', '啊', '她', '是', '了', '你', '我', '都', '也', '不', '在', '吧',
                                '说', '就是', '这',
                                '有', '就', '或', '哇', '哦', '这样', '真的', '还'],
                   # 词云图文件名
                   v_outfile='./static/output/优惠_词云图.jpg'
                   )

def bar_data_th():
    with open('./static/output/优惠_TOP10高频词.txt', 'r') as f:
        a = f.readlines()
    index_name = []
    index_values = []
    for i in a:
        b = i.strip().split(' ')
        pattern = re.compile(r'[\u4e00-\u9fa5]')
        if bool(pattern.search(b[0])):
            index_name.append(b[0])
            index_values.append(b[1])

    return {'index_name':index_name,'index_values':index_values}