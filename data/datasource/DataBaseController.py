import configparser
import certifi
from pymongo import MongoClient

DATA_BASE_NAME = "self-fish-db"


def connect_to_database():
    config = configparser.ConfigParser()
    config.read("db_connection.ini")
    return "mongodb+srv://" + config['CREDENTIALS']['user'] + ":" + config['CREDENTIALS']['password'] + \
           "@cluster0.ryrnh.mongodb.net/" + config['DATABASE']['name'] + "?retryWrites=true&w=majority"


def get_database():
    client = MongoClient(connect_to_database(), tlsCAFile=certifi.where())
    return client[DATA_BASE_NAME]
