""" Manage db module"""
import datetime

from exceptions import ExceptionModel


class ManageDb:
    """ Implemented method of CRUD"""

    def __init__(self, model):
        self.model = model

    def create(self, **kwargs):
        """ Create method"""
        try:
            return self.model(**kwargs).save()
        except Exception as err:
            raise ExceptionModel("ExceptionModel", err)

    def get_all(self):
        """ Get all data method"""
        try:
            return self.model.objects()
        except Exception as err:
            raise ExceptionModel("ExceptionModel", err)

    def get_by_id(self, _id, first=True):
        """ Get by id data method"""
        try:
            obj = self.model.objects(id=_id)
            if obj and first:
                return obj.first()
            return obj
        except Exception as err:
            raise ExceptionModel("ExceptionModel", err)

    def update(self, **kwargs):
        """ Update method"""
        try:
            _id = kwargs.pop('id')
            return self.model.objects(id=_id).update(**kwargs)
        except Exception as err:
            raise ExceptionModel("ExceptionModel", err)

    def delete(self, _id):
        """ Delete method"""
        try:
            return self.model.delete(_id)
        except Exception as err:
            raise ExceptionModel("ExceptionModel", err)

    def get_by_key_value(self, key, value):
        """ Get by value data method"""
        try:
            obj = self.model.objects(__raw__={key: value})
            if obj:
                return obj.first()
            return obj
        except Exception as err:
            raise ExceptionModel("ExceptionModel", err)

    def get_all_by_key_value(self, key, value):
        """ Get by value data method"""
        try:
            return self.model.objects(__raw__={key: value})
        except Exception as err:
            raise ExceptionModel("ExceptionModel", err)

    def get_by_info(self, first=False, **kwargs):
        """ Get by one or more fields"""

        try:
            result = self.model.objects(**kwargs)
            if first:
                result = result.first()
            return result
        except Exception as err:
            raise ExceptionModel("ExceptionModel", err)

    def delete_all(self):
        """ purge method"""
        try:
            return self.model.objects().delete()
        except Exception as err:
            raise ExceptionModel("ExceptionModel", err)
