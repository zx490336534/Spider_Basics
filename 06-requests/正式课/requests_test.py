import requests
import urllib3
from requests.cookies import RequestsCookieJar

urllib3.disable_warnings()

#基础用法
# url = 'https://httpbin.org'
# r = requests.get(url)
# print(r.text)



#提交get参数
# payload = {'key1':'value1','key2':'value2'}
# r = requests.get('https://httpbin.org/get',params=payload)
# print(r.text)
#等价于
# r = requests.get('https://httpbin.org/get?key1=value1&key2=value2')
# print(r.text)



#
# data = {
#     "key1": "value1",
#     "key2": "value2"
# }
# headers = {
#     "Connection": "keep-alive",
#     "Referer": "httpbin.org",
#     "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11",
# }
# url = 'https://httpbin.org/post'
# r = requests.post(url,data=data,headers=headers)
# print(r.text)
# print(r.json())


'''
json转字符串
data = {'k':'v'}
json.dumps(data)
字符串转json
s = '{'k':'v'}'
json.loads(s)
'''

#取消自动跳转，302跳转
# r = requests.get('http://github.com',allow_redirects=True,verify=False)
# print(r.status_code)

#超时,会报错
# r = requests.get('http://github.com',timeout = 0.001,verify=False)
# print(r.status_code)

#代理
proxies = {'http':'127.0.0.1:8080','https':'127.0.0.1:8080'}
r = requests.get('http://httpbin.org/',proxies=proxies)
# print(r.status_code)


#状态码
# r = requests.get('http://httpbin.org/')
# if r.status_code == 200:
#     print('成功')
# else:
#     print('失败')

STATUS_CODES_OK = 101
STATUS_CODES_ERROR = 102
status = 0
if status == STATUS_CODES_OK:
    pass
elif status == STATUS_CODES_ERROR:
    pass
else:
    pass


#使用session
s = requests.session()
r = s.get('http://httpbin.org')
# print(r.status_code)

#cookie
'''
cookie 遵循这样一个原则
子域可以访问父域的cookie，但是父域不能访问子域
test.httpbin.org 可以访问httpbin.org的所有cookie，反之不能，同级域名也不行
子目录可以访问父目录，电脑上父目录不能访问子目录的
'''
jar = RequestsCookieJar()
jar.set('tasty_cookie','yum',domain='httpbin.org',path='/cookies')
jar.set('gross_cookie','blech',domain='httpbin.org',path='elsewhere')
jar.set('root_cookie','root',path='/')
jar.set('default_cookie','default')
url = 'http://httpbin.org/cookies'
r = requests.get(url,cookies=jar)
# print(r.text)

#编码
r = requests.get('http://www.baidu.com')
print(r.encoding)

#r.content 返回的是b''，即字符串
content = r.content
print(content)
print(content.decode('utf-8'))

#r.text返回str''
text = r.text
print(text)
print(text.encode('raw_unicode_escape').decode('utf-8'))
print(text.encode('iso-8859-1').decode('utf-8'))
print(text.encode(r.encoding).decode('utf-8'))  #r.encoding有可能为None