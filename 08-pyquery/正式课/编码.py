r'''
一、python3，内部都是unicode(),[unicode是规范，不是编码]体现出来的
一个是str 例如'中国人abc123'
另一个是str.encode=bytes 是bytes '\\u4e2d\xd6\xd0123abc'
如果看到乱码，就是转错码或者是iso-8859-1，不可见字符

    python3的默认编码是UTF-8

二、各种编码分析，加上unicode
1、unicode和GBK，UTF-8不是一个类型的东西 unicode是一种编码集
有17个区间，\x0000至\x10FFFF 常用的，默认的，就是第一个区间，UCS-2标准
任何字符都是2个字节   \x0030就是字符0
2、ascii码：一个字节，0-127个，\x00 到 \x7f 当今主流的编码都支持ASCII，unicode就是在前面补\x00 到 \x007f
3、iso-8859-1 西欧字符集 一个字节，在ASCII码上扩展。
URL和headers默认都是这个编码
4、GB2312：2个字节，6000多个中文，支持ASCII码 中文：\x8080 高字节和低字节都是\x80以上
5、gbk就是在gb2312的基础上扩展 2个字节 \x8000 高字节是\x80以上 低字节随便
6、UTF-8：1-4个字节，中文是3个字节，几乎用不到4个字节

三、爬虫http解码
1、url和headers都是ios-8859-1，http协议规定的
2、服务器传给客户端的时候，是一个字节串，在headers有
    content-type，charset
    head中的meta下面的charset
    如果没找到默认iso-8859-1，是一个字节的
    当你的默认编码是utf-8时候，url编码其实就是把utf-8的\x 变成 %

四、requests库
response的encoding：3种情况
1.response中有content-type的charset 那么编码是charset设置的编码
2、如果没有charset，但是有content-type这个属性，并且value中包含text，那么编码设为None
3、当以上两种都不满足，encoding='iso-8859-1'

五、怎么处理
1、排除压缩，request提交了accept-encoding：gzip,deflate,br，服务器有可能返回压缩后的数据
response的headers有content-encoding：gzip
requests不支持解压缩，肯定是乱码，去掉accept-encoding
2、response.content.decode('')       iso-8859-1，gbk，utf-8 三个中去测试

'''

#以下三种是等值的，但是建议使用s = '中'


s1 = '中'
s2 = '\u4e2d'
s3 = u'\u4e2d'
print(s1.encode('unicode_escape'))
print(s1.encode('gbk'))
#python3的默认编码是UTF-8
print(s1.encode('UTF-8'))
print(s1.encode())


#utf-8编码的字符串以iso-8859-1解码变成不可见字符(ç¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é)
import requests
r = requests.get('http://www.baidu.com')
print(r.text)

from urllib import parse
print(parse.quote(s1))
print(s1.encode('UTF-8'))
print(s1.encode('GBK'))


import chardet
s4 = b'\xe4\xb8\xad'
print(chardet.detect(s4))
print(s4.decode('ISO-8859-1'))
print(s4.decode('UTF-8'))
s5 = b'\x4e\x2d\x4e\x2d\x4e\x2d\x4e\x2d\x4e\x2d'
print(chardet.detect(s5))
print(s5.decode('ascii'))
#ascii优先，当bytes符合ascii码，不能转到其他编码
print('N-N-N-N-N-'.encode('ascii').decode('UTF-8'))