from requests import session
import re

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



def get_first_str_by_text(p,text):
    l = get_all(p,text)
    if not l:
        raise Exception('没有有效的值')
    return l[0]

def get_all(p,text):
    l = re.findall(p,text,re.M|re.S)
    return l


def browse_github(user,pwd):
    s = session()

    url = 'https://github.com/'
    # r = s.get(url,headers = DEFAULT_HEADERS)

    url_log = 'https://github.com/login'
    r = s.get(url_log,headers=DEFAULT_HEADERS)
    text = r.text
    token = get_first_str_by_text('name="authenticity_token".*?value="(.*?)"',text)

    url_session = 'https://github.com/session'
    data = {
        'commit':'Sign in',
        'utf8':'✓',
        'authenticity_token':token,
        'login':user,
        'password':pwd,
    }
    r = s.post(url_session,data=data)
    text = r.text
    if 'Start a project' in text:
        print('登陆成功')
        print(text)
    else:
        print('登陆失败')


if __name__ == '__main__':
    user = '490336534@qq.com'
    pwd = 'zx660644'
    browse_github(user,pwd)