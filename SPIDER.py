# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
import lxml.html
from lxml import etree

reload(__import__('sys')).setdefaultencoding('utf-8')

url="http://wenku.baidu.com/view/6ecf16e9998fcc22bcd10df5.html?from=search"
html=urllib2.urlopen(url).read().decode("gbk")
# tree=etree.HTML(html)
# print tree.xpath("//div[@id='reader-container-2']")
