from data.datasource import DataBaseController
from data.exceptions.DataBaseConnectionException import DataBaseConnectionException
from domain.model.Trace import Trace


class TracingDataBase:

    def add_trace(self, trace: Trace):
        try:
            data_base = DataBaseController.get_database()
            collection = data_base["traces"]
            trace_dict = {"type": trace.type.name, "id": trace.id, "action": trace.action.name,
                          "time": trace.time}
            return collection.insert_one(trace_dict)
        except Exception as e:
            raise DataBaseConnectionException(e)
