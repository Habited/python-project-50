def get_diff(struct) -> str:
    for key, value in struct.items():
        if isinstance(value, dict):
            get_diff(value)
        else:
            return key
