'''
分析：
1、首页：
https://wx.qq.com/

漏了一步 获取第二部发送二维码的url中的AfuKu1lFWg==
https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_=1517066206221

2、二维码：
https://login.weixin.qq.com/qrcode/AfuKu1lFWg==

3、得到一个redicret_url：
https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=AfuKu1lFWg==&tip=0&r=-942755202&_=1517066206223

4、返回第三步得到的redirect_url：
https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=AQjjWagfYlbwVaPAthMnDC7U@qrticket_0&uuid=AfuKu1lFWg==&lang=zh_CN&scan=1517066158&fun=new&version=v2&lang=zh_CN


等待二维码被成功扫描且点击确认登陆 估计是在第3、4步确认过了

5、初始化微信，获得联系人列表：
https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-942750744&lang=zh_CN&pass_ticket=WPhOiAtLkRN9LffvpnXNkLY5uBESJag2sxZDcpa41No%253D

6、得到了一个msgID：
https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxstatusnotify?lang=zh_CN&pass_ticket=WPhOiAtLkRN9LffvpnXNkLY5uBESJag2sxZDcpa41No%253D

7、获取联系人列表：
https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket=WPhOiAtLkRN9LffvpnXNkLY5uBESJag2sxZDcpa41No%253D&r=1517066212320&seq=0&skey=@crypt_97a4d9e3_b1d8a5469a5f7368117cf71939ef8c7d

8、同步确认，没有消息时，服务器阻塞25秒返回：
window.synccheck={retcode:"0",selector:"0"}
有消息时：
window.synccheck={retcode:"0",selector:"2"}
https://webpush.wx.qq.com/cgi-bin/mmwebwx-bin/synccheck?r=1517066212449&skey=%40crypt_97a4d9e3_b1d8a5469a5f7368117cf71939ef8c7d&sid=Zk6BEgw6mjVK9Rgf&uin=176032015&deviceid=e930425005664675&synckey=1_678793598%7C2_678793617%7C3_678793584%7C11_678793514%7C1000_1517054522%7C1001_1517054593&_=1517066206225

9、获取微信群人员列表：
https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxbatchgetcontact?type=ex&r=1517066212456&lang=zh_CN&pass_ticket=WPhOiAtLkRN9LffvpnXNkLY5uBESJag2sxZDcpa41No%253D

10、获取服务器最近的消息：
https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsync?sid=Zk6BEgw6mjVK9Rgf&skey=@crypt_97a4d9e3_b1d8a5469a5f7368117cf71939ef8c7d&lang=zh_CN&pass_ticket=WPhOiAtLkRN9LffvpnXNkLY5uBESJag2sxZDcpa41No%253D


11、发送文字消息
https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket=WPhOiAtLkRN9LffvpnXNkLY5uBESJag2sxZDcpa41No%253D

12、options方法
https://file.wx.qq.com/cgi-bin/mmwebwx-bin/webwxuploadmedia?f=json

13、上传图片文件
https://file.wx.qq.com/cgi-bin/mmwebwx-bin/webwxuploadmedia?f=json

14、发送图片消息
https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsgimg?fun=async&f=json&lang=zh_CN&pass_ticket=WPhOiAtLkRN9LffvpnXNkLY5uBESJag2sxZDcpa41No%253D

备用：
无意义包：
https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxstatreport?fun=new&lang=zh_CN&pass_ticket=WPhOiAtLkRN9LffvpnXNkLY5uBESJag2sxZDcpa41No%253D
暂时不知道
https://support.weixin.qq.com/cgi-bin/mmsupport-bin/reportforweb?rid=63637&rkey=72&rvalue=75
提示：一些url请求，如果没有返回值，也没有set-cookie 大概率这个页面是不用理会的
微信的联系人唯一标示位：Uin，UserName是每次登陆都会变化的一个不重复的值

requests提交请求的参数3种：
form参数，通过post(data=from参数字典)
json参数，是通过post(json=json字典)
url后面的参数，是通过post(params=url参数字典)
'''
import json
import random

import os
import requests
import time
import re
from bs4 import BeautifulSoup

# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

DEFAULT_HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

def get_13_time():
    return str(int(time.time()*1000))

