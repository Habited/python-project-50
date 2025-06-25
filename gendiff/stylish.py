from typing import Any, Dict


def stylish(difference_dict: Dict[str, Dict], indent: str = '') -> str:
    lines = []
    for key, node in difference_dict.items():
        node_type = node['type']
        value = node.get('value')
        children = node.get('children')

        if node_type == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.append(stylish(children, indent + '    '))
            lines.append(f"{indent}    }}")
        elif node_type == 'added':
            lines.append(f"{indent}  + {key}: "
                         f"{stringify(value, indent + '    ')}")
        elif node_type == 'removed':
            lines.append(f"{indent}  - {key}: "
                         f"{stringify(value, indent + '    ')}")
        elif node_type == 'changed':
            lines.append(f"{indent}  - {key}: "
                         f"{stringify(node['old_value'], indent + '    ')}")
            lines.append(f"{indent}  + {key}: "
                         f"{stringify(node['new_value'], indent + '    ')}")
        else:
            lines.append(f"{indent}    {key}: "
                         f"{stringify(value, indent + '    ')}")

    return '\n'.join(lines)


def stringify(value: Any, indent: str = '') -> str:
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if not isinstance(value, dict):
        return str(value)
    lines = []
    for key, val in value.items():
        lines.append(f"{indent}    {key}: {stringify(val, indent + '    ')}")

    return '{\n' + '\n'.join(lines) + '\n' + indent + '}'
