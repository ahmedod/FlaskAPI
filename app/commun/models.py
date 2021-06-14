""" Models module"""
import datetime

import mongoengine_goodjson as gj
from mongoengine import (CASCADE, BooleanField, ComplexDateTimeField,
                         DateTimeField, DecimalField, Document,
                         DynamicDocument, EmbeddedDocument,
                         EmbeddedDocumentField, IntField, ListField,
                         ReferenceField, StringField)