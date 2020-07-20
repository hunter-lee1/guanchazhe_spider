from flask import Flask,render_template
import pymysql
from model.forms import SearchForm
from flask import request
import useful_functions
import spider_modul
# 这里对数据库内容进行提取
# spider_modul.run()
datalist = useful_functions.get_datalist()
# datalist_reverse = datalist
# datalist_reverse.reverse()

# 这里分析数据库内容，提炼出数据库信息，并对文本内容分词
datainfo1, string = useful_functions.get_datalist_info(datalist)

# 计算 topK=8 的词汇对应的词频
words,weights = useful_functions.get_word_weights(string, topK=8)

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"





# 首页重定位
@app.route('/index')
def home_page():
    return index()


@app.route('/temp')
def temp_page():
    return index()


# 首页
@app.route('/')
def index():
    global weights
    global words
    global data_info
    print(words, weights)
    data_info = datainfo1
    return render_template("index.html", news_info=data_info)

# 新闻缩略页
@app.route('/news')
def news_page():
    return render_template("news.html",news=datalist)


# 基于词频绘制的词云
@app.route('/word')
def word_page():
    return render_template("word.html",news_info=data_info)


# 链接到我的个人主页
@app.route('/team')
def team_page():
    return render_template("team.html")


# 数据库文本信息分析，topK8的词语及频率，暂时用的是直方图
@app.route('/analysis')
def analysis_page():
    return render_template("analysis.html",words = words,weights = weights)


# 搜索界面
@app.route('/search')
def search_page():
    form = SearchForm()
    return render_template('search.html', form=form)


# 搜索结果返回界面，返回时展示数据库中所有内容，包括正文文本
@app.route('/news_result',methods=['POST','GET'])
def newsResult_page():
    form = SearchForm()
    search = request.args.get("query")
    search_list = []
    cnn_search = pymysql.connect(host='127.0.0.1', user='root', password='shujuku', port=3306, database='news_with_keyword',
                                 charset='utf8')
    cursor_search = cnn_search.cursor()
    sql_search = "select * from guanchazhe where content like '{}'".format('%'+search+'%')
    print(sql_search)
    cursor_search.execute(sql_search)
    for item_search in cursor_search.fetchall():
        search_list.append(item_search)
    cursor_search.close()
    cnn_search.close()
    print(search_list)
    return render_template("news_result.html",form=form,news=search_list)


if __name__ == '__main__':
    app.run()
