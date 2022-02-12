from domain.model.TraceType import TraceType


class Trace:

    def __init__(self, type: TraceType, id, starting, finishing):
        self.__type = type
        self.__id = id
        self.__starting = starting
        self.__finishing = finishing
