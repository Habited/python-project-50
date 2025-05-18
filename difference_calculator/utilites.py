import json
from pathlib import Path
from typing import Any, Dict, Union

import yaml


def get_a_python_object(file_path: Union[str, Any]):
    path = Path(file_path)
    content = path.read_text(encoding="utf-8")
    suffix = path.suffix.lower()

    if suffix == ".json":
        return json.loads(content)
    if suffix in (".yml", ".yaml"):
        return yaml.safe_load(content)


def get_diff(old_dict: Dict, new_dict: Dict, ) -> Dict:
    diff = {}
    all_keys = sorted(set(old_dict) | set(new_dict))

    for key in all_keys:
        old_val = old_dict.get(key)
        new_val = new_dict.get(key)

        if isinstance(old_val, dict) and isinstance(new_val, dict):
            diff[key] = {
                "type": "nested", 
                "children": get_diff(old_val, new_val)
            }

        elif key not in new_dict:
            diff[key] = {
                "type": "removed",
                "value": old_val
            }
        elif key not in old_dict:
            diff[key] = {
                "type": "added",
                "value": new_val
            }
        elif old_val == new_val:
            diff[key] = {
                "type": "unchanged",
                "value": old_val
                }
        else:
            diff[key] = {
                "type": "changed",
                "old_value": old_val,
                "new_value": new_val
            }
    return diff
