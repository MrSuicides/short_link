import pymongo

class MongoMethods:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://mongodb:27017/")
        self._db = self.client["mydatabase"]
        self.collection = self._db["customers"]

    def insert(self, link: str, route: str):
        self.collection.insert_one({
            "link": link,
            "route": route
        })

    def collection_count(self) -> int:
        return self.collection.count_documents({})

    def remove_all_records(self):  # -> True ?
        self.collection.delete_many({})

    def search(self):  # -> True ?
        a = []
        for x in self.collection.find():
            a.append(x)
        return a
