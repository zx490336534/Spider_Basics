from urllib import parse

data = {
    'a':'1',
    'b':'2'
}
print(parse.urlencode(data))

s = '我是测试字符'
print(parse.quote(s))

s1 = '%E6%88%91%E6%98%AF%E6%B5%8B%E8%AF%95%E5%AD%97%E7%AC%A6'
print(parse.unquote(s1))