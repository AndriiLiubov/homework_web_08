from mongoengine import *


class Contact(Document):
    fullname = StringField(max_length=150)
    email = StringField(max_length=150)
    received = BooleanField(default=False)
    

