import json


def read_json_files(file):
    with open(file) as read_file:
        data = json.load(read_file)
    return data


def parse_json_files(file, data):
    with open(file, "w") as write_file:
        return json.dump(data, write_file)

