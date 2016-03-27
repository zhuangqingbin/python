#ecoding:utf8
import sys
import urllib2
import urllib
import re
import zlib


def getsource(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'}
    req = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(req).read()
    return html


def creatlinks(source, url):
    links = []
    parts = re.findall('<a style="" href="(.*?)">', source, re.S)
    for each in parts:
        links.append(url + each)
    return links


def extra(context):
    name = re.findall("<h1>(.*?)</h1>", context, re.S)

    # con = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br/>', context, re.S)



    contextlist = name + con
    return contextlist

url='http://www.xbiquge.com/2_2762/8494690.html'
context=getsource(url)
# conlist=extra(context)
# f=open('nov.txt','a+')
# for ev in conlist:
#     final = '\t' + ev+'\n'
#     f.writelines(final)
# f.close()
name = re.findall("<h1>(.*?)</h1>", context, re.S)
con1 = re.findall('<div id="content">(.*?)<script',context,re.S)
con2 =re.sub('<script','<br/>',con1[0])
contex=con2+'<br/>'
con = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br/>', contex, re.S)
contextlist = name + con
f=open('novrrrr.txt','a+')
for ev in contextlist:
     final = '\t' + ev+'\n'
     f.writelines(final)
f.close()