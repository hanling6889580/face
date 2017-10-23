import urllib
import urllib2
import re
import tool
import os
 
#ץȡMM
class Spider:
 
    #ҳ���ʼ��
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
        self.tool = tool.Tool()
 
    #��ȡ����ҳ�������
    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')
 
    #��ȡ������������MM����Ϣ��list��ʽ
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            contents.append([item[0],item[1],item[2],item[3],item[4]])
        return contents
 
    #��ȡMM��������ҳ��
    def getDetailPage(self,infoURL):
        response = urllib2.urlopen(infoURL)
        return response.read().decode('gbk')
 
    #��ȡ�������ּ��
    def getBrief(self,page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        result = re.search(pattern,page)
        return self.tool.replace(result.group(1))
 
    #��ȡҳ������ͼƬ
    def getAllImg(self,page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        #������Ϣҳ�����д���
        content = re.search(pattern,page)
        #�Ӵ�������ȡͼƬ
        patternImg = re.compile('<img.*?src="(.*?)"',re.S)
        images = re.findall(patternImg,content.group(1))
        return images
 
    #�������д��ͼƬ
    def saveImgs(self,images,name):
        number = 1
        print u"����",name,u"����",len(images),u"����Ƭ"
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            fileName = name + "/" + str(number) + "." + fTail
            self.saveImg(imageURL,fileName)
            number += 1
 
    # ����ͷ��
    def saveIcon(self,iconURL,name):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = name + "/icon." + fTail
        self.saveImg(iconURL,fileName)
 
    #������˼��
    def saveBrief(self,content,name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName,"w+")
        print u"����͵͵�������ĸ�����ϢΪ",fileName
        f.write(content.encode('utf-8'))
 
    #����ͼƬ��ַ���ļ��������浥��ͼƬ
    def saveImg(self,imageURL,fileName):
         u = urllib.urlopen(imageURL)
         data = u.read()
         f = open(fileName, 'wb')
         f.write(data)
         print u"�������ı�������һ��ͼƬΪ",fileName
         f.close()
 
    #������Ŀ¼
    def mkdir(self,path):
        path = path.strip()
        # �ж�·���Ƿ����
        # ����     True
        # ������   False
        isExists=os.path.exists(path)
        # �жϽ��
        if not isExists:
            # ����������򴴽�Ŀ¼
            print u"͵͵�½������ֽ���",path,u'���ļ���'
            # ����Ŀ¼��������
            os.makedirs(path)
            return True
        else:
            # ���Ŀ¼�����򲻴���������ʾĿ¼�Ѵ���
            print u"��Ϊ",path,'���ļ����Ѿ������ɹ�'
            return False
 
    #��һҳ�Ա�MM����Ϣ��������
    def savePageInfo(self,pageIndex):
        #��ȡ��һҳ�Ա�MM�б�
        contents = self.getContents(pageIndex)
        for item in contents:
            #item[0]��������URL,item[1]ͷ��URL,item[2]����,item[3]����,item[4]��ס��
            print u"����һλģ��,���ֽ�",item[2],u"����",item[3],u",����",item[4]
            print u"����͵͵�ر���",item[2],"����Ϣ"
            print u"������ط������ĸ��˵�ַ��",item[0]
            #��������ҳ���URL
            detailURL = item[0]
            #�õ���������ҳ�����
            detailPage = self.getDetailPage(detailURL)
            #��ȡ���˼��
            brief = self.getBrief(detailPage)
            #��ȡ����ͼƬ�б�
            images = self.getAllImg(detailPage)
            self.mkdir(item[2])
            #������˼��
            self.saveBrief(brief,item[2])
            #����ͷ��
            self.saveIcon(item[1],item[2])
            #����ͼƬ
            self.saveImgs(images,item[2])
 
    #������ֹҳ�룬��ȡMMͼƬ
    def savePagesInfo(self,start,end):
        for i in range(start,end+1):
            print u"����͵͵Ѱ�ҵ�",i,u"���ط�������MM���ڲ���"
            self.savePageInfo(i)
 
#������ֹҳ�뼴�ɣ��ڴ˴�����2,10,��ʾץȡ��2��10ҳ��MM
spider = Spider()
spider.savePagesInfo(2,10)
