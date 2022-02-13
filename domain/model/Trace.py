from domain.model.TraceAction import TraceAction
from domain.model.TraceType import TraceType


class Trace:

    def __init__(self, type: TraceType, id, action: TraceAction, time):
        self.type = type
        self.id = id
        self.action = action
        self.time = time
