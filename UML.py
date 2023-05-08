import jieba,os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np


def make_file(path):
    if not os.path.exists(path):
        os.makedirs(path)


def make_txt(n,la,a):
    make_file('log_%s/%s/'%(n,la))
    name = a[0]
    label = a[1]
    txt = 'log_%s/%s/%s_%s.txt'%(n,la,la,str(label))
    with open(txt,'a',encoding='utf-8') as f:
        f.write('%s'%name)

for name_ in ['金融壹账通','360数科']:
    if name_ == '金融壹账通':
        la = 'One'
    else:
        la = '360'
    for num in [4,5,6,7,8,9,10]:
        # 读取文本文件
        with open('%s.txt'%name_, 'r', encoding='utf-8') as f:
            news = f.readlines()

        # 分词并去除停用词
        stopwords = []
        # with open('stopwords.txt', 'r', encoding='utf-8') as f:
            # stopwords = [word.strip() for word in f.readlines()]
        words_list = []
        for text in news:
            words = [word for word in jieba.cut(text) if word not in stopwords]
            words_list.append(' '.join(words))

        # 特征提取
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(words_list)

        # 聚类
        kmeans = KMeans(n_clusters=num, random_state=0).fit(X)

        # 输出聚类结果
        df = pd.DataFrame({'text': news, 'label': kmeans.labels_})
        for i in np.array(df):
            make_txt(num,la,i)
            # print(i[0],i,i[1])
            # exit()
        # print(np.array(df)[10][1])
        # exit()
exit()
for k in [1]:
    for i in range(kmeans.n_clusters):
        with open('test.txt','a', encoding='utf-8') as f:
            f.write('%s\n'%(f'Cluster {i}:'))
            f.close()
        print(f'Cluster {i}:')
        cluster_df = df[df['label'] == i]
        print(cluster_df['text'],'==========')
        # print('------',cluster_df[text][10],'------------')
        names = np.array(cluster_df['text'])
        labels = np.array(cluster_df['label'])
        print(names.shape)
exit()
        # for i_ in cluster_df:
            # print('--------------',i_,'----------------')
        # with open('test.txt','a', encoding='utf-8') as f:
            # f.write('%s\n'%(f'Cluster {i}:'))
            # f.close()

# 绘制词云图
from wordcloud import WordCloud
plt.figure(figsize=(8, 8), dpi=100)
for i in range(kmeans.n_clusters):
    cluster_df = df[df['label'] == i]
    text = ' '.join(cluster_df['text'])
    wordcloud = WordCloud(width=400, height=400, background_color='white').generate(text)
    plt.subplot(2, 2, i + 1)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
plt.show()
