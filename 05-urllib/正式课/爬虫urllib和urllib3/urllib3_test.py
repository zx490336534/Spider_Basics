#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

import urllib3

'''
基础用法
'''
# http = urllib3.PoolManager()
# resp = http.request('get','http://www.baidu.com')
# html = resp.data

'''
HTTPConnectionPool
'''
http = urllib3.HTTPConnectionPool('baidu.com')
resp = http.request('get', 'http://www.baidu.com')
print(resp.data)

'''
代理，headers
'''
proxy = urllib3.ProxyManager('http://127.0.0.1:8888', headers={'connection': 'keep-alive'})
r = proxy.request('GET', 'http://httpbin.org/robots.txt')
print(r.status)
print(r.data.encode('utf-8'))

'''
cookie 操作，没有直接的方法操作cookie
'''
import urllib3
proxy = urllib3.ProxyManager('http://127.0.0.1:8888', headers={'connection': 'keep-alive',
                                                               'Cookie':'cookie1=a;cookie2=b'})
r = proxy.request('GET', 'http://httpbin.org/robots.txt')
print(r.status)
print(r.data)