# import jieba        #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud         #词云
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算
import pymysql                          #数据库
import jieba.analyse


#准备词云所需的文字（词）

datalist = []
cnn = pymysql.connect(host='127.0.0.1', user='root', password='shujuku', port=3306, database='news_with_keyword',
                      charset='utf8')
cursor = cnn.cursor()
sql = ' select * from guanchazhe'
cursor.execute(sql)
for item in cursor.fetchall():
    datalist.append(item)
cursor.close()
cnn.close()

text = " "
# 取出数据库中的新闻内容，进行分词
for item in datalist:
    text =  text + item[4]
cut = jieba.cut(text)
string = ' '.join(cut)

img = Image.open(r'.\static\assets\img\tree.jpg')   #打开遮罩图片
img_array = np.array(img)   #将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc"    #字体所在位置：C:\Windows\Fonts
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     #是否显示坐标轴

plt.show()    #显示生成的词云图片

#输出词云图片到文件
plt.savefig(r'.\static\assets\img\key_word.jpg',dpi=500)

















