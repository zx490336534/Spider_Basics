import requests

url = 'http://www.baidu.com'
response = requests.get(url)
# print(response.text) #零、乱码

# print(response.content) #一、b''

print(response.content.decode()) #二、正常

#三、正常
response.encoding = 'utf-8'
print(response.text)

