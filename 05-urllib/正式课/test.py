from http import client,server,cookiejar,cookies
from urllib import request,parse
'禁爬：https://www.baidu.com/robots.txt'
import time
'''
post方法实现
'''
start = time.time()
headers_baidu = {
    'connection':'keep-alive'
}
post_data = {
    'var1':'test'
}
url = 'http://www.baidu.com'
# request_baidu = request.Request(url,headers=headers_baidu,data=post_data,method='option')
request_baidu = request.Request(url,headers=headers_baidu,data=post_data)
request_baidu.get_method = lambda :'option'

# resp = request.urlopen(request_baidu)

'''
代理
'''
# data = {
#     'var':'test'
# }
# proxy =request.ProxyHandler({'http':'127.0.0.1:8888'})
# opener = request.build_opener(proxy)
# request.install_opener(opener)
# data = parse.urlencode(data).encode('utf-8')
# page = opener.open(url,data).read()
# page = page.decode('utf-8')
# print(page)
'''
操作cookie
'''
URL_ROOT = r'http://d.weibo.com/'
cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response =opener.open(URL_ROOT)

for item in cookie:
    print('Name = '+item.name)
    print('Value = '+item.value)


print('耗时：%s '%(time.time() -start))