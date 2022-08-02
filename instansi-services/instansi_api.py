from pymongo import MongoClient
from models.instansi_model import database as db
import csv, json
import json
from bson import ObjectId

db = db()

def objIdToStr(obj):
    return str(obj["_id"])

def search_instansi_by_name(**params):
    data_list = []
    for instansi in db.searchInstansiByName(**params):
        instansi["_id"] = objIdToStr(instansi)
        data_list.append(instansi)
    print(data_list)
    return data_list

def search_instansis():
    data_list = []
    for instansi in db.showInstansis():
        instansi["_id"] = objIdToStr(instansi)
        data_list.append(instansi)
    return data_list

def search_instansis_id(**params):
    result = db.showInstansiById(**params)
    print(result)
    result["_id"] = objIdToStr(result)
    return result
        
def ubah_data(**params):
    try:
        db.updateInstansiById(params)
    except Exception as e:
        print(e)

# params = {
#     "id":"606ebe17a507264ac3df1d96",
#     "data":{
#         "tahunterbit":"test_1_tahun",
#         "genre":"test_1_genre"
#     }
#     }

# search_books_id(**params)