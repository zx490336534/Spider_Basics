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


'''
    requests.util 模块 select_proxy 方法 中可以看出，代理的先后顺序为
    譬如：http://httpbin.org/ 这个地址
    1、匹配 http://httpbin.org ，ps: 后面没有 /
    2、匹配 http
    3、all://httpbin.org
    4、all
'''
# proxies = {'http': '127.0.0.1:8888', 'https':'127.0.0.1:8889', 'http://httpbin.org': '127.0.0.1:8887'}
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
# s = requests.session()
# r = s.get('http://www.baidu.com', params={'k':'中文测试'})
# print(r.encoding)

# r.content 返回的是b'' ，即字节串bytes
# content = r.content
# print(content)
# print(content.decode('utf-8'))
# r.text 返回 str'',  即字符串
# text = r.text
# print(text)
# print(text.encode('raw_unicode_escape').decode('utf-8'))
# print(text.encode('iso-8859-1').decode('utf-8'))
# print(text.encode(r.encoding).decode('utf-8')) # r.encoding 有可能为None
# print(text.encode().decode('utf-8')) # encode  默认编码是UTF-8

s = '我是测试中文abc123'
# print(s.encode('ascii', 'ignore'))  # 忽略不能解析的部分
# print(s.encode('ascii', 'replace'))  # 替换，用？替换所有不认识的部分
# print(s.encode('ascii', 'xmlcharrefreplace')) #替换，用 &#4位数字+；结尾，替换
#
# def xmlchar_2_cn(s):
#     def convert_callback(matches):
#         char_id = matches.group(1)
#         try:
#             return chr(int(char_id))
#         except:
#             return char_id
#     import re
#     ret = re.sub("&#(\d+)(;|(?=\s))", convert_callback, s)
#
#     return ret
#
# s = '我是测试中文abc123'
# s_ascii = s.encode('ascii', 'xmlcharrefreplace')
# print(s_ascii.decode('ascii'))
# print(xmlchar_2_cn(s_ascii.decode('ascii')))

'''
unicode
ascii   0-127 谁都认可，除了ucs
gb2312
gbk
gb18030
utf-8   utf的全称就是 UCS transfer format
utf-16,utf-32，基本不用
'''

# b'&#25105;&#26159;&#27979;&#35797;&#20013;&#25991;abc123'

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
#         t = threading.Thread(target=request_httpbin, args=(i, ))
#         threads.append(t)
#
#     for t in threads:
#         t.start()
#
#     for t in threads:
#         t.join()

'''
不牵扯到网卡返回数据这一块
线程：多个线程之间谁先结束，是随机的，由系统决定
协程：非常规律的，
第一个任务的第一步完成，到第二个任务的第一步，
第一个任务的第二步完成，到第二个任务的第二步
'''

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


