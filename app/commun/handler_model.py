""" Handler model module"""
import datetime
import json

from bson import ObjectId
from mongoengine.queryset.visitor import Q

import models
from exceptions import ExceptionModel
from manager import ManageDb

class ModelHandler(ManageDb):
    """ Handler object with specific query"""

    def __init__(self):
        self.model = models.Cv
        super().__init__(self.model)