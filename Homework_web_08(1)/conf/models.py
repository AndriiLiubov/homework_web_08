from mongoengine import Document
from mongoengine.fields import (
    ReferenceField,
    ListField, 
    StringField, 
    )


class Author(Document):
    fullname = StringField(unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    meta = {"collection": "authors"}
    


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(unique=True)
    meta = {"collection": "quotes"}