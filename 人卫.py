import urllib2
import urllib
import os
import re
from BeautifulSoup import BeautifulSoup
def getAllImageLink():

    html = urllib2.urlopen('http://top.baidu.com/?vit=1&fr=topboards').read().decode('utf-8')
    soup = BeautifulSoup(html)
    liResult = soup.findAll('li')
    print liResult

getAllImageLink()


url = 'http://news.baidu.com/'
content = urllib2.urlopen(url).read().decode('gbk')

#Example：
#<li class="hdline0">
#<i class="dot"></i>
#<strong>
#<a href="http://china.huanqiu.com/article/2016-07/9209287.html?from=bdwz " target="_blank" class="a3" mon="ct=1&amp;a=1&amp;c=top&amp;pn=0">xxx：扶贫工作不搞层层加码</a>
#</strong>
#</li>

pattern = re.compile('<li class="hd.*?<strong>.*?<a.*?>(.*?)</a>.*?strong>', re.S)
hotNews = re.findall(pattern, content)

for i in hotNews:
  print(i)

