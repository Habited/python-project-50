from typing import Any, Dict


def plain(difference_dict: Dict[str, Any],
          indent: str = 'Property ',
          path=[]) -> str:
    lines = []
    for key, node in difference_dict.items():
        node_type = node['type']
        value = node.get('value')
        children: Dict = node.get('children')

        if node_type == 'nested':
            path.append(key)
            lines.append(f'{plain(children)}')
            path.pop()
        elif node_type == 'added':
            path.append(key)
            lines.append(f"{indent}'{'.'.join(path)}' was added with value: "
                         f"{stringify(value)}")
            path.pop()
        if node_type == 'removed':
            path.append(key)
            lines.append(f"{indent}'{'.'.join(path)}' was removed")
            path.pop()
        elif node_type == 'changed':
            path.append(key)
            lines.append(f"{indent}'{'.'.join(path)}' was updated."
                         f" From {stringify(node['old_value'])}"
                         f" to {stringify(node['new_value'])}")
            path.pop()
    return '\n'.join(lines)


def stringify(value: Any) -> Any:
    if isinstance(value, int):
        return f'{value}'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if not isinstance(value, dict):
        return f"'{value}'"
    if isinstance(value, dict):
        return "[complex value]"

