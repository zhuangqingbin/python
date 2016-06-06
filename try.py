#coding:utf8
import re
import urllib2
from bs4 import BeautifulSoup
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

headers = {
    'User - Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
}
def creaturl(stock,page):
    t = 'http://www.iwencai.com/search?typed=1&preParams=tid%253Dreport%2526tr%253D0%2526ft%253D1%2526st%253D0&ts=1&f=1&qs=result_rewrite&selfsectsn=&querytype=&bgid=&sdate=&edate=&searchfilter=&tid=report&w='
    l=t+stock+'&p='+str(page)
    return l


def get(stock):
    list=[]
    for i in range(1,11):
        url=creaturl(stock,i)
        rep=urllib2.Request(url,headers=headers)
        html = urllib2.urlopen(rep)
        soup = BeautifulSoup(html, "lxml")
        li = soup.findAll("p", {"class": "s_r_attr"})
        for each in li:
            list.append(each.get_text()[1:11])
    return list

tests=[]
f=open("stock.txt","r")
for i in range(1,2141):
    html1=f.readline()
    html=re.sub('\n','',html1)
    tests.append(html)
f.close()








time1=time.time()
dict=dict()
for t in tests[2000:2140]:
    dict[t]=get(t)



# dict={'a':[1,5],'b':[2,2,4,5]}
f1=open("1900-2000.txt","a")
for key in dict:
    f1.write(key)
    for l in range(len(dict[key])):
        f1.write(",")
        f1.write(str(dict[key][l]))
    f1.write("\n")
f1.close()

time2=time.time()
print (time2-time1)/60