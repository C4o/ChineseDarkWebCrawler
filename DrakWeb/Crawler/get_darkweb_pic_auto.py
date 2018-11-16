#coding=utf-8
#Created by Cao

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sqlite3, sys, logging, time, os, re, urllib
import win32api, win32clipboard, win32con
from ctypes import *
import time

reload(sys)
sys.setdefaultencoding('utf-8')

def get_image(browser, url, id, path):
    # 访问图片地址
    browser.get(url)
    time.sleep(1.5)
    # 保存的位置
    path = 'C:\\Users\\Administrator\\Desktop\\darkweb\\static\\topic_image\\'+str(id)+'.png'
    # 摁下ctrl
    win32api.keybd_event(17, 0, 0, 0)
    # 摁下s
    win32api.keybd_event(83, 0, 0, 0)
    # 抬起
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    # 延时
    time.sleep(1)
    # 将路径复制到剪切板
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(path)
    win32clipboard.CloseClipboard()
    # 鼠标定位输入框并点击
    windll.user32.SetCursorPos(500, 510)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(1.5)
    # 按下ctrl+a
    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(0x41, 0, 0, 0)
    win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1.5)
    # 按下ctrl+v
    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(0x56, 0, 0, 0)
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1.5)
    # 摁下enter
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1.5)
    # double click
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

def DarkCrawler():
    try:
        fireFoxOptions = webdriver.FirefoxOptions()
        #headless模式无弹窗
        #fireFoxOptions.set_headless()
        #设置tor为firefox源
        binary = FirefoxBinary('C:\\Tor\\Tor Browser\\Browser\\firefox.exe')
        browser = webdriver.Firefox(firefox_options=fireFoxOptions , firefox_binary=binary)
        # 模拟按键进行登录浏览
        browser.get('http://bmp3qqimv55xdznb.onion')
        time.sleep(15)
        browser.find_element_by_id('username').send_keys('JessieC')
        browser.find_element_by_id('password').send_keys('qwerQWER1234')
        browser.find_element_by_name("login").click()
        time.sleep(5)
        # 获取sid后拼接图片地址进行下载
        current_url = browser.current_url
        sid = current_url[-32:]
        image_id_file = open("image_id_new.txt", 'r')
        ids = image_id_file.readlines()
        for id in ids:
            id = str(id[:-1])
            path = 'C:\\Users\\Administrator\\Desktop\\darkweb\\static\\topic_image\\'+str(id)+'.png'
            if os.path.exists(path):
                pass
            else:
                url = "http://bmp3qqimv55xdznb.onion/download/file.php?id=%s&sid=%s" % (id, sid)
                print url
                try:
                    get_image(browser, url, id, path)
                except Exception,e:
                    print e
                    pass
        #关闭firefox、cursor、数据库连接，提交事务
        browser.close()
    except Exception,e:
        print e
        pass


if __name__ == '__main__':
	while 1:
		try:
			print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
			DarkCrawler()
			time.sleep(1000)
		except Exception, e:
			print e
			pass
