import urllib.request
import urllib3
import re
import http.cookiejar
from urllib.parse import urlencode
import json

urllib3.disable_warnings()

url = 'https://github.com/login'
login_url = 'https://github.com/session'

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open(url)
token = re.findall(r'name="authenticity_token".*?value="(.*?)"',response.read().decode('utf-8'))[0]
# print(token)
# print(response.headers.get('Set-Cookie'))
j=0
for i,v in response.headers.items():
    Cookie = v
    j += 1
    if j > 10:
        break

Cookie = Cookie.split(';')[0]
# print(Cookie)

headers = {
'Host': 'github.com',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'https://github.com/session',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Cookie':  Cookie
}
data = {
    'commit':'Sign in',
    'utf8':'✓',
    'authenticity_token':token,
    'login':'490336534@qq.com',
    'password':'zx660644'
}
data = json.dumps(data).encode('utf-8')
# req = urllib.request.Request(login_url,data=data,headers=headers)
# response = opener.open(req)
# print(response.getcode(),response.read())

requests = urllib3.PoolManager()
# login_url = login_url + urlencode(data)
response = requests.request('POST',login_url,headers=headers,body=data)
# print(response.status,response.data.decode('utf-8'))
print(response.status)




