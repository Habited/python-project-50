import json

import yaml


def read_json_files(file):
    with open(file) as read_file:
        return json.load(read_file)


def parse_json_files(data):
    return json.dumps(data)


def read_yaml_files(file):
    with open(file) as read_file:
        return yaml.load(read_file, Loader=yaml.Loader)


def parse_yaml_files(data):
    return yaml.dump(data)
