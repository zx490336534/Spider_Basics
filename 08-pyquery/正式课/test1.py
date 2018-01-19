from lxml import etree
from pyquery import PyQuery as pq
from pyquery.pyquery import fromstring

'''
    pyquery,解析器基于lxml和html5lib库，符合jquery的语法进行操作
    所有基于xml的解析，heml是一种特殊的xml html5是在html基础上的
    1、加载正确编码后的文本：文本、字符串、url访问、数据库等
    2、目标定位：节点、属性、节点之间的层级关系或者相对位置
    3、获取目标：text，属性
    
    正则表达式：纯文本解析
'''
'''
命名规则，看一下PEP8
类：单个单词首字母大写
方法：全小写
属性：常量-全大写 非常量-全小写 下划线分割
'''
html_doc = '''
 <html>
  <head>
   <title>
    The Dormouse's story
   </title>
  </head>
  <body>
   <p class="title">
    <b>
     The Dormouse's story
    </b>
   </p>
   <p class="story">
    Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie 

" id="link1">
     Elsie
    </a>
    <a class="sister" href="http://example.com/lacie 

" id="link2">
     Lacie
    </a>
    and
    <a class="sister" href="http://example.com/tillie 

" id="link2">
     Tillie
    </a>
    and they lived at the bottom of a well.
   </p>
   <p class="story">
    测试中文
   </p>
  </body>
 </html>
'''

pyq_str = pq(html_doc)
head = pyq_str('head')
print(head.html())
print(head.text())

pyq_str = pq(etree.fromstring(html_doc))
head = pyq_str('head')
print(head.html())
print(head.text())

pyq_url = pq(url='http://www.baidu.com',encoding='utf-8')
head = pyq_url('head')
print(head.html())
print(head.text())

pyq_fromstring = fromstring(html_doc,'html')
print(pyq_fromstring[0].head.tag)


pyq_str = pq(html_doc)
body = pyq_str('body')
print(body.html())
print(body.text())
css = 'a[@id="link1"]'
print(pyq_str(css).attr.id)
print(pyq_str(css).attr['id'])
print(pyq_str(css).attr['class'])
print(pyq_str(css).parent()) #父标签
print('-'*20)
css_f = "p[@class='story']"
print(pyq_str(css_f).children()) #子标签

print(pyq_str(css_f).next())

print(pyq_str(css_f).next_all())