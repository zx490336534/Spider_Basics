#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

from bs4 import BeautifulSoup

html_doc = '''
<!-- FD:83:homeproxy/home/personal.vm:START --><!-- FD:83:homeproxy/home/personal.vm:633:personal.schema:personal-页面标题关键字和描述:START -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="gb2312" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="renderer" content="webkit" />
    <meta name="baidu-site-verification" content="OyUb4RVdSe" />

    <title test='test'>支付宝 知托付！</title>
    <meta name="keywords" content="支付宝,电子支付/网上支付/安全支付/手机支付,安全购物/网络购物付款/付款/收款,水电煤缴费/信用卡还款/AA收款,支付宝网站">
    <meta name="description" content="支付宝，全球领先的独立第三方支付平台，致力于为广大用户提供安全快速的电子支付/网上支付/安全支付/手机支付体验，及转账收款/水电煤缴费/信用卡还款/AA收款等生活服务应用。">

    <link rel="icon" href="https://i.alipayobjects.com/common/favicon/favicon.ico" type="image/x-icon" />
    <link rel="shortcut icon" href="https://i.alipayobjects.com/common/favicon/favicon.ico" type="image/x-icon" />
<script>
seajs.pluginSDK = seajs.pluginSDK || {
  Module: {
    _resolve: function() {}
  },
  config: {
    locale: ''
  }
};
// 干掉载入 plugin-i18n.js，避免 404
seajs.config({
  map: [
	[/^.*\/seajs\/plugin-i18n\.js$/, ''],
	[/^.*\i18n!lang\.js$/, '']
  ]
});
    var token = 'sduoiweu208023@L3j123';
</script>
</head>
<body>
    <div class="header">
      <div class="am-header-inner">
        <div class="topNav">
            <div class="laymid">
                <input id='test_id' name='test_name' type='hidden' class='test_class'>测试节点</input>
                <p id="seajsnode">测试节点</p>
                <ul class="fl">
                    <li class="on first"><a href="https://www.alipay.com/i/indexNew.htm" target="_blank" seed="">个人</a></li>
                    <li><a href="https://b.alipay.com/?ynsrc=zhuzhanB" target="_blank" seed="">企业</a></li>
                    <li><a href="http1s://open.alipay.com/platform/home.htm?from=zhuzhanKFZ20160818" target="_blank" seed="">合作伙伴</a></li>
                </ul>
                <ul class="fr rlink">

                    <li><a href="https://mobile.alipay.com/index.htm" target="_blank" seed="">支付宝APP</a></li>
                    <li><span>|</span></li>
                    <li class="am-service">
                      <a class="down-a" href="javascript:;">客户服务<i class="arrow-down"></i></a>
                        <div class="downlist">
                            <div class="">

                              <a href="https://help.alipay.com/lab/index.htm" target="_blank">服务大厅</a>

                              <a href="https://cshall.alipay.com/lab/selfHelp.htm" target="_blank">自助服务</a>

                              <a href="https://egg.alipay.com/" target="_blank">提建议</a>

                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
      </div>
    </div>
</body>
</html>
'''

'''
soup = BeautifulSoup(html_doc, 'html')
#features: fast, html, html.parser, html5, html5lib, lxml, lxml-html, lxml-xml, permissive, strict, xml
fast:一般不推荐使用，不同的系统选择不同的方式
'''
# soup = BeautifulSoup(html_doc, ['lxml', 'html5'])
# soup = BeautifulSoup(html_doc, ['html', 'html5'])
soup = BeautifulSoup(html_doc, 'lxml')

'''不同builder的差异'''
# text = '<a></b></a>'
# soup_test = BeautifulSoup(text, 'lxml') # 会补全 html，body和p
# print('lxml:')
# print(soup_test)
# soup_test = BeautifulSoup(text, 'html.parser') # 会补全 p
# print('html.parser:')
# print(soup_test)
# soup_test = BeautifulSoup(text, 'html5')  # 会补全 html，head，body和p
# print('html5:')
# print(soup_test)
# soup_test = BeautifulSoup(text, 'xml')  # 会加xml头，忽略错误的标签
# print('xml:')
# print(soup_test)

# print(soup.prettify())  # 直接输出文档，str类型，默认utf-8
# print(soup.prettify('gbk')) # 传入编码，输出 bytes
# print(soup.prettify('gbk').decode('gbk')) # 传入编码，输出 bytes

