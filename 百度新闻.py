# -*- coding: cp936-*-
import urllib2
import urllib
import os
import re
from BeautifulSoup import BeautifulSoup
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')



f=open(r'C:\Users\Administrator\Desktop\asd.txt','w')
url='http://news.baidu.com/'
#def printHotNews(url):
content = urllib2.urlopen(url).read().decode('utf-8')
pattern = re.compile('<li class="hd.*?<strong>.*?<a.*?>(.*?)</a>.*?strong>', re.S)
hotNews = re.findall(pattern, content)
for i in hotNews:
        print(i) 



import sys
reload(sys)
sys.setdefaultencoding('utf-8')
bb=map(lambda x:x+'\n',hotNews)
for item in bb:  
        f.write(item)
f.close()

#url='http://top.baidu.com/?vit=1&fr=topbuzz_b1_c513'

#printHotNews(url)


#'<li class="hd.*?<strong>.*?<a.*?>(.*?)</a>.*?strong>'
#'<li>.*?<span.*?>(.*?)</span>.*?<a.*?>(.*?)</a>.*?<span.*?>(.*?)</span>'
