import requests
import re
import urllib
http_head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}

def music_search(tget_strs,tget_head):
    tget_urls='https://www.ximalaya.com/yinyue/'+tget_strs
    tget_html=requests.get(tget_urls,headers=tget_head)
    tget_html.encoding=tget_html.apparent_encoding
    return tget_html

def music_albums(gals_html):
    gals_text=re.findall(r'"albumId":(.*?),',(gals_html).text)
    gals_urlt=[]
    for x in (gals_text[:1]):
        gals_urls='https://www.ximalaya.com/revision/play/album?albumId='+x
        gals_htms=requests.get(gals_urls,headers=http_head)
        gals_urlt=(re.findall(r'"src":"(.*?)"',(gals_htms).text))
    return gals_urlt

def music_gettit(getf_html):
    getf_name=re.findall(r'"title":"(.*?)"',(getf_html).text)
    return getf_name

def music_downlo(urlt,title):
    n=0
    for y in urlt:
        print(n+1,"----"+str(title[n]))
        n = n + 1
    n=int(input("请输入下载编号："))
    try:
        print("正在下载："+str(title[n]))
        urllib.request.urlretrieve(urlt[n],str(title[n]+'.m4a'))
        print("下载成功："+str(title[n]))
    except:
        print("下载失败："+str(title[n]))
    return 0;
