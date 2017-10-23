# -*- coding: utf-8 -*-

import urllib2

import re
import time
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class GetAndStore:
    def __init__(self):
        pass

    #function
    def printHotNews(self,url,url2,url3):
        content = urllib2.urlopen(url).read().decode('UTF-8')
        pattern = re.compile('<li class="hd.*?<strong>.*?<a.*?>(.*?)</a>.*?strong>', re.S)
        News = re.findall(pattern, content)
        
        content2 = urllib2.urlopen(url2).read().decode('UTF-8')
        pattern2 = re.compile('<li>.*?<span class="s1.*?<a.*? target.*?>(.*?)</a>.*?', re.S)
        News2 = re.findall(pattern2, content2)

        content3 = urllib2.urlopen(url3).read().decode('gbk')
        pattern3 = re.compile('<li>.*?<a target="_blank".*?>(.*?)</a>.*?', re.S)
        News3 = re.findall(pattern3, content3)
        
        News.extend(News2)
        News.extend(News3)
        for i in News:
            

            print(i) 
        return News    
    #function can be reused
    def storeDB(self,table,news):
        #use dict store news
        news_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        news_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        #test insert only 1 record
        
        text = "'" + news[0] + "'"  #Chinese character and symbol
        time_now = "'" + news_time + "'"
        date = "'" + news_date + "'"
        text1 = "'" + news[1] + "'"
        text2 = "'" + news[2] + "'"
        text3 = "'" + news[3] + "'"
        text4 = "'" + news[4] + "'"
        text5 = "'" + news[5] + "'"
        text6 = "'" + news[6] + "'"
        text7 = "'" + news[7] + "'"
        text8 = "'" + news[8] + "'"
        text9 = "'" + news[9] + "'"
        text10 = "'" + news[10] + "'"
        text11 = "'" + news[11] + "'"
        text12 = "'" + news[12] + "'"
        text13 = "'" + news[13] + "'"
        text14 = "'" + news[14] + "'"
        text15 = "'" + news[15] + "'"
        text16 = "'" + news[16] + "'"
        text17 = "'" + news[17] + "'"
        text18 = "'" + news[18] + "'"
        text19 = "'" + news[19] + "'"
        text20 = "'" + news[20] + "'"
        text21 = "'" + news[21] + "'"
        text22 = "'" + news[22] + "'"
        text23 = "'" + news[23] + "'"
        text24 = "'" + news[24] + "'"
        
        #connect mysqlDB
        conn = pymysql.connect(
            host='192.168.0.211', 
            port=3306, 
            user='root', 
            passwd='root', 
            db='test',
            use_unicode=1,
            charset='utf8')

        try:
            with conn.cursor() as cursor:
                #create a table
                sql = """CREATE TABLE IF NOT EXISTS %s (
                            text  VARCHAR(200),
                            time  VARCHAR(200),
                            date VARCHAR(200))""" % (table,)
                cursor.execute(sql)
                # Create a new record
                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text1, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text2, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text3, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text4, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text5, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text6, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text7, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text8, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text9, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text10, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text11, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text12, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text13, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text14, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text15, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text16, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text17, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text18, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text19, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text20, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text21, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text22, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text23, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text24, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

                


                

            with conn.cursor() as cursor:
                # Read all records
                sql = "SELECT * FROM (%s) " %(table,)
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
                cursor.close()
        finally:
            conn.close()


if __name__ == "__main__":    
    #variable
    url = 'http://news.baidu.com/'
    url2 = 'http://top.sogou.com/'
    url3 = 'http://top.baidu.com/?vit=1&fr=topbuzz_b1'
    instance1 = GetAndStore()  #create an instance

    try:
        response = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        # http error
        print('Error code: ', e.code)
    except urllib2.HTTPError as e:
        # url error
        print('Reason: ', e.reason)
    else:
        # excute function
        instance1.printHotNews(url,url2,url3)
        instance1.storeDB("table13", instance1.printHotNews(url,url2,url3))
