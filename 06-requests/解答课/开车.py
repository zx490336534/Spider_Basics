import requests
import re
import gevent
from gevent import monkey;monkey.patch_socket()

#post 请求 https://www.nvshens.com/ajax/girl_query_total.ashx
post_url = 'https://www.nvshens.com/ajax/girl_query_total.ashx'
base_url = 'https://www.nvshens.com/'
data = {
    'professional':'主播',
    'country':'中国',
    'curpage':'1',
    'pagesize':'20'
}
image_text = requests.post(post_url,data=data).text
image_urls = re.findall(r"<div><a href='(.*?)/'",image_text,re.S)


def girl_content(url):
    text = requests.get(url)
    text.encoding = 'utf-8'
    text = text.text
    print(text)


if __name__ == '__main__':

    tasks = [gevent.spawn(girl_content,base_url+url) for url in image_urls]
    gevent.joinall(tasks)