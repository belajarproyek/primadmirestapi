from app.models.masjids import database
from app.models.anggotas import database as userdb
from flask import Flask, jsonify, request
from flask_jwt_extended import *
import json, datetime, requests

mysqldb = database()
userdb = userdb()

@jwt_required()
def shows():
    params = get_jwt_identity()
    dbresult = mysqldb.showMasjidByEmail(**params)
    result = []
    if dbresult is not None:
        for items in dbresult:
            id = json.dumps({"id":items[5]})
            instansidetail = getInstansiById(id)
            # print(bookdetail)
            user = {
                "nama" : items[0],
                "masjidid": items[1],
                "nama_masjid" : items[2],
                "alamat" : items[4],
                "id_instansi" : items[5],
                "nama_instansi" : items[6],
                "periode" : instansidetail['periode'],
                "kota" : instansidetail['kota'],
                "kecamatan": instansidetail['kecamatan']
            }
            result.append(user)
    else:
        result=dbresult
        
    return jsonify(result)

@jwt_required()
def add(**params):
    token = get_jwt_identity()
    userid = userdb.showUserByEmail(**token)[0]
    nama_masjid = params['nama']
    id = json.dumps({"id":params["id_instansi"]})
    namainstansi = getInstansiById(id)["nama"]
    params.update({"userid":userid,
                    "nama" :nama_masjid,
                    "nama_instansi" : namainstansi,
                    "isactive": 1
                })
    mysqldb.insertMasjid(**params)
    mysqldb.dataCommit()
    return jsonify({"message":"Success"})

@jwt_required()
def changeStatus(**params):
    mysqldb.updateMasjidStatus(**params)
    mysqldb.dataCommit()
    return jsonify({"message":"Success"})

    

def getInstansiById(data):
    instansi_data = requests.get(url=" http://192.168.1.9:8000/instansibyid",data=data)
    return instansi_data.json()
