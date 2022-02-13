from flask import request, jsonify
from flask_restful import Resource
from dependency_injector.wiring import inject, Provide
from TracingApiContainer import TracingApiContainer
from domain.exception.AddTraceException import AddTraceException
from domain.model.Trace import Trace
from domain.model.TraceType import TraceType
from domain.usecases.AddTraceUseCase import AddTraceUseCase


class TracingController(Resource):

    @inject
    def __init__(self, add_trace_use_case: AddTraceUseCase = Provide[TracingApiContainer.add_trace_use_case]):
        self.__add_trace_use_case = add_trace_use_case

    def post(self):
        try:
            body = request.json
            trace = Trace(TraceType[body["type"]], body["id"], body["starting"], body["finishing"])
            self.__add_trace_use_case.add_trace(trace)
            return request.json
        except AddTraceException as e:
            return str(e), 500
