from flask import Flask, Response
import database_services.RDBService as d_service
from flask_cors import CORS
from flask import jsonify, request
import json

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from application_services.imdb_artists_resource import IMDBArtistResource
from application_services.UsersResource.user_service import UserResource

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@app.route('/imdb/artists/<prefix>')
def get_artists_by_prefix(prefix):
    res = IMDBArtistResource.get_by_name_prefix(prefix)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp


@app.route('/users', methods=["GET"])
def get_users():
    res = d_service.get_user("UserResource", "User")
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp

@app.route('/users/update', methods=["POST"])
def update_users():
    tasks = {
        'ID': 3,
        'firstName': 'aaa',
        'lastName': 'bbb',
        'email': 'aaa@gmail.com',
        'addressID': 2
    }
    # tasks = request.get_json()
    res = d_service.update_users("UserResource", "User", tasks)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


@app.route('/users/<ID>', methods=["GET"])
def get_users_by_ID(ID):
    res = d_service.get_userID("UserResource", "User", ID)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp

@app.route('/users/<ID>/address', methods=["GET"])
def get_users_address_by_ID(ID):
    res = d_service.get_address_by_userID("UserResource", "User", "Address", ID)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp

@app.route('/address', methods=["GET"])
def get_address():
    res = d_service.get_address("UserResource", "Address")
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp




# @app.route('/getUsers')
# def get_by_prefix():
#     res = d_service.get_user("UserResource", 'nameChart')
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
