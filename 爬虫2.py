import urllib2
import urllib
import os
from BeautifulSoup import BeautifulSoup
def getAllImageLink():

    html = urllib2.urlopen('http://top.baidu.com/?vit=1&fr=topbuzz_b1_c513').read()
    soup = BeautifulSoup(html)
    liResult = soup.findAll('<li>.*?<span.*?>(.*?)</span>.*?<a.*?>(.*?)</a>.*?<span.*?>(.*?)</span>')
    print liResult #∑Ω±„µ˜ ‘

    count = 0;
    for image in liResult:
        count += 1
        link = image.get('src')
        imageName = count
        filesavepath = 'C:\Users\Administrator\Desktop\¡Ÿ ±\%s.jpg' % imageName
        urllib.urlretrieve(link,filesavepath)
        print filesavepath 
if __name__ == '__main__':
    getAllImageLink()
#url='http://top.baidu.com/?vit=1&fr=topbuzz_b1_c513'
#http://xiaoxia.org/2012/11/02/python-cralwer/
