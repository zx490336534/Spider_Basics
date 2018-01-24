import pymongo

c = pymongo.MongoClient()
client = c['runoob']
db = client['col']
print(list(db.find()))

#增
db.insert({})
db.save()
#删
db.delete_one()
db.delete_many()
db.remove()
#改
db.update()