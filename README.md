环境要求：
python==3.6
jieba == 0.42.1
wordcloud == 1.8.2.2

运行顺序：
1.python 1xlGetList.py  从新浪财经网站爬取页面
2.python 2xlReadList.py   读取爬取的网页内容
3.python 3xlGetDetail.py  提取有关新闻标题及页面
4.python 4xlReadDetail.py  提取页面文字内容
5.python 5wordcloud.py   生成频次表
6.python check_word.py 生成筛选后的频次表