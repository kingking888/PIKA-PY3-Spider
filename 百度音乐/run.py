import requests
import re
import os
import sys
def main_menu():
    os.system('cls')
    print("")
    print("----------百度音乐下载工具-----------")
    print("-          1~查找歌曲             -")
    print("-          2~下载视频             -")
    print("-          0~退出下载             -")
    print("----------------------------------")
    selt = int(input("请选择对应的下载方式："))
    while 1:
        if selt == 1:
            gqmc=input("请输入对应的搜索词语：")
            gsname(gqmc)
            break
        elif selt == 2:
            gqmc=input("请输入对应的视频编号：")
            print("正在下载视频："+gqmc)
            spname(gqmc)
            print("成功下载视频：" + gqmc)
            break
        elif selt == 3:
            gqmc=""
            break
        elif selt == 0:
            sys.exit(1)
            break
        else:
            selt = int(input("输入有误，请重新输入："))
    return gqmc
def spname(spid):
    url='http://music.baidu.com/playmv/'+spid
    s=requests.session()
    headers={'referer':'http://music.baidu.com/mv',
             'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
             }

    r=s.get(url,headers=headers)
    a=r.content.decode('UTF-8')

    file_mp4=a.split('data.push')[1].split('file_link":"')[1].replace('"});','').replace(r"\\",r'').replace('\/','/').replace("\n",'').strip()

    get_file=s.get(file_mp4)
    mp4_name=spid+'.mp4'
    f=open(mp4_name,'wb')
    f.write(get_file.content)
    f.close()

def gsname(gamz):
# 搜索歌曲
    data = {'key': gamz}
    search_url = 'http://music.taihe.com/search'
# 发送http请求
    search_responset = requests.get(search_url, params=data)
# 设置编码属性
    search_responset.encoding = 'utf-8'
    search_html = search_responset.text
    song_ids = re.findall(r'sid&quot;:(\d+),', search_html)
    song_api = 'http://play.taihe.com/data/music/songlink'
    data = {'songIds': ','.join(song_ids), 'hq': 0, 'type': 'mp3', 'pt': 0, 'flag': 1, 's2p': 650, 'prerate': 128,
        'bwt': 266, 'dur': 231000, 'bat': 266, 'bp': 100, 'pos': 65833, 'auto': 0}
# 发送请求
    song_response = requests.post(song_api, data=data)
# 将返回来的数据转换为字典
    song_info = song_response.json()
    song_info = song_info['data']['songList']
# 遍历下载
    for song in song_info:
        song_name=song['songName']
        with open('%s.mp3' % song_name, 'wb')as f:
            print("成功下载："+gamz+"-"+song_name)
            response = requests.get(song['songLink'])
            f.write(response.content)
main_menu()