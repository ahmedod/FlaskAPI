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

    def add_element_to_thesaurus(self, element, thesaurus_name):
        """TO DO
        """
        try:
            data = self.model.objects(name=thesaurus_name).get()
            data.thesaurus_data.append(element)
            data.save()
        except ExceptionModel as err:
            raise ExceptionModel("query failed : {}".format(err))

    def delete_element_from_thesaurus(self, element, thesaurus_name):
        """TO Do
        """
        try:
            self.model.objects(
                name=thesaurus_name).update(
                pull__thesaurus_data=element)
        except ExceptionModel as err:
            raise ExceptionModel("query failed : {}".format(err))
