import configparser
import certifi
from pymongo import MongoClient

from domain.model.Trace import Trace


class TracingDataBase:

    def __connect_to_database(self):
        config = configparser.ConfigParser()
        config.read("db_connection.ini")
        db_user = config['CREDENTIALS']['user']
        db_password = config['CREDENTIALS']['password']
        db_name = config['DATABASE']['name']
        return "mongodb+srv://" + db_user + ":" + db_password + "@cluster0.ryrnh.mongodb.net/" + \
               db_name + "?retryWrites=true&w=majority"

    def __get_database(self):
        client = MongoClient(self.__connect_to_database(), tlsCAFile=certifi.where())
        return client["self-fish-db"]

    def add_trace(self, trace: Trace):
        data_base = self.__get_database()
        collection = data_base["traces"]
        trace_dict = {"type": trace.type.name, "id": trace.id, "starting": trace.starting, "finishing": trace.finishing}
        return collection.insert_one(trace_dict)
