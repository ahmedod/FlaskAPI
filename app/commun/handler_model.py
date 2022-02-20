""" Handler model module"""
import datetime
import json

from bson import ObjectId
from mongoengine.queryset.visitor import Q


from commun.models import ThesaurusDict
from commun.exceptions import ExceptionModel
from commun.manager import ManageDb

class ThesaurusHandler(ManageDb):
    """ Handler object with specific query"""

    def __init__(self):
        self.model = ThesaurusDict
        super().__init__(self.model)