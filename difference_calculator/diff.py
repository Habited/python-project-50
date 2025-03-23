def get_diff(dict1, dict2, result_dict={}) -> dict:
    for key, value in dict1.items():
        if isinstance(value, dict):
            result_dict[key] = ['', 'nested']
            get_diff(value, dict2)
        else:
            if key in dict2:
                if value == dict2[key]:
                    result_dict[key] = [value, '']
                else:
                    result_dict[key] = [value, dict2[key], 'changet']
            elif key not in dict2:
                result_dict[key] = [value, 'deleted']
    for key, value in dict2.items():
        if isinstance(value, dict):
            result_dict[key] = ['', 'nested']
            get_diff(value, dict1)
        else:
            if key not in dict1:
                result_dict[key] = [value, 'added']

    return result_dict
            
