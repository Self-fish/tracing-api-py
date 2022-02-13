from data.datasource.TracingDataBase import TracingDataBase
from domain.model.Trace import Trace


class TracingRepository:

    def __init__(self, data_base: TracingDataBase):
        self.__data_base = data_base

    def add_trace(self, trace: Trace):
        return self.__data_base.add_trace(trace)
