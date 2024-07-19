
def convertPyToDict(py: dict, fieldname: dict) -> dict:
    result = {}

    for key, value in py.items():
        ogkey = key
        assign = fieldname.get(key) if key in fieldname else None
        ogkey = assign if assign is not None else ogkey

        result[ogkey] = value

    return result


def convertModelToDict(model: dict, fieldname: dict) -> dict:
    result = {}

    for key, value in model:
        ogkey = key
        assign = fieldname.get(key) if key in fieldname else None
        ogkey = assign if assign is not None else ogkey

        result[ogkey] = value

    return result


def convertModelToDictList(data: list, fieldname: dict) -> dict:
    result = []
    for model in data:
        res = {}
        for key, value in model:
            ogkey = key
            assign = fieldname.get(key) if key in fieldname else None
            ogkey = assign if assign is not None else ogkey

            res[ogkey] = value

        result.append(res)
    return result
