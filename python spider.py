# -*- coding:utf-8 -*-
from urllib import urlretrieve
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
reload(__import__('sys')).setdefaultencoding('utf-8')

# save images
# urlretrieve('http://www.baidu.com/img/baidu_jgylogo3.gif','logo.jpg')

url='http://www.pythonscraping.com/pages/warandpeace.html'
# print urlopen(url).read()

#findAll(tag,attr,recursive,text,limits,keywords)

# 任务的对话时红色的，名字是绿色的
html=urlopen(url)
bsobj=BeautifulSoup(html,"lxml")
namelists=bsobj.findAll("span",{"class":"green"})
# for name in namelists:
#     print name
#     print len(name.attrs)
#     print type(name.attrs)
#     print name.get_text()





# dialogue=bsobj.findAll("span",{"class":"red"})
# for each in dialogue:
#     print each.get_text()

#查找网页中内容包含 the prince 的标签数量
# namelists=bsobj.findAll(text="the prince")
# print len(namelists)

#。findAll函数的recursive是一个布尔变量，默认为TRUE，表示在查找过程中递归多层


##导航树
url="http://www.pythonscraping.com/pages/page3.html"
html=urlopen(url)
bsobj=BeautifulSoup(html,"lxml")
#打印giftlist表格所有产品的数据行，子标签
# for child in bsobj.find("table",{"id":"giftList"}).children:
#     print child

#处理兄弟标签，不会获取本身，只有本身之后的数据标签，
# for sibling in bsobj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print sibling

#父标签
# print bsobj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()

#正则表达式和Beautiful结合
# images=bsobj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
# for image in images:
#     print image['src'] #[]运算表示从标签中取得属性的值

#lambda表达式,传入参数为标签tag，然后返回值是布尔值，如此进行筛选
# bsobj.findAll(lambda tag:len(tag.attrs)==2)




#开始采集
# url='http://en.wikipedia.org/wiki/Kevin_Bacon'
# bsobj=BeautifulSoup(urlopen(url),"lxml")
# for link in bsobj.findAll("a"):
#     if 'href' in link.attrs:
#         print link.attrs['href']

#进行所需要网址的筛选,三个特点，他们都在id是bodyContent的div标签中,URL连接不包含分号，URL连接都以/wiki/开头
# links=bsobj.find("div",{"id":"bodyContent"}).findAll("a",{"href":re.compile("^(/wiki/)((?!:).)*$")})
# for link in links:
#     if 'href' in link.attrs:
#         print link.attrs['href']

#链接去重
# pages=set()
# def getlinks(pageurl):
#     global pages
#     html=urlopen("http://en.wikipedia.org"+pageurl)
#     bsobj=BeautifulSoup(html,"lxml")
#     for link in bsobj.findAll("a",href=re.compile("^(/wiki/)")):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 new=link.attrs['href']
#                 pages.add(new)
#                 getlinks(new)
# getlinks("")


#收集整个网站的数据
pages=set()
def getlinks(pageurl)
    global pages
    html=urlopen('http://en.wikipedia.org'+pageurl)
    bsobj=BeautifulSoup(html)
    try:
        print bsobj.h1.get_text()
        print bsobj.find("",{"id":"mw-content-text"}).findAll("p")[0]
        print bsobj.find(id="ca-edit").find("span").find("a").attrs['href']
    except AttributeError:
        print "页面缺少一些信息"

    for link in bsobj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link:
            if link.attrs['href'] not in pages:
                newpage=link.attrs['href']
                pages.add(newpage)
                getlinks(newpage)
