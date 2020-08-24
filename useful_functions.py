import pymysql
import jieba.analyse


HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'shujuku'
PORT = 3306
DATABASE = 'guanchazhe_spider'
CHAREST = 'utf8'


# 连接数据库并提取数据库内容
def get_datalist():
    datalist = []
    cnn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, port=PORT, database=DATABASE,
                          charset=CHAREST)
    cursor = cnn.cursor()
    sql = ' select * from guanchazhe ORDER BY publish_time DESC'
    cursor.execute(sql)
    for item in cursor.fetchall():
        datalist.append(item)
    cursor.close()
    cnn.close()
    return datalist


# 对数据库文本内容进行分词，并返回 data_inf0 = [新闻数，词云数，词汇数，作者人数] ->首页展示的三个内容
def get_datalist_info(datalist):
    text = ""
    for item in datalist:
        text = text + item[4]

    # 分词
    cut = jieba.cut(text)
    string = ' '.join(cut)
    data_info = [len(datalist), 1, len(string), 1]
    return data_info,string


# 对输入文本进行分词，并返回词汇权重
def get_word_weights(string, topK):
    words = []
    weights = []
    for x, w in jieba.analyse.textrank(string, withWeight=True, topK=topK):
        words.append(x)
        weights.append(w)
    return words,weights


# 文本关键字提取
def get_keyword_from_content(content):
    print(content)
    cut = jieba.cut(content)
    string = ' '.join(cut)
    words,_=get_word_weights(string, topK=5)
    return words.append('（自动生成）')