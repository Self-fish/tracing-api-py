from dependency_injector import containers, providers

from data.repository.TracingRepository import TracingRepository
from domain.usecases.AddTraceUseCase import AddTraceUseCase


class TracingApiContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    repository = providers.Factory(TracingRepository)
    add_trace_use_case = providers.Factory(AddTraceUseCase, repository)
