from difference_calculator import utilites


def generate_diff(file1, file2):
    if "json" in str(file1) and "json" in str(file2):
        file1 = utilites.read_json_files(file1)
        file2 = utilites.read_json_files(file2)
    elif "yaml" in str(file1) and "yaml" in str(file2):
        file1 = utilites.read_yaml_files(file1)
        file2 = utilites.read_yaml_files(file2)
    elif "yml" in str(file1) and "yml" in str(file2):
        file1 = utilites.read_yaml_files(file1)
        file2 = utilites.read_yaml_files(file2)
    else:
        return
    result = {}
    for key in file1:
        if key in file2 and file1[key] == file2[key]:
            result[f'   {key}'] = file1[key]
        elif key in file2 and file1[key] != file2[key]:
            result[f'- {key}'] = file1[key]
            result[f'+ {key}'] = file2[key]
        else:
            result[f'- {key}'] = file1[key]
    for key in file2:
        if key not in file1:
            result[f'+ {key}'] = file2[key]
    res = utilites.parse_json_files(result)[1: -1]
    res = res.replace('"', '').split(',')
    res.sort(key=lambda res: res[3])
    res.insert(0, '{')
    res.append('}')
    res = '\n'.join(res)
    return res
