def my_copy(lst1):
    lst2 = []
    for i in range(len(lst1)):
        a = lst1[i]
        lst2.append(a)
    return lst2


lst1 = ['a', 1, 2.0, ['b']]
print("new list: ", my_copy(lst1))