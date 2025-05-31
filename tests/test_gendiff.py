from gendiff import gendiff


def test_generate_diff_json():
    assert gendiff.generate_diff('file1.json', 'file2.json') == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_generate_diff_yaml():
    assert gendiff.generate_diff('file1.yaml', 'file2.yaml') == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_generate_diff_nested_yaml():
    file = open('tests/test_data/format_stalish.txt', 'r')
    assert gendiff.generate_diff('file3.yaml', 'file4.yaml') == file.read()


def test_generate_diff_nested_json():
    file = open('tests/test_data/format_stalish.txt', 'r')
    assert gendiff.generate_diff('file3.json', 'file4.json') == file.read()


def test_generate_diff_plain_json():
    file = open('tests/test_data/format_plain.txt', 'r')
    assert gendiff.generate_diff(
        'file3.json',
        'file4.json', 
        format_name='plain') == file.read()


def test_generate_diff_plain_yaml():
    file = open('tests/test_data/format_plain.txt', 'r')
    assert gendiff.generate_diff(
        'file3.yaml',
        'file4.yaml', 
        format_name='plain') == file.read()


def test_generate_diff_json_yaml():
    file = open('tests/test_data/format_json.txt', 'r')
    assert gendiff.generate_diff(
        'file3.yaml',
        'file4.yaml', 
        format_name='json') == file.read()


def test_generate_diff_format_json():
    file = open('tests/test_data/format_json.txt', 'r')
    assert gendiff.generate_diff(
        'file3.json',
        'file4.json',
        format_name='json') == file.read()
