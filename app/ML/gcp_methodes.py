import re, os, io, json
from google.cloud import storage
from google.cloud import vision
from google.cloud import storage
from google.cloud import language
from google.cloud import automl
from google.protobuf import json_format



# GCP Credentials
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'fedpoc-fb5e076a4395.json'