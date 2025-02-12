from difference_calculator import json_util


def generate_diff(file1_path, file2_path):
    file1_path = json_util.read_json_files(file1_path)
    file2_path = json_util.read_json_files(file2_path)
    result = {}
    for key in file1_path:
        if key in file2_path and file1_path[key] == file2_path[key]:
            result[f'   {key}'] = file1_path[key]
        elif key in file2_path and file1_path[key] != file2_path[key]:
            result[f'- {key}'] = file1_path[key]
            result[f'+ {key}'] = file2_path[key]
        else:
            result[f'- {key}'] = file1_path[key]
    for key in file2_path:
        if key not in file1_path:
            result[f'+ {key}'] = file2_path[key]
    res = json_util.parse_json_files(result)[1: -1]
    res = res.replace('"', '').split(',')
    res.sort(key=lambda res: res[3])
    res.insert(0, '{')
    res.append('}')
    res = '\n'.join(res)
    return res

