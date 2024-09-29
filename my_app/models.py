from django.db import models
import mongoengine as me
from mongoengine import Document, StringField, BooleanField


class TodoItem(Document):
    title= StringField(required=True, max_length=200)
    description = StringField()
    completed = BooleanField(default=False)

    def __str__(self):
        return self.title


# class Event(me.Document):
#     title = me.StringField(required=True, max_length=200)
#     date = me.DateField()
#     description = me.StringField()

#     def __str__(self):
#         return self.title

