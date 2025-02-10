from difference_calculator import gendiff
from pathlib import Path


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


before_file1_json = read_file('file1.json')
before_file2_json = read_file('file2.json')
actual = gendiff.generate_diff(before_file1_json, before_file2_json)


def test_generate_diff():
    assert actual == '''{
- follow: false
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: true
}'''
