#-*- coding:utf-8 -*-
#from finder import FIND
import urllib2
from bs4 import BeautifulSoup as bs
import bs4
from time import sleep
import sys
from pylsy import pylsytable
reload(sys)
sys.setdefaultencoding('utf-8')
data=[]
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
t6 = []
t7 = []
t8 = []
t9 = []
t10 = []
c=0
ret=urllib2.urlopen('http://top.sogou.com/')
#print ret.read()
soup=bs(ret.read(),'lxml')
#print soup.find_all('p',class_='p2')[1:]
for i in soup.select('span'):
    if i.contents:
        print i.get('class'),i.contents
if i.get('class')[0]=='num' or i.get('class')[0]=='hot-num':
    pass
#print i.contents[0]
for i in soup.select('a'):
    if i.get('href').bs.find('query')>0 and type(i.contents[0]) is bs4.element.NavigableString:
        data.append(i.contents[0])
for i in range(1,11):
    for value in data[1+10*c:(1+10*c)+10]:
        if i==1:
            t1.append(value)
        elif i==2:
            t2.append(value)
        elif i==3:
            t3.append(value)
        elif i==4:
            t4.append(value)
        elif i==5:
            t5.append(value)
        elif i==6:
            t6.append(value)
        elif i==7:
            t7.append(value)
        elif i==8:
            t8.append(value)
        elif i==9:
            t9.append(value)
        elif i==10:
            t10.append(value)
#print value.encode('utf-8')
c+=1
#bs4.element.NavigableString
title = [u"实时热点", u"热门电影", u"热门电视剧", u'热门综艺', u'热门动漫', u'热门小说', u'热门游戏', u'热门音乐', u'热门汽车', u'热门人物']
table = pylsytable(title)
table.add_data(u'实时热点',t1)
table.add_data(u"热门电影",t2)
table.add_data(u"热门电视剧",t3)
table.add_data(u"热门综艺",t4)
table.add_data(u"热门动漫",t5)
table.add_data(u"热门小说",t6)
table.add_data(u"热门游戏",t7)
table.add_data(u"热门音乐",t8)
table.add_data(u"热门汽车",t9)
table.add_data(u"热门人物",t10)
table._create_table()
print table
