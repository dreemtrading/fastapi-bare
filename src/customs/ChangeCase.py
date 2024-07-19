import re
import inspect
from sqlalchemy.ext.declarative import DeclarativeMeta


def modelToDictionary(obj):
    if isinstance(obj, dict):
        return {k: modelToDictionary(v) for k, v in obj.items()}
    elif isinstance(obj.__class__, DeclarativeMeta):
        return {c.key: modelToDictionary(getattr(obj, c.key)) for c in inspect(obj).mapper.column_attrs}
    elif isinstance(obj, list):
        return [modelToDictionary(i) for i in obj]
    else:
        return obj


def camelToSnake(data):
    def internalFunc(name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    if isinstance(data, dict):
        return {internalFunc(k): camelToSnake(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [camelToSnake(i) for i in data]
    else:
        return data


def snakeToCamel(data):
    def internalFunc(name):
        components = name.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

    if isinstance(data, dict):
        return {internalFunc(k): snakeToCamel(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [snakeToCamel(i) for i in data]
    else:
        return data
