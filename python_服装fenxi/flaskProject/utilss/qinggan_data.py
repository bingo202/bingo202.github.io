import pandas as pd
from snownlp import SnowNLP
from wordcloud import WordCloud
from pprint import pprint
import jieba.analyse
import matplotlib.pyplot as plt
import pymysql
from sklearn.metrics import precision_score
import os


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def sentiment_analyse(v_cmt_list):
    """
    情感分析打分
    :param v_cmt_list: 需要处理的评论列表
    :return:
    """
    score_list = []
    tag_list = []
    pos_count = 0
    neg_count = 0
    mid_count = 0
    for comment in v_cmt_list:
        tag = ''
        sentiments_score = SnowNLP(comment).sentiments
        if sentiments_score < 0.5:
            tag = '消极'
            neg_count += 1
        elif sentiments_score > 0.5:
            tag = '积极'
            pos_count += 1
        else:
            tag = '中性'
            mid_count += 1
        score_list.append(sentiments_score)
        tag_list.append(tag)
    df_p['情感得分'] = score_list
    df_p['分析结果'] = tag_list
    grp = df_p['分析结果'].value_counts()
    print('正负面评论统计：')
    print(grp)
    grp.plot.pie(y='分析结果', autopct='%.2f%%')
    plt.title('评论_情感分布占比图')
    plt.savefig(file_name+'/评论_情感分布占比图.png')
    df_p.to_excel(file_name+'/评论_情感评分结果.xlsx', index=None)

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

conn = pymysql.connect(host="localhost", user="root", passwd="123456", db='fz_data', port=3306, charset="utf8")
keywords=['T恤', '外套', '毛衣', '泳装', '牛仔装', '裤子', '西装', '运动装', '连衣裙']
for keyword in keywords:
    if not os.path.exists('../static/output/{}_data'.format(keyword)):
        os.mkdir('../static/output/{}_data'.format(keyword))

    file_name='../static/output/{}_data'.format(keyword)

    if keyword:
        sql = "select * from comment where type_sp='{}'".format(keyword)
        df_comment = pd.read_sql(sql, conn)
    else:
        sql = "select * from comment"
        df_comment = pd.read_sql(sql, conn)

    df_p=df_comment[['user_start','conent','type_sp']]
    v_cmt_list = df_p['user_start'].values.tolist()
    print('length of v_cmt_list is:{}'.format(len(v_cmt_list)))
    v_cmt_list = [str(i) for i in v_cmt_list]
    v_cmt_str = ' '.join(str(i) for i in v_cmt_list)

    sentiment_analyse(v_cmt_list)

    # 2、用jieba统计弹幕中的top10高频词
    keywords_top10 = jieba.analyse.extract_tags(
        v_cmt_str, withWeight=True, topK=10)
    print('top10关键词及权重：')
    pprint(keywords_top10)
    with open(file_name+'/TOP10高频词.txt', 'w') as f:
        for i in keywords_top10:
            f.write(str(i[0]) + ' ' + str(i[1]))  # i[0]是关键词，i[1]是权重值
            f.write('\n')



    score_q=df_p.groupby('分析结果')['情感得分'].mean()
    plt.bar(score_q.index,score_q.values)
    plt.savefig(file_name+'/分析结果.jpg')
    plt.show()

    score_list=[]
    for i in df_p['情感得分']:
        if i >=0.55:
            score_list.append('积极')
        elif i <0.55:
            if i>0.45:
                score_list.append('中性')
            else :
                score_list.append('消极')

    df_p['实际值']=score_list

    df_1=df_p.replace({'分析结果':{'积极':0,'中性':1,'消极':2},'实际值':{'积极':0,'中性':1,'消极':2}})
    labels = [0,1,2]
    precision = precision_score(df_1['分析结果'], df_1['实际值'], labels=labels, average="micro") # average 指定为micro
    prec= precision_score(df_1['分析结果'], df_1['实际值'], labels=labels, average="macro")
    print('精准率：',precision)
    print('召回率：',prec)

    plt.bar(['精准率','召回率'],[1,1])
    plt.bar(['精准率','召回率'],[precision,prec])
    plt.title('模型精准率与召回率展示')
    plt.legend(['100%','n%'])
    plt.savefig(file_name+'/模型精准率与召回率.jpg')
    plt.show()
    # 3、画词云图
    make_wordcloud(v_str=v_cmt_str,
                   # 停用词
                   v_stopwords=['这个', '吗', '的', '啊', '她', '是', '了', '你', '我', '都', '也', '不', '在', '吧', '说', '就是', '这',
                                '有', '就', '或', '哇', '哦', '这样', '真的', '还'],
                   # 词云图文件名
                   v_outfile=file_name+'/评论_词云图.jpg'
                   )

