from pathlib import Path

from difference_calculator.gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


before_file1_json = get_test_data_path('file1.json')
before_file2_json = get_test_data_path('file2.json')
actual_json = generate_diff(before_file1_json, before_file2_json)

before_file1_yaml = get_test_data_path('file1.yaml')
before_file2_yaml = get_test_data_path('file2.yaml')
actual_yaml = generate_diff(before_file1_yaml, before_file2_yaml)


def test_generate_diff_json():
    assert actual_json == '''{
 - follow: false
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: true
}'''


def test_generate_diff_yaml():
    assert actual_yaml == '''{
 - follow: false
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: true
}'''