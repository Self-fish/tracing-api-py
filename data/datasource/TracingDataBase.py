from data.datasource import DataBaseController
from domain.model.Trace import Trace


class TracingDataBase:

    def add_trace(self, trace: Trace):
        data_base = DataBaseController.get_database()
        collection = data_base["traces"]
        trace_dict = {"type": trace.type.name, "id": trace.id, "starting": trace.starting, "finishing": trace.finishing}
        return collection.insert_one(trace_dict)
