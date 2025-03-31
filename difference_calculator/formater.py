def stalish(dictionary) -> str:
    result = ''
    for key, value in dictionary.items():
        if 'added' in value:
            result += f'+ {key}: {value[0]}\n'
        elif 'nested' in value:
            result += f'{key}:\n'
        elif 'deleted' in value:
            result += f'- {key}: {value[0]}\n'
        elif 'changet' in value:
            result += f'''- {key}: {value[0]}\n+ {key}: {value[1],
                                                          {value[-1]}}\n'''
        else:
            result += f'  {key}: {value[0]}\n'
    return result
