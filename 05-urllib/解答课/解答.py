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