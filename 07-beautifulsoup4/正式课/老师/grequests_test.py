#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

import time
import requests
import grequests
import urllib3
urllib3.disable_warnings()

urls = [
    'https://docs.python.org/2.7/library/index.html',
    'https://docs.python.org/2.7/library/dl.html',
    'http://www.iciba.com/partial',
    'http://2489843.blog.51cto.com/2479843/1407808',
    'http://blog.csdn.net/woshiaotian/article/details/61027814',
    'https://docs.python.org/2.7/library/unix.html',
    'http://2489843.blog.51cto.com/2479843/1386820',
    'http://www.bazhuayu.com/tutorial/extract_loop_url.aspx?t=0',
    'https://docs.python.org/2.7/library/index.html',
    'https://docs.python.org/2.7/library/dl.html',
    'http://www.iciba.com/partial',
    'http://2489843.blog.51cto.com/2479843/1407808',
    'http://blog.csdn.net/woshiaotian/article/details/61027814',
    'https://docs.python.org/2.7/library/unix.html',
    'http://2489843.blog.51cto.com/2479843/1386820',
    'http://www.bazhuayu.com/tutorial/extract_loop_url.aspx?t=0',
    'https://docs.python.org/2.7/library/index.html',
    'https://docs.python.org/2.7/library/dl.html',
    'http://www.iciba.com/partial',
    'http://2489843.blog.51cto.com/2479843/1407808',
    'http://blog.csdn.net/woshiaotian/article/details/61027814',
    'https://docs.python.org/2.7/library/unix.html',
    'http://2489843.blog.51cto.com/2479843/1386820',
    'http://www.bazhuayu.com/tutorial/extract_loop_url.aspx?t=0',
    'https://docs.python.org/2.7/library/index.html',
    'https://docs.python.org/2.7/library/dl.html',
    'http://www.iciba.com/partial',
    'http://2489843.blog.51cto.com/2479843/1407808',
    'http://blog.csdn.net/woshiaotian/article/details/61027814',
    'https://docs.python.org/2.7/library/unix.html',
    'http://2489843.blog.51cto.com/2479843/1386820',
    'http://www.bazhuayu.com/tutorial/extract_loop_url.aspx?t=0',
    'https://docs.python.org/2.7/library/index.html',
    'https://docs.python.org/2.7/library/dl.html',
    'http://www.iciba.com/partial',
    'http://2489843.blog.51cto.com/2479843/1407808',
    'http://blog.csdn.net/woshiaotian/article/details/61027814',
    'https://docs.python.org/2.7/library/unix.html',
    'http://2489843.blog.51cto.com/2479843/1386820',
    'http://www.bazhuayu.com/tutorial/extract_loop_url.aspx?t=0',
]

def method1():
    t1 = time.time()
    for url in urls:
        res = requests.get(url, verify=False)

    t2 = time.time()
    print('method1', t2 - t1)

def method2():
    tasks = [grequests.get(u) for u in urls]
    t1 = time.time()
    res = grequests.map(tasks, size=3)
    t2 = time.time()
    print('method2', t2 - t1)

def method3():
    tasks = [grequests.get(u) for u in urls]
    t1 = time.time()
    res = grequests.map(tasks, size=8)
    t2 = time.time()
    print('method3', t2 - t1)

def method4():
    tasks = [grequests.get(u, callback=response_handle) for u in urls]
    t1 = time.time()
    res = grequests.map(tasks, size=8)
    t2 = time.time()
    print('method4', t2 - t1)

def response_handle(r, *args, **kwargs):
    print(r.url)

if __name__ == '__main__':
    method1()
    method2()
    method3()
    method4()

