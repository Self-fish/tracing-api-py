from flask import request
from flask_restful import Resource

class TracingController(Resource):

    def post(self):
        body = request.json
