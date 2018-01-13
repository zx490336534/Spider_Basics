import urllib.request


url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
print(type(response.headers)) # read  getcode 返回http状态码
for i,v in response.headers.items():
    print(i,v)
print(response.read())

#添加headers，data
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
req = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read())

#处理cookie信息
import http.cookiejar
cookie = http.cookiejar.CookieJar() #声明一个CookieJar实例来保存cookie
handler = urllib.request.HTTPCookieProcessor(cookie) #创建一个cookie处理器
opener = urllib.request.build_opener(handler)
response = opener.open(url)
print(cookie)
print(opener)


import urllib3

requests = urllib3.PoolManager()
r = requests.request('GET',url)
print('\n')
print(r.data)
