def lchain(*iterables):
    result = []
    for iterable in iterables:
        for element in iterable:
            result.append(element)
    return result


print("[1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)", '\nResult:', lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)))