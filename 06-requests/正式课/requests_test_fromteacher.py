#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from requests.cookies import RequestsCookieJar
__author__ = 'Terry'

import requests
from requests import session

'''
基础用法
'''
# url = 'http://httpbin.org/'
# r = requests.get(url)
# print(r.text)

'''
提交get参数
'''
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('http://httpbin.org/get', params=payload)
#等价于
# r = requests.get('http://httpbin.org/get?key1=value1&key2=value2')
# print(r.text)

'''
headers
'''
# headers = {
# 	    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
# 	                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
# 	    'Referer': r'http://httpbin.org',
# 	    'Connection': 'keep-alive',
# 	}
# data = {
# 	    'key1': 'value1',
# 	    'key2': 'value2'
# 	}
# url = 'http://httpbin.org/post'
# r = requests.post(url, data=data, headers=headers)
# print(r.text)  # 打印的是一个字符串，但是符合json的语法的字符串
# print(r.json()) # 打印的是json对象

'''
json转字符串
data = {'k':'v'}
json.dumps(data)

字符串转json
s = '{"k":"v"}'
j = json.loads(s)
'''
# import json
# r = requests.post(url, data=json.dumps(data), headers=headers)  # json.loads(string)
# print(r.text)

'''取消自动跳转，302的跳转'''
# r = requests.get('https://github.com', allow_redirects=False, verify=False)
# print(r.status_code)

# r = requests.get('https://github.com', timeout=0.001, verify=False)
# print(r.status_code)

# proxies = {'http': '127.0.0.1:8888', 'https':'127.0.0.1:8889', 'http://httpbin.org/': '127.0.0.1:8887'}
# proxies = {'http': '127.0.0.1:8888', 'https':'127.0.0.1:8889'}
# r = requests.get('http://httpbin.org/', proxies=proxies)
# print(r.status_code)

# r = requests.get('https://www.alipay.com')
# r = requests.get('https://www.alipay.com', verify=False)
# print(r.status_code)

'''
response，状态码
'''
# r = requests.get('http://httpbin.org/') # head, option等
# if r.status_code == requests.codes.ok:
# if r.status_code == 200:
#     print('成功')
# else:
#     print('失败')

# STATUS_CODES_OK = 101
# STATUS_CODES_ERROR = 102
# STATUS_CODES_EXCEPTION = 103
# status = 0
# if status == STATUS_CODES_OK:
#     pass
# elif status == STATUS_CODES_ERROR:
#     pass
# else:
#     pass

'''
cookie
cookie 遵循这样一个原则：
子域可以访问父域的cookie，但是父域不能访问子域
test1.httpbin.org 可以访问 httpbin.org的所有cookie，反之不能， 同级域名也不行，也访问不了test2.httpbin.org
httpbin.org/child1 可以访问 httpbin.org/的所有cookie，反之不能， 同级目录也不行，也访问不了httpbin.org/child2
'''
# jar = RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='test.httpbin.org', path='/cookies')  #
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# jar.set('root_cookie', 'root', path='/')
# jar.set('default_cookie', 'default')
# url = 'http://httpbin.org/cookies'
# s = requests.session()
# r = s.get(url, cookies=jar)
# print(r.text)

'''
使用session
'''
# s = requests.session()
# r = s.get('http://httpbin.org/')
# r = requests.get('http://httpbin.org/')

# print(r.status_code)

'''
编码
'''
r = requests.get('http://www.baidu.com')
print(r.encoding)

# r.content 返回的是b'' ，即字节串bytes
content = r.content
print(content)
print(content.decode('utf-8'))
# r.text 返回 str'',  即字符串
text = r.text
print(text)
print(text.encode('raw_unicode_escape').decode('utf-8'))
print(text.encode('iso-8859-1').decode('utf-8'))
print(text.encode(r.encoding).decode('utf-8')) # r.encoding 有可能为None

s = '我是测试中文abc123'
print(s.encode('ascii', 'ignore'))
print(s.encode('ascii', 'replace'))
print(s.encode('ascii', 'xmlcharrefreplace'))

s = '我是测试中文abc123'
s_ascii = s.encode('ascii', 'xmlcharrefreplace')
print(s_ascii.decode('ascii'))
from common.util import xmlchar_2_cn
print(xmlchar_2_cn(s_ascii.decode('ascii')))

'''
    多线程
'''
# import threading
# from time import ctime
#
# def request_httpbin(num=0, url='http://httpbin.org/'):
#     print('第 %s 次请求 开始， %s' % (num, ctime()))
#     r = requests.get('http://httpbin.org/')
#     print('第 %s 次请求 结束， %s' % (num, ctime()))
#
# if __name__ == '__main__':
#     threads = []
#     for i in range(1, 101):
#         t = threading.Thread(target=request_httpbin, args=(i,))
#         threads.append(t)
#
#     for t in threads:
#         t.start()
#
#     for t in threads:
#         t.join()

'''
使用gevent实现并发
'''
# import requests
# import gevent
# import urllib3
# urllib3.disable_warnings()
# import time
# from gevent import monkey
# monkey.patch_all()
#
# urls = [
#     'https://docs.python.org/2.7/library/index.html',
#     'https://docs.python.org/2.7/library/dl.html',
#     'http://www.iciba.com/partial',
#     'http://2489843.blog.51cto.com/2479843/1407808',
#     'http://blog.csdn.net/woshiaotian/article/details/61027814',
#     'https://docs.python.org/2.7/library/unix.html',
#     'http://2489843.blog.51cto.com/2479843/1386820',
#     'http://www.bazhuayu.com/tutorial/extract_loop_url.aspx?t=0',
# ]
#
# def method1():
#     t1 = time.time()
#     for url in urls:
#         res = requests.get(url, verify=False)
#
#     t2 = time.time()
#     print('method1', t2 - t1)
#
# def method2():
#     jobs = [gevent.spawn(requests.get, url, verify=False) for url in urls]
#     t1 = time.time()
#     gevent.joinall(jobs)
#     t2 = time.time()
#     print('method2', t2 - t1)
#
# if __name__ == '__main__':
#     method1()
#     method2()