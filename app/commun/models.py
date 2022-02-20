""" Models module"""
import datetime
from typing_extensions import Required

import mongoengine_goodjson as gj
from mongoengine import (CASCADE, BooleanField, ComplexDateTimeField,
                         DateTimeField, DecimalField, Document,
                         DynamicDocument, EmbeddedDocument,
                         EmbeddedDocumentField, IntField, ListField,
                         ReferenceField, StringField)


class ThesaurusDict(gj.Document):
    """
    TO DO .
    """
    # {"collection":"Thesaurus"}
    name = StringField(max_length=20, Required=True)
    thesaurus_type = StringField(max_length=20, Required=True)
    thesaurus_data = ListField(StringField(max_length=300))
