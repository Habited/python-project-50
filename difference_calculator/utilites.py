import json

import yaml


def get_the_file_path(file):
    if 'json' in file:
        with open(file, 'r') as read_file:
            f = json.load(read_file)
            return f
    elif 'yaml' in file:
        with open(file, 'r') as read_file:
            f = yaml.load(read_file, Loader=yaml.Loader)
            return f


def parse_json_files(data):
    return json.dumps(data)


def parse_yaml_files(data):
    return yaml.dump(data)
