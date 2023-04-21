import wordcloud,jieba

def getCloud(filename):
    with open(f"{filename}.txt", encoding="utf-8") as fr:
        text=fr.read()

    jieba.add_word(filename)
    textList=jieba.lcut(text)
    textWords=" ".join(textList)
    #print(textWords)

    STOPWORDS = ["在", "和", "年", "是", "与", "也","日", "月","也","，", "的","。","\n", "、",
                 "的","。","“", "”","。",",", "（", "；", "：", "了", "）"," ","为",filename]  # 停用词
    d={}
    for i in textList:
        d[i]=d.get(i,0)+1

    for key in STOPWORDS:
        try:
            del d[key]
        except:
            pass
    result = sorted(d.items(), key=lambda x: x[1], reverse=True)
    fw=open(filename+"词频统计.txt","w",encoding="utf-8")
    for key,value in result:
        fw.write("{}:{}\n".format(key,value))
    fw.close()

    w=wordcloud.WordCloud(
                          collocations=False,
                          scale=5,
                          font_path="msyh.ttc",
                          background_color="white",
                          max_words=1000,
                          contour_width=1,
                          stopwords=STOPWORDS)
    w.generate(textWords)
    w.to_file(f"词云_{filename}.jpg")


#getCloud("金融壹账通")
getCloud("360数科")
