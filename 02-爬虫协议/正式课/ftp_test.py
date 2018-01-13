from ftplib import FTP


ftp = FTP()

ftp.connect('127.0.0.1',21) #建立连接

ftp.set_debuglevel(2) #输出调试信息

ftp.login(user='root',passwd='123') #登陆

ftp.encoding = 'UTF-8' #编码

file_name = 'zx.txt' #本地文件名
file = open(file_name,'wb') #写入模式打开本地文件
ftp.retrbinary('RETR zx.txt',file.write) #使用write回调函数写到本地

ftp.cwd('one/two') #切换目录
for f in ftp.nlst(): #目录下全部文件
    file = open(f, 'wb')  # 写入模式打开本地文件
    ftp.retrbinary('RETR %s' % f, file.write)  # 使用write回调函数写到本地
    file.close()

file.close()

ftp.quit() #退出ftp