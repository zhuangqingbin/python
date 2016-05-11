# -*- coding: cp936 -*-
#author:雪之忆
#---------------------

import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re
import time
import httplib
import Cookie
def readtxt(path):
    url=[]
    with open(path,'r') as txt:
        url=txt.readlines()
    return url
'''登陆网页，读取网页'''
hosturl='http://www.cnki.net/'
#生成cookie
httplib.HTTPConnection.debuglevel = 1
cookie = cookielib.CookieJar()

#创建一个新的opener来使用cookiejar
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie),urllib2.HTTPHandler)
#post地址
posturl='http://epub.cnki.net/kns/brief/result.aspx?dbprefix=scdb&action=scdbsearch&db_opt=SCDB'
#构建头结构，模拟浏览器
headers={'Connection':'Keep-Alive',
         'Accept':'text/html,*/*',
         'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36',
         'Referer':posturl}
#通过chorme抓包获取postdata

#传入股票的名称，返回源代码
#知网的参数编码是UTF8编码，所以中文需要先gbk解码再进行utf-8编码
def get(str,date1,date2):
    DbCatalog='中国学术文献网络出版总库'.decode('gbk').encode('utf8')
    magazine='上海证券报+中国证券报+证券日报+证券时报+中国经营报+21世纪经济报道+经济观察报+第一财经日报'.decode('gbk').encode('utf8')
    txt=str.decode('gbk').encode('utf8')
    times=time.strftime('%a %b %d %Y %H:%M:%S')+' GMT+0800 (中国标准时间)'
    parameters={'ua':'1.21',
            'PageName':'ASP.brief_result_aspx',
            'DbPrefix':'CCND',
            'DbCatalog':DbCatalog,
            'ConfigFile':'CCND.xml',
            'db_opt':'CJFQ,CJFN,CDFD,CMFD,CPFD,IPFD,CCND,CCJD,HBRD',
            'base_special1':'%',
            'magazine_value1':magazine,
            'magazine_special1':'%',
            'txt_1_sel':'SU',
            'txt_1_value1':txt,
            'txt_1_relation':'#CNKI_AND',
            'txt_1_special1':'=',
            'his':'0',
            'publishdate_from':date1,
            'publishdate_to':date2,
            '__': times
            }
    postdata=urllib.urlencode(parameters)

    query_string=urllib.urlencode({'pagename':'ASP.brief_result_aspx','DbCatalog':'中国学术文献网络出版总库',
                               'ConfigFile':'SCDB.xml','research':'off','t':int(time.time()),
                               'keyValue':'特力A','dbPrefix':'CCND',
                               'S':'1','spfield':'SU'
                               })

    url='http://epub.cnki.net/KNS/request/SearchHandler.ashx?action=&NaviCode=*&'
    url2='http://epub.cnki.net/kns/brief/brief.aspx?'

    req=urllib2.Request(url+postdata,headers=headers)
    html=opener.open(req).read()

    req2=urllib2.Request(url2+query_string,headers=headers)
    result2 = opener.open(req2)
    html2=result2.read()
    return html2

#传入网页的源代码，返回搜索的返回结果数目
def find(content):
    l = re.search("nbsp;.*?nbsp;(.*?)&nbsp", content).group(1)
    return l



# h=get('苏宁云商','2015-1-1','2015-2-1')
# l=find(h)
# print l


#读取所有2000多只股票形成tests列表
tests=[]
f=open("stock.txt","r")
for i in range(1,2141):
    html1=f.readline().decode('utf8').encode('gbk')
    html=re.sub('\n','',html1)
    tests.append(html)
f.close()
# for each in tests:
#     print each.decode('utf8').encode('gbk')
#生成每只股票和它的出现次数的字典
# tests=['美年健康','爱尔眼科']

# for each in tests:
#     print each.decode('gbk').encode('utf8')
time1=time.time()
dict=dict()
datelist=['2015-1-1','2015-2-1','2015-3-1','2015-4-1','2015-5-1','2015-6-1','2015-7-1','2015-8-1','2015-9-1','2015-10-1','2015-11-1','2015-12-1','2016-1-1']
for test in tests:
    list=[]
    for i in range(12):
        con=get(test,datelist[i],datelist[i+1])
        num=find(con)
        list.append(num)
    dict[test]=list


# 将字典写入txt文本中
f1=open("cnki1.txt","a")
for test in tests:
    test1=test.decode('gbk').encode('utf8')
    f1.writelines(test1+","+dict[test][0]+","+dict[test][1]+","+dict[test][2]+","+dict[test][3]+","+dict[test][4]+","+dict[test][5]+","+dict[test][6]+","+dict[test][7]+","+dict[test][8]+","+dict[test][9]+","+dict[test][10]+","+dict[test][11]+"\n")
f1.close()

time2=time.time()
print time2-time1