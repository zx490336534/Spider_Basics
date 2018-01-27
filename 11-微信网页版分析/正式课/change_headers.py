from urllib.parse import parse_qsl

def print_headers_raw_to_dict(headers_raw_l):
    print("{\n    '" + ",\n    ".join(map(lambda s: "'" +
        "': '".join(s.strip().split(': ')) + "'", headers_raw_l))[1:-1] + "'\n}")

def print_headers_raw_to_dict_space(headers_raw_l):
    print("{\n    '" + ",\n    ".join(map(lambda s: "'" + "': '".join(s.strip().split('\t')) + "'", headers_raw_l))[1:-1] + "'\n}")

def print_dict_from_copy_headers(headers_raw):
    headers_raw = headers_raw.strip()
    headers_raw_l = headers_raw.splitlines()

    if 'HTTP/1.1' in headers_raw_l[0]:
        headers_raw_l.pop(0)
    if headers_raw_l[0].startswith('Host'):
        headers_raw_l.pop(0)
    if headers_raw_l[-1].startswith('Cookie'):
        headers_raw_l.pop(-1)

    if ':' in headers_raw_l[0]:
        print_headers_raw_to_dict(headers_raw_l)
    else:
        print_headers_raw_to_dict_space(headers_raw_l)

def print_url_params(url_params):
    s = str(parse_qsl(url_params.strip(), 1))
    print("OrderedDict(\n    " + "),\n    ".join(map(lambda s: s.strip(), s.split("),")))[1:-1] + ",\n)")


if __name__ == '__main__':
    text = '''
	GET /otn/leftTicket/log?leftTicketDTO.train_date=2018-02-13&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CSQ&purpose_codes=ADULT HTTP/1.1
Host: kyfw.12306.cn
Connection	keep-alive
Cache-Control	no-cache
Accept	application/json, text/javascript, */*; q=0.01
If-Modified-Since	0
User-Agent	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36
Referer	https://kyfw.12306.cn/otn/leftTicket/init
Accept-Encoding	gzip, deflate, sdch
Accept-Language	zh-CN,zh;q=0.8
Cookie	JSESSIONID=14E3D608CF07BA70F289D01E393C7E50; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=200278538.64545.0000; RAIL_EXPIRATION=1516530260973; RAIL_DEVICEID=f2T-YHHOVgWxXsYXPoB8g7UjWxVhf9LzmzfowiB7x2P-GkCEJhf2RN_7kuULxRf6hyPXYkYac7gFyDGX6MCKruYPxYJFqphkWSqYvcj7YCCkVoj8p0lih_m_7NjXlQK2MzWaUD9aFIFe64cyWO2KLmwSt-2IsihU; current_captcha_type=Z; acw_tc=AQAAAAdFGgkAfQIAwLz+Z7kcj9pHaWAk; _jc_save_fromDate=2018-02-13; _jc_save_toDate=2018-02-13; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u957F%u6C99%2CCSQ; _jc_save_wfdc_flag=dc
    '''
print_dict_from_copy_headers(text)

text_1 = '''
appid	wx782c26e4c19acffb
redirect_uri	https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage
fun	new
lang	zh_CN
_	1517066206221
'''
print_dict_from_copy_headers(text_1)