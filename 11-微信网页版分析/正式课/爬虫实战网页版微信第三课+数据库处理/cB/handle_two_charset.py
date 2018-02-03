
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

content = b'\xb2\xe2\xca\xd4\xd6\xd0\xce\xc4   \xe6\xb5\x8b\xe8\xaf\x95\xe4\xb8\xad\xe6\x96\x87'
content_list = content.split(' ')
print(content_list)
# print(content.decode('utf-8', 'ignore'))
# print(content.decode('utf-8'))
content_array = bytearray(content)

'''
思路就是：
1、先按一种编码进行处理，譬如先进行UTF-8处理，得到部分数据
2、取得这个剩下出错部分的bytes，进行另外的编码处理s
'''