import json


def read_json_files(file):
    with open(file) as read_file:
        return json.load(read_file)


def parse_json_files(data):
    return json.dumps(data)
