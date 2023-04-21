import time

import requests

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
}

proName="360数科"

fr=open(f"{proName}url.txt",encoding="utf-8")
lines=fr.readlines()
fr.close()

for i in range(len(lines)):
    if i==98:
        continue

    line=eval(lines[i])
    print(i)
    # if "金融壹账通" not in line[0]:
    if "奇富科技" not in line[0] and "360数科" not in line[0]:
        continue

    print(line[1])
    res=requests.get(line[1],headers=headers)
    res.encoding="utf-8"
    html=res.text

    fw=open(f"{proName}detail\\{i}.html","w",encoding="utf-8")
    fw.write(html)
    fw.close()


    time.sleep(2)


