# -*- coding: utf-8 -*-
#在Unix 直接用
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

article = open('D:\基础软件\protobuf\hamuleite.txt', "r").readlines()

f=open('D:\基础软件\protobuf\asd.txt',"w")

for x in words:
    b=jieba.lcut(article, cut_all = False)
    c=( " ".join(b))
    f.write(c)


    
f.close()
