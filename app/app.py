import os
from mongoengine import connect
from flask import Flask, request, jsonify
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from config import gcs_source_uri, gcs_destination_uri, bucket_name



MONGODB_PORT = os.environ.get("MONGODB_PORT")
MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")
MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME")
MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD")
MONGODB_HOSTNAME = os.environ.get("MONGODB_HOSTNAME")

application = Flask(__name__)
application.config['SECRET_KEY'] = 'super-secret'
application.config['JWT_ALGORITHM']= 'HS256'
jwt = JWT(application, authenticate, identity)


connect(alias='default', db=MONGODB_DATABASE, username=MONGODB_USERNAME,
        password=MONGODB_PASSWORD, host=MONGODB_HOSTNAME)



@application.route('/test')
@jwt_required()
def index():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
