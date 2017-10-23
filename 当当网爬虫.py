import urllib2
import re
import time
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url='http://category.dangdang.com/cp01.56.00.00.00.00.html?search_category=1'
url3='http://top.baidu.com/?vit=1&fr=topbuzz_b1'
content3 = urllib2.urlopen(url3).read().decode('gbk')
pattern3 = re.compile('<span class.*?</span>', re.S)
News3 = re.findall(pattern3, content3)


content = urllib2.urlopen(url).read().decode('gbk')
pattern = re.compile('<em></em>*?</a>', re.I)
News = re.findall(pattern, content)
f=open('D:\\wind\\ss.txt','w')

for i in News:
    f.write(i)

f.close()

