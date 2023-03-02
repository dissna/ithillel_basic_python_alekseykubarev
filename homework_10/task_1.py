def copydeep(obj, memory=None):
    if memory is None:
        memory = {}

    obj_id = id(obj)
    if obj_id in memory:
        return memory[obj_id]

    if isinstance(obj, (str, int, float, bool)):
        copied_obj = obj
    elif isinstance(obj, list):
        copied_obj = []
        memory[obj_id] = copied_obj
        for item in obj:
            copied_item = copydeep(item, memory)
            copied_obj.append(copied_item)
    elif isinstance(obj, dict):
        copied_obj = {}
        memory[obj_id] = copied_obj
        for key, value in obj.items():
            copied_key = copydeep(key, memory)
            copied_value = copydeep(value, memory)
            copied_obj[copied_key] = copied_value
    else:
        raise ValueError("Unsupported data type")

    return copied_obj


test_data = [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658]}, 2.0, {'e': 0}]
test_data[3]['d'] = test_data
test_data[-1]['f'] = test_data[-1]
copy = copydeep(test_data)
print(test_data)
# [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658], 'd': [...]}, 2.0, {'e': 0, 'f': {...}}]
print(copy)
# [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658], 'd': [...]}, 2.0, {'e': 0, 'f': {...}}]
print(copy[3]['c'] is not test_data[3]['c'])  # True
print(copy[3]['d'] is not test_data[3]['d'])  # True
print(copy[3]['d'] is copy)  # True
print(copy[-1] is not test_data[-1])  # True
print(copy[-1] is copy[-1]['f'])  # True