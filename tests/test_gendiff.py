from pathlib import Path

from difference_calculator.gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


before_file1_json = get_test_data_path('file1.json')
before_file2_json = get_test_data_path('file2.json')
actual = generate_diff(before_file1_json, before_file2_json)


def test_generate_diff():
    assert actual == '''{
 - follow: false
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: true
}'''
