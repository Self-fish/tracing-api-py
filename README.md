# Tracing API
The purpose of this API is to provide a way to trace all the actions that the aquarium is doing by receving a Trace object as follows:

```python
class Trace:
    def __init__(self, type: TraceType, id, action: TraceAction, time):
        self.type = type
        self.id = id
        self.action = action
        self.time = time
```

## TraceType
Until now, the type of traces supported are the following:
* **COVER_MOTOR**: each time the motors in charge of moving the cover START or STOP
* **FILL_BOMB**: each time that the bomb in charge of filling the aquarium START or STOP
* **LIGHTS**: each time that the lights START or STOP

## Data Base
In order to store the different traces, I'm using mongodb in which the information is stored as follows:

```json
{
  "_id":{
    "$oid":"6208d674c86bfea773e126d3"
  },
  "type":"COVER_MOTOR",
  "id":"right_back",
  "action":"START",
  "time":{
    "$numberInt":"1234567"
  }
}
```

## Data base connection
In order to connect with your mongodb, you need to define a *db_connection.ini* file with the following format

```text
[CREDENTIALS]
user = user
password = password

[DATABASE]
name = database-name
```
