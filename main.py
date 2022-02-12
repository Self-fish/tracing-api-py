import sys
import logging
from flask import Flask
from flask_restful import Api
from TracingApiContainer import TracingApiContainer
from framework.controller.TracingController import TracingController

app = Flask(__name__)
api = Api(app)

api.add_resource(TracingController, '/tracing')


if __name__ == '__main__':
    tracing_container = TracingApiContainer()
    tracing_container.wire(modules=[sys.modules[__name__]])
    app.run(host='0.0.0.0', port=8083)
    log = logging.getLogger('werkzeug')
    log.disabled = True
