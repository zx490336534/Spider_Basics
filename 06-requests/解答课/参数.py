import requests

url = 'http://www.github.com'


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
proxy = {'http':'127.0.0.1:8080','https':'127.0.0.1:8080'}
data = {'key':'value1'}

response = requests.post(url,headers=headers,data=data) #正常跳转
response.encoding = 'utf-8'
print(response.headers) #location
print(response.history)
print(response.url)
print('-----------------')
response1 = requests.post(url,headers=headers,data=data,allow_redirects=False) #不允许跳转
response1.encoding = 'utf-8'
print(response1.headers) #location
print(response1.history)
print(response1.url)