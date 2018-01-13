#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

from urllib import parse

# data = {
#     'a': '1',
#     'b': '2'
# }
#
# print(parse.urlencode(data))

s = '我是测试字符串'
print(parse.quote(s))

s1 = '%E6%98%AF'
print(parse.unquote(s1))
