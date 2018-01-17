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

    <link rel="icon" href="https://i.alipayobjects.com/common/favicon/favicon.ico 

" type="image/x-icon" />
    <link rel="shortcut icon" href="https://i.alipayobjects.com/common/favicon/favicon.ico 

" type="image/x-icon" />
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
                    <li class="on first"><a href="https://www.alipay.com/i/indexNew.htm 

" target="_blank" seed="">个人</a></li>
                    <li><a href="https://b.alipay.com/?ynsrc=zhuzhanB 

" target="_blank" seed="">企业</a></li>
                    <li><a href="http1s://open.alipay.com/platform/home.htm?from=zhuzhanKFZ20160818 

" target="_blank" seed="">合作伙伴</a></li>
                </ul>
                <ul class="fr rlink">

                    <li><a href="https://mobile.alipay.com/index.htm 

" target="_blank" seed="">支付宝APP</a></li>
                    <li><span>|</span></li>
                    <li class="am-service">
                      <a class="down-a" href="javascript:;">客户服务<i class="arrow-down"></i></a>
                        <div class="downlist">
                            <div class="">

                              <a href="https://help.alipay.com/lab/index.htm 

" target="_blank">服务大厅</a>

                              <a href="https://cshall.alipay.com/lab/selfHelp.htm 

" target="_blank">自助服务</a>

                              <a href="https://egg.alipay.com/ 

" target="_blank">提建议</a>

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
soup = BeautifulSoup(html_doc,'lxml')
# text = '<a></b></a>'
# soup_test = BeautifulSoup(text,'lxml') #会补全html body和p
# print('lxml:')
# print(soup_test)

# print(soup.prettify()) #直接输出文档，str类型，默认utf-8
# print(soup.prettify('gbk')) #传入编码，输出bytes
# print(soup.prettify('gbk').decode('gbk')) #传入编码，输出bytes

print(soup.title)  #标签，包括标签本身
print(soup.title.name) #标签的名字
print(soup.title.string) #标签的内容
print(soup.title.text) #标签的内容 str对象

print(soup.meta) #标签
print(soup.meta['charset']) #标签属性

print(soup.meta.parent.name) #标签的父标签
print(soup.html.parent.name)
print(soup.html.parent.parent)

text = '''
<a><b>text1</b><c>text2</c>
<d>text3</d><e e1='100/><f f1='101'/></a>
'''

sibling_soup = BeautifulSoup(text,'lxml')
print(sibling_soup.b.next_sibling) #兄弟节点
print(sibling_soup.c.previous_sibling) #兄弟节点
print(sibling_soup.c.next_sibling)  #兄弟节点 是换行符
print(sibling_soup.d.previous_sibling)  #兄弟节点 是换行符
print('结束')
print(sibling_soup.a.next_element) #下个元素 是<b>text1</b>
print(sibling_soup.b.next_element) #下个元素 text
print(sibling_soup.b.next_element.next_element) #下个元素 是换行符
print(sibling_soup.d.previous_element) #上个元素 是换行符
# print(sibling_soup.f1.previous_element) #上个元素 是<e e1='100'/>
print('结束')

print(soup.find_all('meta')) #查找所有
print(soup.find_all('meta',limit=2)) #查找2个
print(soup.find('meta',{'name':'renderer'}))
print(soup.find_all('meta',{'name':'renderer'},limit=1))

print(soup.find(id='seajsnode'))

print(soup.find(text='支付宝 知托付！'))
print(soup.find(text='支付宝 知托付！',test = 'test'))
print(soup.find('title',text='支付宝 知托付！'))