import urllib3
import re
urllib3.disable_warnings()
from urllib3 import ProxyManager



def login_by_email(email,pwd):
    DEFAULT_HEADERS = {
        'Host': 'github.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://github.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }
    # http = ProxyManager('https://127.0.0.1:8080')
    http = urllib3.HTTPSConnectionPool('github.com')
    r = http.request('GET','https://github.com/login',headers=DEFAULT_HEADERS)
    text = r.data.decode('utf-8')
    token = re.findall(r'name="authenticity_token".*?value="(.*?)"', text)[0]

    cookie_login = r.headers['set-cookie']

    data = {
        'commit': 'Sign in',
        'utf8': '✓',
        'authenticity_token': token,
        'login': email,
        'password': pwd,
    }
    DEFAULT_HEADERS['Cookie'] = cookie_login
    r = http.request('POST','https://github.com/session',data,headers=DEFAULT_HEADERS,encode_multipart=False,redirect=False)
    #redirect=False取消自动跳转

    cookie_session = r.headers['set-cookie']
    # print(cookie_session)
    DEFAULT_HEADERS['Cookie'] = cookie_session

    r = http.request('GET','https://github.com/',headers=DEFAULT_HEADERS)
    text = r.data.decode('UTF-8')
    # print(text)
    if 'Start a project' in text:
        print('登陆成功')
        # print(text)
    else:
        print(r.status)
        print(text)
        print('登陆失败')


login_by_email('490336534@qq.com','zx660644')