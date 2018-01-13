import urllib3

'''
基础用法
'''
http = urllib3.PoolManager()
resp = http.request('get','http://www.baidu.com')
html = resp.data

'''
HTTPConnectionPool
'''
http = urllib3.HTTPConnectionPool('www.baidu.com') #不写会报错：TypeError: __init__() missing 1 required positional argument: 'host'
resp = http.request('get','http://www.baidu.com')
print(resp.data)

'''
requests测试
'''
# import requests
# s = requests.session()
# r = s.get('https://www.baidu.com')
# print(r.text.encode('raw_unicode_escape').decode('utf-8'))

'''
代理
'''

proxy = urllib3.ProxyManager('http://127.0.0.1:8080',headers={'connection':'keep-alive'})
r = proxy.request('GET','http://httpbin.org/robots.txt')
print(r.status)
print(r.data)

'''
cookie 操作 没有直接的方法操作cookie
'''
