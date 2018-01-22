'''
一、关系型数据库和非关系型数据库
数据库就是一个数据的持久化，保存到硬盘
基本操作就是增、删、改、查
1、关系型数据库：mssql、mysql、oracle、db2等等，通过SQL语句进行数据库的操作
ACID原则，基于事务
A:原子性
C:一致性
I:独立性
D:持久性
存储过程、触发器、自定义的函数
2、非关系型数据库：NoSQL(not only sql) 基于文件存储，格式是BSON(binary son) 没有太多的规范
方便扩展

二、mongodb
C++写的，也是跨平台的，但是不同的平台要重新编译
有函数，但是是JavaScript写的
也是有索引的，高频率查询的字段一定要建立索引
支持语音非常多

工具：
mongo3
mongohub
rockmongo
mongodb compass

mongodb中，填写的是json字符串
key-value键值对进行保存的
key:字符串组成
value:字符串，数字，null，列表([])，另一个json


三、数据库操作库
1、pymongo
2、mongoengine

四、封装
1、可移植性高，对内的接口是不变的，只需要修改db模块
2、业务模块，只需要知道你的db模块暴露的api或者叫接口

'''

from bson import ObjectId
from pymongo import MongoClient

# 创建一个连接
# client = MongoClient('localhost',27017)
client = MongoClient() #默认参数即localhost接口和27017端口

# 访问数据库对象
db = client.primer
# db = client['primer'] #使用字典形式访问数据库

# 访问集合对象
print(db.dataset)
print(db['dataset'])

