# -*- coding:utf-8 -*-
import requests
import re
#使打印的内容是中文
reload(__import__('sys')).setdefaultencoding('utf-8')


def changeurl(start_url,page):  #传参数(开始的url，页数)
    urls=[]
    for i in range(1,page+1):
        url=start_url+str(i)
        urls.append(url)
    return urls

def getHtml(url):
    #构造头部
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
    #用requests获得网页
    gethtml=requests.get(url,headers=headers)
    return gethtml.text
#打开（wangyuan.txt,'w+'方式写入）
f=open('wangyuan.txt','w+')
#开始的url
start_url="http://tieba.baidu.com/p/3826846894?see_lz=1&pn="
#所有连接调用changurl()构成
all_link=changeurl(start_url,3)
#遍历每个连接
for link in all_link:
    #网页源码调用getHtml(传入连接)
    Yuanma=getHtml(link)
    #所有内容用正则到百度贴吧的每一个楼层抓取
    neirongs=re.findall('<div id="post_content_.*?" class="d_post_content .*?">            (.*?)</div>',Yuanma,re.S)
    #遍历每一个楼层内容
    for neirong in neirongs:
        #对抓到内容再处理
        neirong=neirong.replace('<br>','')
        neirong=neirong.replace('<img class="BDE_Image" pic_type="0" width="560" height="395" src="http://imgsrc.baidu.com/forum/w%3D580/sign=b03b9d4da5ec08fa260013af69ef3d4d/77a6ef345982b2b7979a003634adcbef77099b19.jpg" pic_ext="jpeg"  ><img class="BDE_Image" pic_type="0" width="560" height="150" src="http://imgsrc.baidu.com/forum/w%3D580/sign=24f197924ac2d562f208d0e5d71390f3/2e3e9300baa1cd11ef424bd2bc12c8fcc1ce2daa.jpg" pic_ext="jpeg"  >','')
        neirong=re.sub('<a href=.*?</a>',"",neirong,re.S)
        f.write(neirong)
#关闭文件
f.close()