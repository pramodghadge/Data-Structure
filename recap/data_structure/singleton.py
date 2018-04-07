from functools import wraps

def singleton(cls):
    instances = {}
    @wraps
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


