import datetime

from pymongo import MongoClient

class Model():

    def __init__(self):
        self.client = MongoClient("mongodb://52.26.59.112:27017")
        #self.client = MongoClient()
        self.db = self.client['todoDB']
        self.todos = self.db['todos']

