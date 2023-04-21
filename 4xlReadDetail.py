from bs4 import BeautifulSoup

proName="360数科"
fw=open(f"{proName}.txt","w",encoding="utf-8")
for i in range(0,900):
    try:
        fr=open(f"{proName}detail\\{i}.html",encoding="utf-8")
        html=fr.read()
        fr.close()
    except:
        continue

    if "文章不存在" in html:
        continue

    soup=BeautifulSoup(html,"lxml")
    try:
        title=soup.find("h1",class_="main-title").text
    except:
        title=""
    try:
        content=soup.find("div",id="artibody").text
    except:
        content = soup.find("div", class_="article").text

    title=title.replace("\xa0","")
    content=content.strip()
    content=content.replace("\u3000"," ")
    content = content.replace("\xa0", " ")
    content = content.replace("\u2002", " ")
    while "\n\n" in content:
        content=content.replace("\n\n","\n")
    print([i,title,content])
    fw.write(title+"\n")
    fw.write(content+"\n\n")
fw.close()