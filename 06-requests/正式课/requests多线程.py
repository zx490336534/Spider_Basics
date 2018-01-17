import threading
from time import ctime
import requests

def request_httpbin(num=0, url='http://httpbin.org/'):
    print('第 %s 次请求 开始， %s' % (num, ctime()))
    r = requests.get('http://httpbin.org/')
    print('第 %s 次请求 结束， %s' % (num, ctime()))

if __name__ == '__main__':
    threads = []
    for i in range(1, 101):
        t = threading.Thread(target=request_httpbin, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()