# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
reload(__import__('sys')).setdefaultencoding('utf-8')

#links生成一致，标题 h1，后文不完整


class spider():
    def __init__(self):
        print '开始爬取......'

    def getsource(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'}
        req = urllib2.Request(url, headers=headers)
        html = urllib2.urlopen(req).read()
        return html

    def creatlinks(self,source,url):
        links=[]
        parts=re.findall('<a style="" href="(.*?)">',source,re.S)
        for each in parts:
            links.append(url+each)
        return links

    def extra(self,context):
        name=re.findall("<h1>(.*?)</h1>",context,re.S)

        #con=re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br/>',context,re.S)

        con1 = re.findall('<div id="content">(.*?)<script', context, re.S)
        con2 = re.sub('<script', '<br/>', con1[0])
        contex = con2 + '<br/>'
        con = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br/>', contex, re.S)

        contextlist=name+con
        return contextlist


spider=spider()
url='http://www.xbiquge.com/2_2762/'
source=spider.getsource(url)
links=spider.creatlinks(source,url)

f=open('hi.txt','a+')
for link in links:
    context=spider.getsource(link)
    contextlist=spider.extra(context)
    for ev in contextlist:
        final = '\t' + ev + '\n'
        f.writelines(final)
    f.writelines('\n\n')
f.close()


