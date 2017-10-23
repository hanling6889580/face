
import urllib2,re  
from bs4 import BeautifulSoup  
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')  
url="http://www.weather.com.cn/weather/101280601.shtml"  
def getHtml(url):  
    try:  
        print url  
        html = urllib2.urlopen(url).read()#.decode('utf-8')#½âÂëÎªutf-8  
    except:  
        return  
    return html  
def getWeatherReport(html):  
    if not html:  
        print 'nothing can be found'  
        return  
    soup=BeautifulSoup(html,'lxml')  
    try:  
        items=soup.find("ul",{"class":"t clearfix"})  
        result = re.sub(re.compile('\n+'),"\n",str(items.text))  
        print result  
    except:  
        print "something was wrong"  
        return  
    return result  
html=getHtml(url)  
getWeatherReport(html)  
