from domain.model.Trace import Trace


class AddTraceUseCase:

    def add_trace(self, trace: Trace):
        print("Adding the trace")