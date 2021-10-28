项目中更新了sql文件，但是我没有测试过是否可行，如果在数据库连接部分还有问题，请见issues。

# 观察者新闻网爬虫（新闻爬虫）

## 项目包含技术

爬虫： Requests + etree + Xpath

可视化： Flask + Echarts + WordCloud

文本分析：jieba分词

数据库： MySQL

##  说明

本项目是完成学校实训的作业，实现了对观察者新闻网的新闻内容爬取，存储，文本分析与可视化。（只供学习，如果涉及新闻版权等问题，作者立刻删仓库跑路！）

完成的时间很仓促，项目整个完成时间大约4天。这期间，由于没有任何爬虫基础，所以边学边做，项目疏漏的地方一定很多，欢迎指正！

本项目在实现过程中参考了以下内容

B站： [基础python+Flask+爬虫 ](https://www.bilibili.com/video/BV12E411A7ZQ?from=search&seid=17327553224685529336) 通过这个课程了解了爬虫的基础知识并且学习了网站搭建的知识（负基础教程，老师讲的很细很细，我是跳着看的

爬虫模块，参考了一个爬取观察者网的代码（但是我找不到链接了，找到了再来补，在上面做了很多改进）

B站：[Xpath相关内容](https://www.bilibili.com/video/BV1mW411D7wC?from=search&seid=2199964054070293764)  通过这个学习的Xpath 讲的也很清楚 

搜索界面的网页模板参考的是github上一个demo [搜索界面UI](https://github.com/kaibush/flask_search_ui)

## 使用

> 因为时间匆忙，忘记创建虚拟环境，所以暂时无法提供requrements.txt， 不过用的都是很常见的库，都可以通过pip来安装！

1. 配置环境 

```
pip install XXX
```

2. 运行app, 然后点击命令行中的地址

   ![启动](https://github.com/hunter-lee1/guanchazhe_spider/blob/master/img-storage/image-20200720154016179.png)

   

   ![image-20200720154157803](https://github.com/hunter-lee1/guanchazhe_spider/blob/master/img-storage/image-20200720154157803.png)

   ## 实现效果
  
   1. 词频可视化![词频可视化页](https://github.com/hunter-lee1/guanchazhe_spider/blob/master/img-storage/words_weights.gif)

   2. 词云![词云](https://github.com/hunter-lee1/guanchazhe_spider/blob/master/img-storage/word_cloud.gif)

   3. 搜索![搜索](https://github.com/hunter-lee1/guanchazhe_spider/blob/master/img-storage/search.gif)

      
