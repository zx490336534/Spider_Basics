import urllib3
import re
import json

'''
用urllib3实现github登陆
'''

github_headers = {
'Host': 'github.com',
'Connection': 'keep-alive',
'Content-Length': '186',
'Cache-Control':' max-age=0',
'Origin': 'https://github.com',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'https://github.com/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

url_login = 'https://github.com/login'
url_session = 'https://github.com/session'

urllib3.disable_warnings()
http = urllib3.PoolManager()
res_login = http.request('GET',url_login)
value = re.findall('name="authenticity_token".*?value="(.*?)"',res_login.data.decode('utf8'))[0]

github_data = {
    'commit':'Sign in',
    'utf8':'✓',
    'authenticity_token':value,
    'login':'490336534@qq.com',
    'password':'zx660644'
}

encoded_github_data = json.dumps(github_data).encode('utf-8')
res_session = http.request('POST',url_session,headers = github_headers, body=encoded_github_data)

text = res_session.data.decode('utf8')
print(text)
if 'Start a project' in text:
    print('登陆成功')
    print(text)
else:
    print('登陆失败')
