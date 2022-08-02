from pymongo import MongoClient
from bson.objectid import ObjectId

class database:
    def __init__(self):
        try:
            self.nosql_db = MongoClient()
            self.db = self.nosql_db.primadmi
            self.mongo_col = self.db.instansis
            print("database connected")
        except Exception as e:
            print(e)
    
    def showInstansis(self):
        result = self.mongo_col.find()
        return [item for item in result]
    
    def showInstansiById(self,**params):
        result = self.mongo_col.find_one({"_id":ObjectId(params["id"])})
        return result
    
    def searchInstansiByName(self, **params):
        query = {"nama" : {"$regex": "{0}".format(params["nama"]), "$options": "i"}}
        result = self.mongo_col.find(query)
        return result
    
    def insertInstansi(self,document):
        self.mongo_col.insert_one(document)
    
    def updateInstansiById(self,**params):
        query_1 = {"_id":ObjectId(params["id"])}
        query_2 = {"$set": params["data"]}
        self.mongo_col.update_one(query_1,query_2)
    
    def deletInstansiById(self, **params):
        query = {"_id":ObjectId(params["id"])}
        self.mongo_col.delete(query)