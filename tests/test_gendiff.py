from gendiff import gendiff


def test_generate_diff_nested_yaml():
    file = open('tests/test_data/format_stylish.txt', 'r')
    assert gendiff.generate_diff(
        'tests/test_data/file1.yaml',
        'tests/test_data/file2.yaml', ) == file.read()


def test_generate_diff_nested_json():
    file = open('tests/test_data/format_stylish.txt', 'r')
    assert gendiff.generate_diff(
        'tests/test_data/file1.json',
        'tests/test_data/file2.json') == file.read()


def test_generate_diff_plain_json():
    file = open('tests/test_data/format_plain.txt', 'r')
    assert gendiff.generate_diff(
        'tests/test_data/file1.json',
        'tests/test_data/file2.json', 
        format_name='plain') == file.read()


def test_generate_diff_plain_yaml():
    file = open('tests/test_data/format_plain.txt', 'r')
    assert gendiff.generate_diff(
        'tests/test_data/file1.yaml',
        'tests/test_data/file2.yaml', 
        format_name='plain') == file.read()


def test_generate_diff_json_yaml():
    file = open('tests/test_data/format_json.txt', 'r')
    assert gendiff.generate_diff(
        'tests/test_data/file1.yaml',
        'tests/test_data/file2.yaml', 
        format_name='json') == file.read()


def test_generate_diff_format_json():
    file = open('tests/test_data/format_json.txt', 'r')
    assert gendiff.generate_diff(
        'tests/test_data/file1.json',
        'tests/test_data/file2.json',
        format_name='json') == file.read()

