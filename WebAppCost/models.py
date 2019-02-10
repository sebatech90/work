from peewee import *
from app import base


class BaseModel(Model):
    class Meta:
        database = base


class Users(BaseModel):
    name = CharField(null=False)
    surname = CharField(null=False)

    def __str__(self):
        return self.name


class Expenses(BaseModel):
    user = ForeignKeyField(Users, related_name='user')
    name = CharField(null=False)
    date = DateTimeField(null=False)
    cost = DoubleField(null=False)

    def __str__(self):
        return self.name