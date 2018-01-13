'''
模拟登陆 提交post请求 验证成功 返回首页
微博post请求
location.replace

1.预登陆 给服务器提交账号 服务器返回一些post请求参数
user_url = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=MTUxNjgyMzA2NDQ%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.19)&_=1515674933152'

2.提交账号密码参数 服务器返回一个跳转的地址 必须要跳转 不然不成功
post_url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'


post返回的url:
https://login.sina.com.cn/crossdomain2.php?action=login&entry=weibo&r=https%3A%2F%2Fpassport.weibo.com%2Fwbsso%2Flogin%3Fssosavestate%3D1547210886%26url%3Dhttps%253A%252F%252Fweibo.com%252Fajaxlogin.php%253Fframelogin%253D1%2526callback%253Dparent.sinaSSOController.feedBackUrlCallBack%2526sudaref%253Dweibo.com%26display%3D0%26ticket%3DST-MjIzOTA1MzQzNQ%3D%3D-1515674886-gz-24A7FAA2DAC5783E50EA159021E9D6C8-1%26retcode%3D0&sr=1920%2A1080

找到加密的地方

'''