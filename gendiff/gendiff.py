import json

from . import plain, stalish, utilites


def generate_diff(file_1, file_2, format_name='stalish') -> str:
    dict1 = utilites.get_a_python_object(file_1)
    dict2 = utilites.get_a_python_object(file_2)
    difference_dict = utilites.get_diff(dict1, dict2)
    if format_name == 'stalish':
        update = stalish.stalish(difference_dict)
        return '{\n' + update + '\n}'
    elif format_name == 'plain':
        update = plain.plain(difference_dict)
        return update
    elif format_name == 'json':
        return json.dumps(difference_dict, indent=4)