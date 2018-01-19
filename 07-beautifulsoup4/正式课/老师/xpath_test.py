#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

'''
    xpath
    nodename	 选取此节点的所有子节点。
    /	        从根节点选取。
    //	        从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
    .	        选取当前节点。
    ..	        选取当前节点的父节点。
    @          选取属性
    *	        匹配任何元素节点。
    @*	        匹配任何属性节点。
    node()     配任何类型的节点
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
    <a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>
    <a class="sister" href="http://example.com/lacie" id="link2">
     Lacie
    </a>
    and
    <a class="sister" href="http://example.com/tillie" id="link2">
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
from lxml import etree

# tree = etree.HTML(html_doc) # 会自动补全 html 标签
# print(etree.tostring(tree, encoding="utf-8").decode('utf-8'))
# tree = etree.fromstring(html_doc)
# print(etree.tostring(tree, encoding="utf-8").decode('utf-8'))
# tree = etree.XML(html_doc)
# print(etree.tostring(tree, encoding="utf-8").decode('utf-8'))


# tree = etree.HTML(html_doc)
# print(tree.xpath('//title')[0].text) # 节点内容
# print(tree.xpath('//title')[0].tag)  # 节点名
# print(tree.xpath('//p[@class="story"]')[1].text)
#
# print(etree.tostring(tree.xpath('//title')[0]))  # etree.tostring 输出节点全部信息
#
# print(tree.xpath('//title')[0].getparent().tag)  # 父节点
#
# print(tree.xpath('//a')[1].get('class'))  # 获取属性
# print(tree.xpath('//a')[1].attrib)  # 所有属性的字典
#
# print(tree.xpath("//text()")) # 所有字符串，列表形式
# print(tree.xpath("//text()")[2]) # 所有字符串，列表形式
#
# print(tree.xpath("string()")) # 所有文本，字符串 类型，以单一标签为分界，如 <br/>
