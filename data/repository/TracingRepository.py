from data.datasource.TracingDataBase import TracingDataBase
from data.exceptions.DataBaseConnectionException import DataBaseConnectionException
from domain.exception.AddTraceException import AddTraceException
from domain.model.Trace import Trace


class TracingRepository:

    def __init__(self, data_base: TracingDataBase):
        self.__data_base = data_base

    def add_trace(self, trace: Trace):
        try:
            return self.__data_base.add_trace(trace)
        except DataBaseConnectionException as e:
            raise AddTraceException(e)