class WXRobot(object):
    def __init__(self):
        self.s = requests.session()
        self.s.verify = False
        self.s.headers = DEFAULT_HEADERS
        self.DeviceID = 'e' + str(random.random())[2:17]

    def visit_index(self):
        url = 'https://wx.qq.com/'
        self.s.get(url)
        print('首页访问完成')

    def visit_jslogin(self):
        url = 'https://login.wx.qq.com/jslogin'
        params = {
        'appid': 'wx782c26e4c19acffb',
        'redirect_uri': 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage',
        'fun': 'new',
        'lang': 'zh_CN',
        '_': get_13_time()
        }

        r = self.s.get(url,params=params)
        text = r.text

        maths = re.search('window.QRLogin.uuid = "(.*?)"', text)
        uuid = maths.group(1)
        self.uuid = uuid
        print('uuid获取完成')

    def visit_vcode(self):
        url = 'https://login.weixin.qq.com/qrcode/%s' % self.uuid
        r = self.s.get(url)
        with open('qrcode.jpg','wb') as f:
            f.write(r.content)
        print('二维码获取完成')

    def visit_login(self):
        url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=%s&tip=0&_=%s' %(self.uuid,get_13_time())

        n = 60
        while n > 0:
            r = self.s.get(url)
            text = r.text

            maths = re.search('window.code=(.*?);',text)
            self.maths = maths
            code = int(self.maths.group(1))
            if code == 200:
                print('已经登陆')
                maths = re.search('redirect_uri="(.*?)"', text)
                self.redirect_url = maths.group(1)
                return True
            elif code == 201:
                print('已经扫描，但是没有点击登陆确认')
            elif code == 408:
                print('超时，二维码无效')
                break
            else:
                print('未知错误')
                break

            n -= 1
            time.sleep(1)
        return False
        print('redirect_url获取完成')

    def visit_newloginpage(self):
        r = self.s.get(self.redirect_url, allow_redirects=False)
        text = r.text
        bs = BeautifulSoup(text,'lxml')
        self.skey = bs.find('skey').text
        self.wxsid = bs.find('wxsid').text
        self.wxuin = bs.find('wxuin').text
        self.pass_ticket = bs.find('pass_ticket').text
        self.isgrayscale = bs.find('isgrayscale').text
    def get_BaseRequest_content(self):
        data = {"Uin": self.wxuin,
                 "Sid": self.wxsid,
                 "Skey": self.skey,
                 "DeviceID": self.DeviceID
                }
        return data

    def get_BaseRequest(self):
        data ={"BaseRequest": self.get_BaseRequest_content()
               }
        return data

    def visit_webwxinit(self):
        url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit"
        params = {
            'r': ~int(time.time()),
            'lang':'zh_CN',
            'pass_ticket':self.pass_ticket,

        }
        r = self.s.post(url,json=self.get_BaseRequest(),params=params)
        r.encoding = 'utf-8'
        text = r.text
        json_data = json.loads(text)
        self.my_account = json_data['User']
        self.chatSet = json_data['ChatSet']
        self.group_list = json_data['ContactList']
        print('登陆用户为：%s' % (self.my_account['NickName']))

    def visit_statusnotify(self):
        url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxstatusnotify?lang=zh_CN&pass_ticket=%s' % self.pass_ticket
        data = {
            "BaseRequest": self.get_BaseRequest_content(),
             "Code": 3,
             "FromUserName": self.my_account['UserName'],
             "ToUserName": self.my_account['UserName'],
             "ClientMsgId": int(get_13_time())

        }
        self.s.post(url,json=data)

        print('visit_statusnotify获取完成')

    def visit_getcontace(self):
        url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact'
        params = {
        'lang': 'zh_CN',
        'pass_ticket': self.pass_ticket,
        'r': get_13_time(),
        'seq': '0',
        'skey': self.skey
            }
        r = self.s.get(url,params=params)
        r.encoding('utf-8')
        json_data = r.json()
        self.member_list = json_data['MemberList']
        print('visit_getcontace获取完成')

    def visit_batchgetcontact(self):
        url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxbatchgetcontact'
        params = {
            'type':'ex',
            'r':get_13_time(),
            'lang':'zh_CN',
            'pass_ticket':self.pass_ticket
        }
        chat_list = self.chatSet.split(',')
        chat_list.remove('filehelper')
        chat_list_new = [{'UserName':c.strip(),'EncryChatRoomId':''}for c in chat_list if c.startswith('@')]
        data = {
            "BaseRequest": self.get_BaseRequest_content(),
            "Count": 19,
            "List":chat_list_new

        }
        r = self.s.post(url,params=params)
        r.encoding='UTF-8'
        json_data = r.json()
        self.group_contract_list = json_data['ContactList']

    def get_LocalId(self):
        return str(time.time())+str(random.random())[2:9]


    def send_msg(self,msg,to_user_name='filehelper'):
        url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg'
        data = {
	"BaseRequest":self.get_BaseRequest_content(),
	"Msg": {
		"Type": 1,
		"Content": msg,
		"FromUserName": self.my_account['UserName'],
		"ToUserName": to_user_name,
		"LocalID": self.get_LocalId(),
		"ClientMsgId": self.get_LocalId()
	},
	    "Scene": 0
    }
        data = json.dumps(data,ensure_ascii=False).encode('utf-8')
        r =self.s.post(url,data)
        json_data = r.json()
        if 0 == json_data['BaseResponse']['Ret']:
            print('发送消息成功')
        else:
            print('发送消息失败 %s' % r.text)


    def upload_img(self,pic_path):
        pass

    def send_img(self,to_user_name='filehelper'):
        pass




if __name__ == '__main__':
    wx = WXRobot()
    wx.visit_index()
    wx.visit_jslogin()
    wx.visit_vcode()
    b = wx.visit_login()
    if b:
        wx.visit_newloginpage()
        wx.visit_webwxinit()
        wx.visit_statusnotify()
        wx.visit_batchgetcontact()
        wx.send_msg('测试发送！！！')

    print('登陆结束')


