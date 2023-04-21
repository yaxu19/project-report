import time

import requests

headers={
    'Host':'search.sina.com.cn',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate, br',
    'Content-Type':'application/x-www-form-urlencoded',
    'Content-Length':'79',
    'Origin':'https://search.sina.com.cn',
    'Connection':'keep-alive',
    'Referer':'https://search.sina.com.cn/news',
    'Cookie':'UOR=www.baidu.com,mil.news.sina.com.cn,; ULV=1680674243821:2:1:1:111.18.4.217_1680674181.490925:1668063114851; SINAGLOBAL=124.114.130.162_1668063114.876636; __bid_n=184604f636614489524207; Hm_lvt_b82ffdf7cbc70caaacee097b04128ac1=1680674437; Qs_lvt_335601=1672141041%2C1680617806%2C1680618217; Qs_pv_335601=3144168201705445400%2C3626599799561090600%2C15751328694277248; FEID=v10-52e50482945833e890ed3707ad8cea99ea399088; __xaf_fpstarttimer__=1672141042208; __xaf_thstime__=1672141044313; FPTOKEN=R3dNlHv4JxgYsC/2OMshiianM5xfn+1tR4Cw3WNJcHqoqfxFUrqlVo3aRSLNS5dpIbo9igB8MoSViFd6h3myWOrAz8ndNILaPJThBYHDftRMKN6X4aeKbUhaS9eJFAhgG3lbfCVxRlOySuE1rwmLPMpcDLJwhCfw8/DOmabPH45YZqVJW8D33evDpejtrp6bOeankGHqlGa8RSTnpKI+Ye4rnvTBhRB0hGLbnu/tXiFLnGuuCJvg2iw7p7yn+tfV3v+b53KVIk5l3kdwPBW6lvQ3TVRJRmWAC9CS49NGWGd7TFl7rZcmeHaaTsOcHk+2jEi2kZWgbiJRLoq2D0aGXWY0NSPSsxVwR44NmuX1oE1jfylniEcXhAtWJVevdgE+fjb96a2NxR1G/RJqtENBBw==|GqtKZXhcoJXppsNXkEEGRy8wvStSILXBXB4A+qBVT84=|10|55945d431d822f0d464f95f48d382e54; __xaf_fptokentimer__=1672141044315; ALF=1683266183; SCF=ApKJPI6YcUKdojZdi_9QxNoxG3f-edxgodr7E3hTt4gsi7j7ToN80LWJyO4rk73TI7cSFAqu2D83W2lsjcz8rFU.; U_TRS1=000000a2.3e4688b.6405c42b.ce10acb5; rotatecount=2; hqEtagMode=1; Apache=111.18.4.217_1680674181.490925; SUB=_2A25JKX3XDeRhGedH7lYQ9S_Mzj6IHXVqX-gfrDV_PUNbm9ANLXHekW9NUDwaRS7Rq3JuyEV7i4AXpKDsMWWPf4Ew; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whop-ggIkOyKCbI4Fznh-4d5NHD95Qp1K-XeK-peh-EWs4DqcjLi--Xi-iWiK.Xi--ciKLhi-2Ri--fiKnfiKnRi--NiK.XiKLs15tt; U_TRS2=000000d9.18d7ac3a.642d0d87.8351556e; beegosessionID=292ac22ded1dc3b155f6eb768930266d; SEARCH-SINA-COM-CN=; Hm_lpvt_b82ffdf7cbc70caaacee097b04128ac1=1680674437',
    'Upgrade-Insecure-Requests':'1',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-User':'?1',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'TE':'trailers',
}

# proName="金融壹账通" #25
proName="360数科" #50
#proName="奇富科技" #50
url="https://search.sina.com.cn/news"
for i in range(1,51):
    # datas={
    #     "q": "金融壹账通",
    #     "c": "news",
    #     "range": "all",
    #     "size": "10",
    #     "page": str(i)
    # }

    # datas={
    #     "q": "360数科",
    #     "c": "news",
    #     "range": "all",
    #     "size": "10",
    #     "page": str(i)
    # }

    datas={
        "q": "奇富科技",
        "c": "news",
        "range": "all",
        "size": "10",
        "page": str(i)
    }

    res=requests.post(url,headers=headers,data=datas)
    res.encoding="utf-8"
    content=res.text

    fw=open(f"{proName}list\\{i+50}.html","w",encoding="utf-8")
    fw.write(content)
    fw.close()
    print(i)
    time.sleep(2)