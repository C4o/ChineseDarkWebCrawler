#coding=utf-8
#Created by Cao

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sqlite3, sys, logging, time, os, re, urllib
import win32api, win32clipboard, win32con
from ctypes import *
import shutil
import hashlib

reload(sys)
sys.setdefaultencoding('utf-8')

def get_image(browser):
    elements = browser.find_elements_by_xpath("//dt[@class='attach-image']/img")
    for element in elements:
        url = element.get_attribute("src")
        file_id = url.split("?id=")[1].split("&amp;sid")[0].split("&")[0]
        file = open('image_id.txt', 'a+')
        file.write(file_id+'\n')
        file.close()

def get_links(index_url , pagenum, browser):
    topic = []
    for i in range(1 , pagenum+1 , 1):
        if i == 1:
            page_url = index_url
        else:
            page_url = index_url + '&start=' + str(30*(i-1))
        browser.get(page_url)
        topic_links = browser.find_elements_by_class_name('topictitle')
        for topic_link in topic_links:
            topic.append(topic_link.get_attribute('href'))
    return topic

def get_content_insert(topic , crawl_time, browser, catagroy):
    table_name = 'DrakWeb_' + catagroy
    content = dict([])
    for top in topic:
        try:
            try:
                conn = sqlite3.connect('C:\\Users\\Administrator\\Desktop\\darkweb\\db.sqlite3')
                cursor = conn.cursor()
            except Exception,e:
                print e
                pass
            browser.get(top)
            topic_post_time = browser.find_element_by_xpath("//table[@class='v_table_1']/tbody/tr[3]/td[6]").text
            topic_post_username = browser.find_element_by_xpath("//span[@class='responsive-hide']/strong/span").text
            topic_title = browser.find_element_by_xpath("//h2[@class='topic-title']/a").text
            topic_sales_nums = browser.find_element_by_xpath("//table[@class='v_table_1']/tbody/tr[9]/td[2]").text
            topic_deal_nums = browser.find_element_by_xpath("//table[@class='v_table_1']/tbody/tr[7]/td[4]").text
            topic_price_dollar = browser.find_element_by_xpath("//table[@class='v_table_1']/tbody/tr[5]/td[4]").text
            topic_sales_status = browser.find_element_by_xpath("//table[@class='v_table_1']/tbody/tr[7]/td[2]").text
            topic_id = top.split("&")[1].split("=")[1]
            content['topic_post_time'] = str(topic_post_time).decode('utf-8')
            content['topic_post_username'] = str(topic_post_username).decode('utf-8')
            content['topic_title'] = str(topic_title).decode('utf-8')
            content['topic_sales_nums'] = str(topic_sales_nums).decode('utf-8')
            content['topic_deal_nums'] = str(topic_deal_nums).decode('utf-8')
            content['topic_price_dollar'] = str(topic_price_dollar).decode('utf-8')
            content['topic_sales_status'] = str(topic_sales_status).decode('utf-8')
            content['topic_id'] = hashlib.md5(content['topic_post_username']+content['topic_title']+content['topic_post_time']).hexdigest()
        except:
            pass
        #计算行数
        line_num = len(cursor.execute('''SELECT * FROM '''+table_name).fetchall())
        #测试是否重复
        print content['topic_id']
        sql1 = '''SELECT ID FROM %s where Topic_id="%s"''' % (table_name, content['topic_id'])
        print sql1
        if len(cursor.execute(sql1).fetchall())>0:
            try:
                cursor.execute('''UPDATE %s SET Deal_divide_sales="%s" , Topic_price_dollar="%s" , Topic_sales_status="%s" , Crwal_time="%s" WHERE Topic_id="%s"''' % (table_name, str(content['topic_deal_nums']+'/'+content['topic_sales_nums']) ,  content['topic_price_dollar'] , content['topic_sales_status'] , str(crawl_time) , content['topic_id']))
            except Exception,e:
                print e
                pass
        else:
            try:
                sql2 = '''INSERT INTO %s (ID , Topic_id, Topic_post_username , Topic_title , Topic_post_time , Deal_divide_sales , Topic_price_dollar , Topic_sales_status , Crwal_time , Catagory)
                        VALUES (%d , "%s", "%s" , "%s" , "%s" , "%s" , "%s" , "%s" , "%s" , "%s")''' \
                       % (table_name, line_num+1 , content['topic_id'], content['topic_post_username'] , content['topic_title'] , content['topic_post_time'] , str(content['topic_deal_nums']+'/'+content['topic_sales_nums']) , content['topic_price_dollar'] , content['topic_sales_status'] , str(crawl_time), catagroy)
                cursor.execute(sql2)
                # 保存静态页面并写入
                html = browser.page_source
                get_image(browser)
                html = str(html)
                html = html.replace('./download/file.php?id=', '/static/topic_image/')
                html = re.sub(r'\&amp\;sid\=[0-9a-zA-Z]{32}', '.png', html)
                # 以帖子id来做唯一值
                filename = "../../static/"+str(content['topic_id'])+'.html'
                print "-------------"+filename
                file = open(filename, 'w')
                file.write(html)
                file.close()
                print 'insert test'
            except Exception,e:
                print e
                pass
        cursor.close()
        conn.commit()
        conn.close()

def DarkCrawler(num, catagroy, pages):
    try:
        fireFoxOptions = webdriver.FirefoxOptions()
        #headless模式无弹窗
        fireFoxOptions.set_headless()
        #设置tor为firefox源
        binary = FirefoxBinary('C:\\Tor\\Tor Browser\\Browser\\firefox.exe')
        browser = webdriver.Firefox(firefox_options=fireFoxOptions , firefox_binary=binary)
        # 模拟按键进行登录浏览
        browser.get('http://bmp3qqimv55xdznb.onion')
        time.sleep(10)
        browser.find_element_by_id('username').send_keys('username')# 要登录的用户名
        browser.find_element_by_id('password').send_keys('password')# 对应的密码
        browser.find_element_by_name("login").click()
        first_links = browser.find_elements_by_class_name('index_list_title')
        #找到卖数据情报的页面并收集所有的
        for link in first_links:
            href = link.get_attribute('href')
            if "viewforum.php?f="+str(num) in href:
                link.click()
                break
        index_url = browser.current_url
        topic = get_links(index_url , pages, browser)
        print 'test3'
        crawl_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        get_content_insert(topic , crawl_time, browser, catagroy)
        #关闭firefox、cursor、数据库连接，提交事务
        browser.close()
        browser.quit()
    except Exception,e:
        print e
        pass

if __name__ == '__main__':
    if len(sys.argv) == 3:
        catagroy = sys.argv[1]
        pages = sys.argv[2]
        list = {'sex':100, 'data':78, 'service':57, 'material':82, 'virtual_source':58, 'teach':84, 'cvv':59, 'other':37, 'basic':60, 'private':80}
        if catagroy in ['sex', 'data', 'service', 'material', 'virtual_source', 'teach', 'cvv', 'other', 'basic', 'private']:
            pages = int(pages)
            id = list[catagroy]
            DarkCrawler(id, catagroy, pages)
        else:
            print "your keyword must be in 'sex','data','service','material','virtual_source','teach','cvv','other','basic','private'"
    else:
        print "Example: python darkweb.py keyword 1"
        print "your keyword must be in 'sex','data','service','material','virtual_source','teach','cvv','other','basic','private'"
