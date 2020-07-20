# Guanchazhe_News_spider

## 项目包含技术

爬虫： Requests + etree + Xpath

可视化： Flask + Echarts + WordCloud

文本分析：jieba分词

数据库： MySQL

##  说明

本项目是完成学校实训的作业，时间仓促，项目整个完成时间大约4天，在实现过程中参考了以下内容

B站： [基础python+Flask+爬虫 ](https://www.bilibili.com/video/BV12E411A7ZQ?from=search&seid=17327553224685529336) 通过这个课程了解了爬虫的基础知识并且学习了网站搭建的知识（负基础教程，老师讲的很细很细，我是跳着看的

爬虫模块，参考了一个爬取观察者网的代码（但是我找不到链接了，找到了再来补，在上面做了很多改进）

B站：[Xpath相关内容](https://www.bilibili.com/video/BV1mW411D7wC?from=search&seid=2199964054070293764)  通过这个学习的Xpath 讲的也很清楚 

## 使用

> 因为时间匆忙，忘记创建虚拟环境，所以暂时无法提供requrements.txt， 不过用的都是很常见的库都可以通过pip来安装！

1. 配置环境 

```
pip install XXX
```

2. 运行app, 然后点击命令行中的地址

   ![启动](https://github.com/hunter-lee1/guanchazhe_spider/blob/master/img-storage/image-20200720154016179.png)

   

   ![image-20200720154157803](https://github.com/hunter-lee1/guanchazhe_spider/blob/master/img-storage/image-20200720154016179.png)

   ## 实现效果

   1. 首页

   ![首页](E:\Flask_spider\img-storage\首页.gif)

   2. 新闻页 ![新闻页](E:\Flask_spider\img-storage\新闻页.gif)

   3. 词频可视化![词频可视化页](E:\Flask_spider\img-storage\词频可视化页.gif)

   4. 词云![词云](E:\Flask_spider\img-storage\词云.gif)

   5. 搜索![搜索](E:\Flask_spider\img-storage\搜索.gif)

      