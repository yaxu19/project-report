from bs4 import BeautifulSoup

#proName="金融壹账通"
proName="360数科"
fw=open(f"{proName}url.txt","w",encoding="utf-8")
for i in range(1,101):
    fr=open(f"{proName}list/{i}.html",encoding="utf-8")
    html=fr.read()
    fr.close()

    soup=BeautifulSoup(html,"lxml")
    divs=soup.find_all("div",class_="box-result clearfix")
    for div  in divs:
        a=div.h2.a
        href=a["href"]
        title=a.text

        row=[title,href]
        fw.write(str(row)+"\n")
        print(title,href)
fw.close()