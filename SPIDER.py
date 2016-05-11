# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
import lxml.html
from lxml import etree
from bs4 import BeautifulSoup

url='http://m.weibo.cn'
html=urllib2.urlopen(url)
soup=BeautifulSoup(html,"lxml")
lists=soup("p")
for list in lists:
    print list.get_text()
