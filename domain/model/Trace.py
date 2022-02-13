from domain.model.TraceType import TraceType


class Trace:

    def __init__(self, type: TraceType, id, starting, finishing):
        self.type = type
        self.id = id
        self.starting = starting
        self.finishing = finishing
