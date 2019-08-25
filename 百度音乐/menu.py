import os
import sys
from pget import spname,gsname
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
            gqmc=input("请输入对应的歌手名字：")
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