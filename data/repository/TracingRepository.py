from domain.model.Trace import Trace


class TracingRepository:

    def add_trace(self, trace: Trace):
        print(trace.type.name)
        print(trace.id)
        print(trace.starting)
        print(trace.finishing)