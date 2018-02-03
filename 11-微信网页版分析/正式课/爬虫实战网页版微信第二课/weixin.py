#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import hashlib
import json
import mimetypes
import os
import random
import re
import threading
from collections import OrderedDict
from urllib import parse
import time

import math
import requests
from bs4 import BeautifulSoup

from cA.mysql_handle import insert_many

__author__ = 'Terry'


def get_13_time():
    """
    获取13位的str类型的时间戳
    """
    return str(int(time.time() * 1000))


log_path = os.path.join(os.getcwd(), 'logs', 'log')

def save_error_to_log(text, sign='unknown'):
    with open(log_path, 'a') as f:
        f.write("%s:%s%s%s%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), sign, os.linesep, text, os.linesep))

class WeiXinRobot(object):
    WX_URLS = {
        'jslogin': 'https://login.wx2.qq.com/jslogin?%s',
        'qrcode': 'https://login.weixin.qq.com/qrcode/%s',
        'login': 'https://login.wx2.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&tip=%s&uuid=%s&_=%s'
    }

    DEFAULT_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'content-type': 'application/json;charset=UTF-8;application/x-www-form-urlencoded',
        'Referer': 'https://wx.qq.com/',
    }

    UPLOAD_FILE_HEADERS = {
        'Connection': 'keep-alive',
        'Origin': 'https://wx.qq.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'https://wx.qq.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'multipart/form-data'
    }

    # 上传文件的最大限制，单位是 byte
    UPLOAD_CHUNK_MAX_SIZE = 524288

    def __init__(self):
        self.s = requests.session()
        self.s.verify = False
        self.s.headers = self.DEFAULT_HEADERS

        self.stopped = False   # 程序是否停止
        self.member_list = []  # 联系人列表
        self.public_list = []  # 公众账号列表
        self.group_list = []  # 群聊列表
        self.special_list = []  # 特殊账号列表
        self.friend_list_other = []  # 非男非女好友
        self.friend_list_male = []  # 男性好友
        self.friend_list_female = []  # 女性好友
        self.contact_list = []  # 所有好友
        self.group_member_dict = {}  # 群聊成员

        self.MediaId = ''
        self.sync_check_ = int(get_13_time())

    @property
    def proxies(self):
        return self.s.proxies

    @proxies.setter
    def proxies(self, proxies):
        self.s.proxies = proxies

    def get_wx_uuid(self):
        params = {
            'appid': 'wx782c26e4c19acffb',
            'redirect_uri': 'https://login.wx2.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage',
            'fun': 'new',
            'lang': 'zh_CN',
            '_': get_13_time,
        }

        r = self.s.get(self.WX_URLS['jslogin'] % parse.urlencode(params))
        text = r.text
        regex = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)"'
        matches = re.search(regex, text)
        if matches and matches.group(1) == '200':
            uuid = matches.group(2)
            self.uuid = uuid
            return True, uuid
        return False, ''

    def gen_qr_code(self):
        qr_code_path = os.path.join(os.getcwd(), 'qrcode.jpg')
        r = self.s.get(self.WX_URLS['qrcode'] % self.uuid)
        with open(qr_code_path, 'wb') as f:
            f.write(r.content)

        return True

    def wait_for_login_until_success_or_timeout(self):
        n = 60
        while n > 0:
            b, code = self.wait_for_login()
            if b and code == 200:
                return True

            n -= 1
            time.sleep(3)

        return False

    def wait_for_login(self, tip=1):
        print("等待登录中。。。。。。")
        try:
            r = self.s.get(self.WX_URLS['login'] % (tip, self.uuid, get_13_time()))
            text = r.text
            matches = re.search(r'window.code=(\d+);', text)
            code = int(matches.group(1))
        except:
            code = 408

        # window.code=200;
        # window.redirect_uri="https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=AyPPydglb9whniF9K_joE5nP@qrticket_0&uuid=QbCvMofYuA==&lang=zh_CN&scan=1499220301";
        if code == 201:  # 手机扫描识别成功
            return True, code
        if code == 200:  # 确认按钮点击成功
            matches = re.search(r'window.redirect_uri="(\S+?)";', text)
            # self.redirect_uri = matches.group(1) + '&fun=new&version=v2&lang=zh_CN'
            self.redirect_uri = matches.group(1)
            self.base_uri = self.redirect_uri[:self.redirect_uri.rfind('/')]
            temp_host = self.base_uri[8:]
            self.base_host = temp_host[:temp_host.find("/")]
            return True, code
        if code == 408: # 未扫描
            return False, code
        return False, code

    def is_stopped(self):
        return self.stopped

    def logon_out(self):
        print("登出微信。。。。。。")
        url = self.base_uri + '/webwxlogout?redirect=1&type=0&skey=%s' % self.skey
        params = {
            'sid': self.wxsid,
            'uid': self.wxuin
        }
        self.s.get(url, params=params)

    def finish(self):
        self.stopped = True
        self.logon_out()
        print("发送结束")

    def start_sync_check_loop_thread(self):
        self.sync_check_thread = threading.Thread(target=self.loop_sync_check, args=())
        self.sync_check_thread.start()

    def loop_sync_check(self):
        print("开始循环发送sync_check")
        while not self.is_stopped():
            self.sync_check()
            time.sleep(10)
        print("结束循环发送sync_check")

    def sync_check(self, host=''):
        text = ''
        try:
            self.sync_check_ += 1
            params = {
                'r': get_13_time(),
                'sid': self.wxsid,
                'uin': self.wxuin,
                'skey': self.skey,
                'deviceid': self.get_deviceId(),
                'synckey': self.sync_key,
                '_': self.sync_check_,
            }

            url = 'https://webpush.' + self.base_host + '/cgi-bin/mmwebwx-bin/synccheck?%s' % parse.urlencode(params)
            self.DEFAULT_HEADERS['Referer'] = 'https://wx2.qq.com/?&lang=zh_CN'
            r = self.s.get(url, headers=self.DEFAULT_HEADERS)

            text = r.text
            # matches = re.search(r'window.synccheck=\{retcode:"(\d+)",selector:"(\d+)"\}', content)
            # return matches.group(1), matches.group(2)
        except Exception as e:
            if text:
                save_error_to_log(text, 'sync_check')
            raise e

    def login(self):
        print("检测登录状态。。。。。。")
        # 301，不自动跳转
        r = self.s.get(self.redirect_uri, allow_redirects=False)
        text = r.text

        if text.startswith('<error><ret>1203</ret>'):
            print('微信小号，不让登录网页版本')
        else:
            bs = BeautifulSoup(text, 'lxml')
            self.skey = bs.find('skey').text
            self.wxsid = bs.find('wxsid').text
            self.wxuin = bs.find('wxuin').text
            self.pass_ticket = bs.find('pass_ticket').text

        if all((self.skey, self.wxsid, self.wxuin, self.pass_ticket)):
            return True
        else:
            save_error_to_log(text, 'login')
            print("检测登录状态未知异常，查看日志。。。。。。")
        return False

    def get_deviceId(self):
        return 'e' + repr(random.random())[2:17]

    def get_base_request(self):
        return {'Skey': self.skey, 'Sid': self.wxsid, 'Uin': int(self.wxuin), 'DeviceID': self.get_deviceId()}

    def wx_init(self):
        print("初始化。。。。。。")
        text = ''
        try:
            url = self.base_uri + '/webwxinit?r=%s' % str(~int(time.time()))
            r = self.s.post(url, json={'BaseRequest': self.get_base_request()})
            r.encoding = 'UTF-8'
            text = r.text
            json_data = json.loads(text)
            self.my_account = json_data['User']
            print('昵称：%s 登录成功' % self.my_account['NickName'])
            self.SyncKey = json_data['SyncKey']
            self.sync_key = '|'.join([str(item['Key']) + '_' + str(item['Val']) for item in self.SyncKey['List']])
            self.group_list = [member for member in json_data['ContactList'] if member['UserName'].startswith('@@')]
            return json_data['BaseResponse']['Ret'] == 0
        except Exception as e:
            if text:
                save_error_to_log(text, 'wx_init')
            raise e

    def wx_notify(self):
        print("开启通知中。。。。。。")
        text = ''
        try:
            url = self.base_uri + '/webwxstatusnotify'
            params = {
                "Code": 3,
                'BaseRequest': self.get_base_request(),
                "FromUserName": self.my_account['UserName'],
                "ToUserName": self.my_account['UserName'],
                "ClientMsgId": int(get_13_time())
            }
            r = self.s.post(url, params)
            text = r.text
            json_data = json.loads(text)
            return json_data['BaseResponse']['Ret'] == 0
        except Exception as e:
            if text:
                save_error_to_log(text, 'wx_notify')
            raise e

    def wx_getcontact(self):
        print("获取联系人。。。。。。")
        text = ''
        try:
            dic_list = []
            b = True
            seq = 0
            while b:
                url = '%s/webwxgetcontact?pass_ticket=%s&r=%s&seq=%s&skey=%s' % (
                    self.base_uri, self.pass_ticket, get_13_time(), seq, self.skey)
                r = self.s.get(url)
                r.encoding = 'UTF-8'
                text = r.text
                dic = json.loads(text)

                dic_list.append(dic)
                if int(dic["Seq"]) == 0:
                    b = False
                else:
                    seq = dic["Seq"]

            for dic in dic_list:
                self.member_list.extend(dic['MemberList'])

            return True

        except Exception as e:
            if text:
                save_error_to_log(text)
            raise e

    def insert_member_into_mysql(self):
        insert_list = []
        my_user_name = self.my_account['UserName']
        insert_list.extend([[my_user_name, m['UserName'], m['NickName'], m['Sex'], '0'] for m in self.special_list])
        insert_list.extend([[my_user_name, m['UserName'], m['NickName'], m['Sex'], '1'] for m in self.contact_list])
        insert_list.extend([[my_user_name, m['UserName'], m['NickName'], m['Sex'], '2'] for m in self.group_list])
        insert_list.extend([[my_user_name, m['UserName'], m['NickName'], m['Sex'], '8'] for m in self.public_list])

        sql = 'insert into member(user_name, member_user_name, member_nick_name, sex, member_type) values(%s, %s, %s, %s, %s)'
        insert_many(sql, insert_list)

    def split_member(self):
        print("联系人分组中。。。。。。")
        special_users = ['newsapp', 'fmessage', 'filehelper', 'weibo', 'qqmail',
                         'fmessage', 'tmessage', 'qmessage', 'qqsync', 'floatbottle',
                         'lbsapp', 'shakeapp', 'medianote', 'qqfriend', 'readerapp',
                         'blogapp', 'facebookapp', 'masssendapp', 'meishiapp',
                         'feedsapp', 'voip', 'blogappweixin', 'weixin', 'brandsessionholder',
                         'weixinreminder', 'wxid_novlwrv3lqwv11', 'gh_22b87fa7cb3c',
                         'officialaccounts', 'notification_messages', 'wxid_novlwrv3lqwv11',
                         'gh_22b87fa7cb3c', 'wxitil', 'userexperience_alarm', 'notification_messages']

        for contact in self.member_list:
            if contact['UserName'] in special_users:  # 特殊账户
                self.special_list.append(contact)
            elif contact['VerifyFlag'] & 8 != 0:  # 公众号
                self.public_list.append(contact)
            elif contact['UserName'].startswith('@@'):  # 群聊
                self.group_list.append(contact)
            else:
                # 男性
                if 1 == contact['Sex']:
                    self.friend_list_male.append(contact)
                # 女性
                elif 2 == contact['Sex']:
                    self.friend_list_female.append(contact)
                else:
                    self.friend_list_other.append(contact)

                self.contact_list.append(contact)

        self.insert_member_into_mysql()

    def webwxsync(self):
        text = ''
        try:
            url = self.base_uri + '/webwxsync?sid=%s&skey=%s&lang=zh_CN&pass_ticket=%s' % (
                self.wxsid, self.skey, self.pass_ticket)

            data = {
                'BaseRequest': self.get_base_request(),
                'SyncKey': self.SyncKey,
                'rr': ~int(time.time())
            }
            r = self.s.post(url, data)
            text = r.text
            json_data = json.loads(text)

            if json_data['BaseResponse']['Ret'] == 0:  # 更新同步键
                self.SyncKey = json_data['SyncKey']
                SyncKey = json_data['SyncCheckKey'] or json_data['SyncKey']
                self.sync_key = '|'.join([str(item['Key']) + '_' + str(item['Val']) for item in SyncKey['List']])
            return json_data
        except Exception as e:
            if text:
                save_error_to_log(text)
            raise e

    '''
        获取群聊的成员列表
    '''
    def wx_batchget_contact(self, group_list=None):
        text = ''
        try:
            group_list = group_list or [{'UserName': g['UserName'], 'EncryChatRoomId': ''} for g in self.group_list]
            url = '%s/webwxbatchgetcontact?type=ex&r=%s&lang=zh_CN&pass_ticket=%s' % (
                self.base_uri, int(time.time()), self.pass_ticket)
            params = {
                'BaseRequest': self.get_base_request(),
                'Count': len(group_list),
                'List': group_list
            }
            r = self.s.post(url, json=params)
            r.encoding = 'UTF-8'
            text = r.text
            json_data = json.loads(text)
            old_group_list = [g['UserName'] for g in self.group_list]
            for group in json_data['ContactList']:
                self.group_member_dict[group['UserName']] = group['MemberList']
                if group['UserName'] not in old_group_list:
                    del group['MemberList']
                    self.group_list.append(group)

            return json_data['BaseResponse']['Ret'] == 0
        except Exception as e:
            if text:
                save_error_to_log(text)
            raise e

    def upload_media(self, file_path, to_user_name='filehelper'):
        print("上传图片中。。。。。。")
        # if not os.path.exists(pic_path):
        #     print('[ERROR] File not exists.')
        #     return False

        file_size = os.path.getsize(file_path)

        file_symbol = 'pic'

        with open(file_path, 'rb') as f:
            file_md5 = hashlib.md5(f.read()).hexdigest()

        file_ = open(file_path, 'rb')
        try:
            # ceil 就是向上取整
            chunks = math.ceil(file_size/self.UPLOAD_CHUNK_MAX_SIZE)
            upload_media_request = json.dumps(OrderedDict([
                ('UploadType', 2),
                ('BaseRequest', self.get_base_request()),
                ('ClientMediaId', int(get_13_time())),
                ('TotalLen', file_size),
                ('StartPos', 0),
                ('DataLen', file_size),
                ('MediaType', 4),
                ('FromUserName', self.my_account['UserName']),
                ('ToUserName', to_user_name),
                ('FileMd5', file_md5)]
            ))

            for chunk in range(chunks):
                r = self.upload_chunk_file(file_path, file_symbol, file_size,
                                                 file_, chunk, chunks, upload_media_request)
                text = r.text
                MediaId = json.loads(text)['MediaId']
                if MediaId:
                    self.MediaId = MediaId
                    print("上传图片成功。。。。。。")
                    return MediaId
        finally:
            file_.close()

        print("上传图片失败。。。。。。")
        return False

    def upload_chunk_file(self, file_path, file_symbol, file_size, file, chunk, chunks, uploadMediaRequest):
        url = 'https://file.' + self.base_host + '/cgi-bin/mmwebwx-bin/webwxuploadmedia?f=json'
        file_name = os.path.basename(file_path)
        file_type = mimetypes.guess_type(file_name)[0] or 'application/octet-stream'
        files = OrderedDict([
            ('id', (None, 'WU_FILE_0')),
            ('name', (None, file_name)),
            ('type', (None, file_type)),
            ('lastModifiedDate', (None, time.strftime('%a %b %d %Y %H:%M:%S GMT+0800 (CST)'))),
            ('size', (None, str(file_size))),
            ('chunks', (None, str(chunks))),
            ('chunk', (None, str(chunk))),
            ('mediatype', (None, file_symbol)),
            ('uploadmediarequest', (None, uploadMediaRequest)),
            ('webwx_data_ticket', (None, self.s.cookies['webwx_data_ticket'])),
            ('pass_ticket', (None, self.pass_ticket)),
            ('filename', (file_name, file.read(self.UPLOAD_CHUNK_MAX_SIZE), 'application/octet-stream'))])
        if chunks == 1:
            del files['chunk']
            del files['chunks']
        return self.s.post(url, files=files, headers=self.UPLOAD_FILE_HEADERS)

    def send_pic_and_msg(self, MediaId, content, uid):
        b = True
        code = -110
        if MediaId:
            b, code = self.send_img_msg_by_uid(self.MediaId, uid)

        if b and content:
            b, code = self.send_msg_by_uid(content, uid)

        return b, code

    def send_img_msg_by_uid(self, MediaId, uid):
        code = -110
        url = self.base_uri + '/webwxsendmsgimg?fun=async&f=json'
        data = {
            'BaseRequest': self.get_base_request(),
            'Msg': {
                'Type': 3,
                'MediaId': MediaId,
                'Content': '',
                'FromUserName': self.my_account['UserName'],
                'ToUserName': uid,
                'LocalID': str(time.time() * 1e7),
                'ClientMsgId': str(time.time() * 1e7),},}
        if self.pic[-4:] == '.gif':
            url = self.base_uri + '/webwxsendemoticon?fun=sys'
            data['Msg']['Type'] = 47
            data['Msg']['EmojiFlag'] = 2

        r = self.s.post(url, data=json.dumps(data))
        text = r.text
        res = json.loads(text)
        code = res['BaseResponse']['Ret']
        if code == 0:
            self.webwxsync()
            return True, code
        # 频繁
        elif code == 1205:
            return False, code
        elif code == -1 or code == 1101:
            return False, code
        else:
            save_error_to_log(text, 'send_img_msg_by_uid')
            return False, code

    def send_msg_by_uid(self, text, uid):
        url = self.base_uri + '/webwxsendmsg'
        ClientMsgId = str(int(time.time())) + str(random.random() * 10000000)[0:7]
        params = {
            'BaseRequest': self.get_base_request(),
            'Msg': {'ClientMsgId': ClientMsgId, 'Content': text, 'FromUserName': self.my_account['UserName'],
                    'LocalID': ClientMsgId, 'ToUserName': uid, 'Type': 1},
            'Scene': 0
        }
        data = json.dumps(params, ensure_ascii=False).encode('utf8')
        r = self.s.post(url, data=data)
        text = r.text
        res = json.loads(text)
        ret = res['BaseResponse']['Ret']
        if ret == 0:
            self.webwxsync()
            return True, ret
        elif ret == 1205:
            print("发送文字信息繁忙")
        elif ret == -1:
            pass
        else:
            print("发送信息未知错误")
            save_error_to_log(text, 'send_msg')

        return False, ret

    def start_send(self, content, pic='', send_group=True, send_Friend=True, sex_type='0'):
        if pic:
            self.pic = pic
            self.upload_media(pic)
        else:
            self.pic = ''
            self.MediaId = ''

        code = -110
        # 微信群
        if send_group:
            for m, member in enumerate(self.group_list):
                if not member['NickName'].startswith('Terry'):
                    continue
                b, code = self.send_pic_and_msg(self.MediaId, content, member['UserName'])

                if code == 1205:
                    print("群图片发送频繁，共发送 %s 个 " % str(m + 1))
                    break
                elif code == 1101:
                    print("账号失效，需要重新扫描二维码，共发送 %s 个 " % str(m + 1))
                    return

        # 好友
        if send_Friend:
            if sex_type == '1':
                send_friend_list = self.friend_list_male
            elif sex_type == '2':
                send_friend_list = self.friend_list_female
            else:
                send_friend_list = self.contact_list

            for n, member in enumerate(send_friend_list):
                if member['NickName'] != 'shinejie':
                    continue

                b, code = self.send_pic_and_msg(self.MediaId, content, member['UserName'])
                if code == 1205:
                    print("好友发送频繁，发送 %s 个" % str(n + 1))
                    break
                elif code == 1101:
                    print("账号失效，需要重新扫描二维码，共发送 %s 个 " % str(m + 1))
                    break

    def init_all_env(self):
        if self.login():
            self.wx_init()
            self.wx_notify()
            self.wx_getcontact()
            # self.wx_batchget_contact()
            self.split_member()
            self.start_sync_check_loop_thread()
            self.webwxsync() #
        else:
            print('登录错误！')

if __name__ == '__main__':
    import urllib3
    urllib3.disable_warnings()

    wx = WeiXinRobot()
    # wx.proxies = {'https': '127.0.0.1:8888'}

    b, uuid = wx.get_wx_uuid()
    if b:
        wx.gen_qr_code()
        b = wx.wait_for_login_until_success_or_timeout()
        if b:
            wx.init_all_env()

            content = '测试微信机器人'
            pic = os.path.join(os.getcwd(), 'qrcode.jpg')

            wx.start_send(content, pic)
    else:
        print('微信访问错误')

    wx.finish()
    print('执行结束')
