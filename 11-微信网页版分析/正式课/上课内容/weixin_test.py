#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time

__author__ = 'Terry'

import requests
from bs4 import BeautifulSoup

DEFAULT_HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

def visit_index(s):
    url = 'https://wx.qq.com/'
    s.get(url)

def get_13_time():
    return str(int(time.time()*1000))

class WXRobot(object):
    def __init__(self):
        self.s = requests.session()
        self.s.verify = False
        self.s.headers = DEFAULT_HEADERS

    def visit_index(self):
        url = 'https://wx.qq.com/'
        self.s.get(url)
        print('首页访问完成')

    def visit_jslogin(self):
        url = 'https://login.wx.qq.com/jslogin'
        params = {
            'appid': 'wx782c26e4c19acffb',
            'redirect_uri': 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage',
            'fun': 'new',
            'lang': 'zh_CN',
            '_': get_13_time()
        }
        r = self.s.get(url, params=params)
        text = r.text
        maths = re.search('window.QRLogin.uuid = "(.*?)"', text)
        uuid = maths.group(1)
        self.uuid = uuid

        print('uuid获取完成')

    def visit_vcode(self):
        url = 'https://login.weixin.qq.com/qrcode/%s' % self.uuid
        r = self.s.get(url)

        with open('qrcode.jpg', 'wb') as f:
            f.write(r.content)

        print('二维码获取完成')

    def visit_login(self):
        url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?' \
              'loginicon=true&uuid=%s&tip=0&_=%s' % \
              (self.uuid ,get_13_time())

        n = 60
        while n > 0:
            r = self.s.get(url)
            text = r.text

            maths = re.search('window.code=(.*?);', text)
            code = int(maths.group(1))

            if code == 200:
                print('已经登录')
                maths = re.search('redirect_uri="(.*?)"', text)
                self.redirect_uri = maths.group(1)
                return True
            elif code == 201:
                print('已经扫描，但是没有点击 登录 确认')
            elif code == 408:
                print('超时，二维码无效')
                break
            else:
                print('未知错误')
                break

            n -= 1
            time.sleep(1)

        return False
        print('redirect_uri获取完成')

    def visit_newloginpage(self):
        r = self.s.get(self.redirect_uri, allow_redirects=False)
        text = r.text

        bs = BeautifulSoup(text, 'lxml')
        self.skey = bs.find('skey').text
        self.wxsid = bs.find('wxsid').text
        self.wxuin = bs.find('wxuin').text
        self.pass_ticket = bs.find('pass_ticket').text
        self.isgrayscale = bs.find('isgrayscale').text


if __name__ == '__main__':
    wx = WXRobot()

    wx.visit_index()

    wx.visit_jslogin()

    wx.visit_vcode()

    b = wx.visit_login()

    if b:
        wx.visit_newloginpage()

    print('运行结束')

