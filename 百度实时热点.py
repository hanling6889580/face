#unicode=utf-8
import urllib2
import urllib
import os
import re
from BeautifulSoup import BeautifulSoup

f=open(r'C:\Users\Administrator\Desktop\asd.txt','w')
url='http://top.baidu.com/?vit=1&fr=topbuzz_b1'
#def printHotNews(url):
content = urllib2.urlopen(url).read().decode('gbk','ignore').encode('utf-8')
pattern = re.compile('<li>.*?<span.*?>(.*?)</span>.*?<a.*?>(.*?)</a>.*?<span.*?>(.*?)</span>', re.S)
hotNews = re.findall(pattern, content)

for i in hotNews:
        print(i) 
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
bb=map(lambda x:x+','+'\n',hotNews)
for item in bb:  
        f.write(item)
f.close()
