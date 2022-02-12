from dependency_injector import containers, providers

from domain.usecases.AddTraceUseCase import AddTraceUseCase


class TracingApiContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    add_trace_use_case = providers.Factory(AddTraceUseCase)
