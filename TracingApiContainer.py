from dependency_injector import containers, providers

from data.datasource.TracingDataBase import TracingDataBase
from data.repository.TracingRepository import TracingRepository
from domain.usecases.AddTraceUseCase import AddTraceUseCase


class TracingApiContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    data_base = providers.Factory(TracingDataBase)
    repository = providers.Factory(TracingRepository, data_base)
    add_trace_use_case = providers.Factory(AddTraceUseCase, repository)
