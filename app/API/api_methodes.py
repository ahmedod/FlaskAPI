""" API methodes Module"""
import json

from commun.handler_model import ThesaurusHandler


def insert_thesaurus(data_dict):
    """TO DO 
    """
    thesaurus = ThesaurusHandler()
    try:
        thesaurus.create(data_dict)
    except Exception as err:
        raise Exception("dict insersion failed: {}".format(err))
    return "thesaurus insertion with success"


def get_all_thesaurus():
    """TO DO 
    """
    thesaurus = ThesaurusHandler()
    try:
        res = thesaurus.get_all().to_json()
    except Exception as err:
        raise Exception("data fetching failed: {}".format(err))
    return res


def get_thesaurus_by_id(data):
    """TO DO 
    """
    thesaurus = ThesaurusHandler()
    try:
        res = thesaurus.get_by_id(data).to_json()
    except Exception as err:
        raise Exception("data fetching failed: {}".format(err))
    return res


def purge_thesaurus():
    """TO DO 
    """
    thesaurus = ThesaurusHandler()
    try:
        thesaurus.delete_all()
    except Exception as err:
        raise Exception("data fetching failed: {}".format(err))
    return "delete success"


def delete_thesaurus_by_id(id):
    """TO DO 
    """
    thesaurus = ThesaurusHandler()
    try:
        thesaurus.delete(id=id)
    except Exception as err:
        raise Exception("data fetching failed: {}".format(err))
    return "delete success"


def add_element(element, thesaurus_name):
    """ TO DO
    """

    thesaurus = ThesaurusHandler()
    for item in element:
        thesaurus.add_element_to_thesaurus(item, thesaurus_name)
    message = "doc updated"
    return message


def delete_element_from_thesaurus(elemnt, thesaurus_name):
    """TO DO 
    """
    thesaurus = ThesaurusHandler()
    try:
        thesaurus.delete_element_from_thesaurus(elemnt, thesaurus_name)
    except Exception as err:
        raise Exception("data fetching failed: {}".format(err))
    return "delete success"
