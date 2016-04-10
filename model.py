from peewee import *


class Administrators(Model):
    email = CharField(unique=True, null=False)
    password = CharField(max_length=32, null=False)
    status = IntegerField(default=0)


class Advertisements(Model):
    description = CharField(max_length=200)
    code = TextField()
    status = IntegerField(default=0)


class CategoriesChannels(Model):
    name = CharField(max_length=120)
    details = TextField()
