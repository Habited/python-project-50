def get_diff(dict1, dict2, result_dict={}, depth=0) -> dict:
    for key, value in dict1.items():
        if isinstance(value, dict) and key in dict2:
            result_dict[key] = ['nested', depth]
            depth += 1
            get_diff(value, dict2)
        else:
            if key in dict2:
                if dict2[key] == value:
                    result_dict[key] = [value, None]
                else:
                    result_dict[key] = [value, dict2[key], 'changet']
            else:
                result_dict[key] = [value, 'deleted']
            
    for key, value in dict2.items():
        if isinstance(value, dict):
            result_dict[key] = ['nested', depth]
            depth += 1
            get_diff(value, dict1)
        elif key not in dict1:
            result_dict[key] = [value, 'added']

    return result_dict
