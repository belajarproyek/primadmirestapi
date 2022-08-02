from app.models.anggotas import database
from flask import Flask, jsonify, request
from flask_jwt_extended import *
import json
import datetime

mysqldb = database()


@jwt_required()
def shows():
    dbresult = mysqldb.showUsers()
    result = []
    print(dbresult)
    for items in dbresult:
        user = {
            "id": items[0],
            "nama": items[1],
            "tgl_lahir": items[2],
            "alamat": items[3],
            "jenis_kelamin": items[4],
            "email": items[5]

        }
        result.append(user)

    return jsonify(result)


def show(**params):
    dbresult = mysqldb.showUserById(**params)
    user = {
        "id": dbresult[0],
        "nama": dbresult[1],
        "tgl_lahir": dbresult[2],
        "alamat": dbresult[3],
        "jenis_kelamin": dbresult[4],
        "email": dbresult[5],
    }

    return jsonify(user)


def insert(**params):
    mysqldb.insertUser(**params)
    mysqldb.dataCommit()
    return jsonify({"message": "Success"})


def update(**params):
    mysqldb.updateUserById(**params)
    mysqldb.dataCommit()
    return jsonify({"message": "Success"})


def delete(**params):
    mysqldb.deleteUserById(**params)
    mysqldb.dataCommit()
    return jsonify({"message": "Success"})


def token(**params):
    dbresult = mysqldb.showUserByEmail(**params)
    if dbresult is not None:
        user = {
            "nama": dbresult[1],
            "email": dbresult[5]
        }
        expires = datetime.timedelta(days=1)
        expires_refresh = datetime.timedelta(days=3)
        access_token = create_access_token(
            user, fresh=True, expires_delta=expires)

        data = {
            "data": user,
            "token_access": access_token
        }
    else:
        data = {
            "message": "Email tidak terdaftar"
        }

    return jsonify(data)
