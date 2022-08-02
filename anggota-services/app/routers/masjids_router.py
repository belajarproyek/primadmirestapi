from app import app
from app.controllers import masjids
from flask import Blueprint, request

masjids_blueprint = Blueprint('masjids_router', __name__)

@app.route("/masjids", methods=["GET"])
def showMasjids():
    return masjids.shows()

@app.route("/masjids/insert", methods=["POST"])
def insertMasjid():
    params = request.json
    return masjids.add(**params)

@app.route("/masjids/status", methods=["POST"])
def changeMasjid():
    params = request.json
    return masjids.changeStatus(**params)