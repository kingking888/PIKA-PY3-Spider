import os
import sys
def main_menu():
    os.system('cls')
    print("")
    print("-------喜马拉雅FM音乐下载工具--------")
    print("-          1~歌曲类型             -")
    print("-          2~歌单编号             -")
    print("-          3~查找名称             -")
    print("-          0~退出下载             -")
    print("----------------------------------")
    selt = int(input("请选择对应的下载方式："))
    while 1:
        if selt == 1:
            gqmc=main_gqzl()
            break
        elif selt == 2:
            gqmc=input("请输入对应的歌单编号：")
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

def main_gqzl():
    print("----------~~~请选择歌曲类型~~~~--------")
    print("- 00~全部  10~嘻哈  20~雷鬼  30~纯音  -")
    print("- 01~流行  11~电音  21~动漫  31~翻唱  -")
    print("- 02~摇滚  12~后摇  22~影视  32~影视  -")
    print("- 03~民谣  13~现代  23~朋克  33~欧美  -")
    print("- 04~轻纯  14~民乐  24~舞台  34~催眠  -")
    print("- 05~古风  15~声乐  25~儿歌  35~游戏  -")
    print("- 06~爵士  16~拉丁  26~实验  36~日韩  -")
    print("- 07~蓝调  17~金属  27~喜剧  37~电子  -")
    print("- 08~乡村  18~独立  28~视频  38~铃声  -")
    print("- 09~古典  19~灵魂  29~老歌  39~原创  -")
    print("-----------请输入数字选择类型-----------")
    zllb=["","liuxing","yaogun","minyao","qingyinyue","gufeng","jueshi","landiao","xiangcun","gudian",
          "xiha","dianyin","houyao","xinshiji","minyue","shengyue","lading","jinshu","duli","linghun",
          "leigui","anime","yingshiyuansheng","punk","wutai","erge","shiyanyinyue","xiju","reci820","reci117",
          "reci310","reci125","reci121","reci507","reci322","reci119","reci506","reci328","reci130","reci320"]
    xzlx=int(input("请选择对应的歌曲类型："))
    if xzlx<0 or xzlx>39 : return zllb[0]
    else : return zllb[xzlx]