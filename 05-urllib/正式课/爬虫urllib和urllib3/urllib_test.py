#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

from urllib import request, parse
import time
start = time.time()
'''
自定义headers
'''
headers_baidu = {
    'connection': 'keep-alive'
}
url = 'http://www.baidu.com'
request_baidu = request.Request(url, headers=headers_baidu)
resp = request.urlopen(request_baidu)

'''
post方法实现
'''
headers_baidu = {
    'connection': 'keep-alive'
}
post_data = {
    'var1': 'test'
}
url = 'http://www.baidu.com'
request_baidu = request.Request(url, headers=headers_baidu, data=post_data)
resp = request.urlopen(request_baidu)

'''
get、post方法之外的方法实现
'''
headers_baidu = {
    'connection': 'keep-alive'
}
post_data = {
    'var1': 'test'
}
url = 'http://www.baidu.com'
# request_baidu = request.Request(url, headers=headers_baidu, data=post_data, method='options')
request_baidu = request.Request(url, headers=headers_baidu, data=post_data)
request_baidu.get_method = lambda : 'options'
resp = request.urlopen(request_baidu)

'''
代理
'''
data = {
    'var1': 'test'
}
proxy = request.ProxyHandler({'http': '127.0.0.1:8888'})  # 设置proxy
opener = request.build_opener(proxy)  # 挂载opener
request.install_opener(opener)  # 安装opener
data = parse.urlencode(data).encode('utf-8')
page = opener.open(url, data).read()
page = page.decode('utf-8')
print(page)

'''
操作cookie
'''
import http.cookiejar
URL_ROOT = r'http://d.weibo.com/'

cookie = http.cookiejar.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
handler = request.HTTPCookieProcessor(cookie)  # 利用HTTPCookieProcessor对象来创建cookie处理器
opener = request.build_opener(handler)  # 通过handler来构建opener

response = opener.open(URL_ROOT)

for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)

print("耗时：%s 秒" % (time.time() - start))


