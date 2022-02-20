import os

import requests
from flask import Flask, Response, jsonify, request
from flask_jwt import JWT, jwt_required
from mongoengine import connect

from API.api_methodes import (add_element, delete_element_from_thesaurus,
                              delete_thesaurus_by_id, get_all_thesaurus,
                              get_thesaurus_by_id, insert_thesaurus,
                              purge_thesaurus)
from security import authenticate, identity

MONGODB_PORT = os.environ.get("MONGODB_PORT")
MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")
MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME")
MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD")
MONGODB_HOSTNAME = os.environ.get("MONGODB_HOSTNAME")

application = Flask(__name__)
application.config['SECRET_KEY'] = 'super-secret'
application.config['JWT_ALGORITHM'] = 'HS256'
jwt = JWT(application, authenticate, identity)


connect(alias='default', db=MONGODB_DATABASE, username=MONGODB_USERNAME,
        password=MONGODB_PASSWORD, host=MONGODB_HOSTNAME)


@application.route('/test')
@jwt_required()
def index():
    return {"status": True,
            "message": " Welcome too the Dockerized Flask MongoDB app!"}


@application.route('/insert', methods=['POST'])
@jwt_required()
def add_thesaurus():
    """
    This function is used to create a document.

    Returns:
        response: this return a message of status inserted document. (dict)
    """
    data = request.get_json()
    print(data)
    message = insert_thesaurus(data)
    return {"status": True, "message": message}


@application.route('/insert_element', methods=['POST'])
@jwt_required()
def add_element_to_thesaurus():
    """
    This function is used to create a document.

    Returns:
        response: this return a message of status inserted document. (dict)
    """
    data = request.get_json()
    message = add_element(data['element'], data['thesaurus_name'])
    return {"status": True, "message": message}


@application.route('/get_all', methods=['GET'])
def read_doc():
    """ TO DO
    """
    response = get_all_thesaurus()
    return Response(response, mimetype="application/json", status=200)


@application.route('/get_by_id', methods=['GET'])
def get_doc_id():
    """
    This function is used to read document by id.

    Returns:
        response: this return the document data. (dict)
    """
    id = request.args.get("doc_id")
    response = get_thesaurus_by_id(id)
    return Response(response, mimetype="application/json", status=200)


@application.route('/purgethesaurus', methods=['DELETE'])
def purge_collection():
    """
    This function is used to delete document by id.

    Returns:
        response: this return a message of status deleted document. (dict)
    """
    message = purge_thesaurus()
    return Response(message, mimetype="application/json", status=200)


@application.route('/delete_by_id', methods=['DELETE'])
def delete_doc():
    """
    This function is used to delete document by id.

    Returns:
        response: this return a message of status deleted document. (dict)
    """
    data = request.args.get("doc_id")
    response = delete_thesaurus_by_id(data)
    return response


@application.route('/delete_element', methods=['POST'])
@jwt_required()
def delete_element():
    """
    This function is used to create a document.

    Returns:
        response: this return a message of status inserted document. (dict)
    """
    data = request.get_json()
    message = delete_element_from_thesaurus(
        data['element'], data['thesaurus_name'])
    return {"status": True, "message": message}


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT,
                    debug=ENVIRONMENT_DEBUG)
