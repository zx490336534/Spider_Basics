from pymongo import MongoClient

client = MongoClient()
db = client['test']
cursor = db.restaurants.find()
for i in cursor:
    print(i)

#指定相等条件
cursor = db.restaurants.find({"borough": "Manhattan"})
for i in cursor:
    print(i)

#在一个嵌入式的文档中查询
cursor = db.restaurants.find({"address.zipcode": "10075"})
for i in cursor:
    print(i)


#在一个数组中查询
cursor = db.restaurants.find({"grades.grade": "B"})
for i in cursor:
    print(i)

#大于（$gt）操作符
cursor = db.restaurants.find({"grades.score": {"$gt": 30}})
for i in cursor:
    print(i)
#小于（$lt）操作符
cursor = db.restaurants.find({"grades.score": {"$lt": 10}})
for i in cursor:
    print(i)


#组合条件
#与：逗号
cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})
for i in cursor:
    print(i)
#或：$or
cursor = db.restaurants.find({"$or": [{"cuisine": "Italian"}, {"address.zipcode": "10075"}]})
for i in cursor:
    print(i)


'''
pymongo.ASCENDING表示升序排序。
pymongo.DESCENDING表示降序排序。
'''
import pymongo
cursor = db.restaurants.find().sort([
    ("borough", pymongo.ASCENDING),
    ("address.zipcode", pymongo.ASCENDING)
])
for i in cursor:
    print(i)