# print(soup.title) # 标签，包括标签本身
# print(soup.title.name) # 标签的名字
# s = soup.title.string
# print(soup.title.string) # 标签的内容, NavigableString 对象
# print(soup.title.text) # 标签的内容， str 对象

# meta = soup.meta
# print(meta) # 标签
# print(meta['charset']) # 标签属性
# print(meta.get('charset')) # 标签属性

# print(soup.meta.parent.name) # 标签的父标签
# print(soup.html.parent.name)
# print(soup.html.parent.parent)

# text = '''
# <a><b>text1</b><c>text2</c>
# <d>text3</d><e e1='100'/><f f1='101'/><></a>
# '''
# sibling_soup = BeautifulSoup(text, 'lxml')
# print(sibling_soup.b.next_sibling) #  兄弟节点
# print(sibling_soup.c.previous_sibling) #  兄弟节点
# print(sibling_soup.c.next_sibling.next_sibling) #  兄弟节点，是 换行符
# print(sibling_soup.d.previous_sibling) #  兄弟节点，是 换行符
# print('over')

# print(sibling_soup.a.next_element) #  下一个元素，是 <b>text1</b>
# print(sibling_soup.b.next_element) #  下一个元素，是 text1
# print(sibling_soup.b.next_element.next_element) #  下一个元素，是 换行符
# print(sibling_soup.d.previous_element) #  上一个元素，是 换行符
# print(sibling_soup.f.previous_element) #  上一个元素，是 <e e1='100'/>
# print('结束')

# print(soup.find_all('meta')) # 查找所有
# print(soup.find_all('meta', limit=2)) # 查找所有 ，limit 几个
# # 查找特定的一个标签，其实也是调用的find_all，不过会在取到一个值后返回
# print(soup.find('meta', {'name': 'renderer'}))
# print(soup.find_all('meta', {'name': 'renderer'}, limit=1))
#
# # 根据id查找特定的一个标签
# print(soup.find(id="seajsnode"))
#
# print(soup.find(text='支付宝 知托付！')) # 根据标签内容查找特定的一个标签，不能仅仅有标签内容一个参数
# print(soup.find(text='支付宝 知托付！', test='test')) # 根据标签内容查找特定的一个标签，不能仅仅有标签内容一个参数
# print(soup.find('title', text='支付宝 知托付！')) # 根据标签内容查找特定的一个标签，不能仅仅有标签内容一个参数

# meta = soup.find('meta', {'name': 'renderer'})
# print(meta)
# print(meta.find_next_sibling('meta')) # 查找下个符合条件的兄弟节点
# print(meta.find_next_siblings('meta')) # 查找所有符合条件的兄弟节点
#
# print(meta.find_next_sibling('a')) # 查找下个符合条件的兄弟节点
# print(meta.find_next('a')) # 查找下个符合条件的节点
# print(meta.find_all_next('a')) # 查找所有符合条件的节点

# print(soup.find('body').get_text()) # 获取所有文本
# print(soup.find('body').get_text('|')) # 获取所有文本，| 是分隔符

'''
    标签对象一样可以使用所有方法
'''
# body = soup.find('body')
# print(body.find('div'))
# form = soup.find('form')
# var1 = form.find('var1')
# var2 = form.find('var2')
# var3 = form.find('var3')
# var4 = form.find('var4')
'''
    标签对象，可以和字符串一样编码和解码
'''
# markup = "<b>\N{SNOWMAN}</b>"
# snowman_soup = BeautifulSoup(markup, 'html.parser')
# tag = snowman_soup.b
# print(tag)
# print(tag.encode("utf-8"))
# print(tag.encode("utf-8").decode('utf-8'))
# print(tag.encode("iso-8859-1"))
# print(tag.encode("iso-8859-1").decode('iso-8859-1'))
# print(tag.encode("gbk"))
# print(tag.encode("gbk").decode('gbk'))

'''
    css选择器
'''
# print(soup.select("title")) # 标签名
# print(soup.select("html head title")) # 逐层查找
# print(soup.select("body a")) # 不逐层查找

# print(soup.select("body > a")) # >  子节点
# print(len(soup.select("body > div"))) # >  子节点
# print(soup.select("body > div")) # >  子节点
#
# print(soup.select("input ~ p")) # >  兄弟节点
#
# print(soup.select("#test_id"))  # 通过id
# print(soup.select("input#test_id"))  # 通过id
#
# print(soup.select('.test_class')) # 通过class
#
# print(soup.select('meta[charset="gb2312"]'))

