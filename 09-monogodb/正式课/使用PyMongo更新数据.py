from pymongo import MongoClient

client = MongoClient()
db = client.test

result = db.restaurants.update_one(
    {"name": "Vella"},
    {
        "$set": {
            "cuisine": "American (New)"
        },
        "$currentDate": {"lastModified": True}
    }
)