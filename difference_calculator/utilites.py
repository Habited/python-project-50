import json
import os

import yaml


def get_the_file_path(file):
    return os.path.abspath(file)


def get_a_python_object(file_path) -> dict:
    f: tuple = os.path.split(file_path)
    file_name: str = f[-1]
    if 'json' in file_name:
        return read_a_json_file(file_name)
    elif 'yaml' in file_name:
        return read_a_yaml_file(file_name)


def parse_json_files(data):
    return json.dumps(data)


def parse_yaml_files(data):
    return yaml.dump(data)


def read_a_json_file(file):
    with open(file, 'r') as file_read:
        dictionary = json.load(file_read)
        return dictionary


def read_a_yaml_file(file):
    with open(file, 'r') as file_read:
        dictionary = yaml.load(file_read, Loader=yaml.Loader)
        return dictionary
