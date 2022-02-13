from data.repository.TracingRepository import TracingRepository
from domain.model.Trace import Trace


class AddTraceUseCase:

    def __init__(self, repository: TracingRepository):
        self.__repository = repository

    def add_trace(self, trace: Trace):
        return self.__repository.add_trace(trace)
