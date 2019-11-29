import json
import uuid


def get_test_context():
    class Context(object):
        pass
    c = Context()
    c.aws_request_id = uuid.uuid4().__str__()
    return c


def pretty_json(obj_to_pretty: dict) -> str:
    return json.dumps(obj_to_pretty, default=str, sort_keys=True)
