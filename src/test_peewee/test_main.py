# -*- coding: utf-8 -*-

"""
# @Time    : 2017/8/21 20:07
# @Author  : jeffreysun
# @Site    : 
# @File    : test_main.py
# @Software: PyCharm Community Edition
"""
from datetime import date

from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database

def init_db():
    db.connect()
    db.create_tables([Person, Pet])

def test_save():
    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
    uncle_bob.save()


def main():
    db.connect()
    test_save()

if __name__ == '__main__':
    main()