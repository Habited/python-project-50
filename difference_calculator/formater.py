from typing import Dict

from difference_calculator import utilites


def stalish(difference_dict: Dict[str, Dict], indent: str = '') -> str:
    '''Форматирует словарь с различиями в формат stalish.

    Args:
        difference_dict: Словарь с различиями
        indent: Текущий отступ

    Returns:
        Строковое представление difference_dict в формате stalish 
    '''

    lines = []
    for key, node in difference_dict.items():
        node_type = node['type']
        value = node.get('value')
        children = node.get('children')

        if node_type == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.append(stalish(children, indent + '    '))
            lines.append(f"{indent}    }}")
        elif node_type == 'added':
            lines.append(f"{indent}  + {key}: {utilites.stringify(value, indent + '    ')}")
        elif node_type == 'removed':
            lines.append(f"{indent}  - {key}: {utilites.stringify(value, indent + '    ')}")
        elif node_type == 'changed':
            lines.append(f"{indent}  - {key}: {utilites.stringify(node['old_value'], indent + '    ')}")
            lines.append(f"{indent}  + {key}: {utilites.stringify(node['new_value'], indent)}")
        else:
            lines.append(f"{indent}    {key}: {utilites.stringify(value, indent + '    ')}")

    return '\n'.join(lines)
