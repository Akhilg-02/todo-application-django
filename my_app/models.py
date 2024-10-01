from django.db import models
import mongoengine as me
from mongoengine import Document, StringField, BooleanField
import bcrypt

class TodoItem(Document):
    title= StringField(required=True, max_length=200)
    description = StringField()
    completed = BooleanField(default=False)

    def __str__(self):
        return self.title


class User(Document):
    username = StringField(required=True, unique=True, max_length=100)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)


    def set_password(self, raw_password):
        # hashing the password
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, raw_password):
        # checking the password
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))

class Event(me.Document):
    title = me.StringField(required=True, max_length=200)
    date = me.DateField()
    description = me.StringField()

    def __str__(self):
        return self.title

