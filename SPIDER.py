#ecoding:utf8
import sys
import urllib2
import urllib
import re
import zlib

url='https://mail.qq.com/'
data=urllib.urlencode({'u':'360650538@qq.com','p':'zqb13645979670'})
# req=urllib2.Request(url,data)
req=urllib2.Request(url)
html=urllib2.urlopen(req).read()
print html.decode('gbk').encode('utf-8')

# request = urllib2.Request(url)
# request.add_header('Accept-encoding', 'gzip')
# opener = urllib2.build_opener()
# response = opener.open(request)
# html = response.read()
# gzipped = response.headers.get('Content-Encoding')
# if gzipped:
#     html = zlib.decompress(html, 16+zlib.MAX_WBITS)
# print html