import uuid

def generate_id():
    return str(uuid.uuid4())

def check_object_has_keys(obj: dict, keys: list) -> bool:
    return all([key in obj for key in keys])