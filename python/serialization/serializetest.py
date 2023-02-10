#!/usr/bin/env python3
import json
class NodeRef:
    def __init__(self, mydata):
        self.mydata = mydata

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

a_dict = {
    "some_data": "first level",
    "some_object": NodeRef("mydata obv")
}

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if type(o) == NodeRef:
            return dict({"mydata": o.mydata})
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.encode(self, o)

#print(json.dumps(a_dict, cls=MyEncoder))
print(MyEncoder().encode(a_dict))