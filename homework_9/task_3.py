def copydeep(obj):
    if isinstance(obj, (int, float, str, bool)):
        return obj
    elif isinstance(obj, list):
        return [copydeep(x) for x in obj]
    elif isinstance(obj, tuple):
        return tuple(copydeep(x) for x in obj)
    elif isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            new_dict[copydeep(key)] = copydeep(value)
        return new_dict


obj = ['a', 1, 2.0, ['b']]
lst2 = copydeep(obj)
obj[3].append(0)
print(obj[3], lst2[3])