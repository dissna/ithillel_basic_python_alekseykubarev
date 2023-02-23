from random import randint

def index(lst, elem):
    for x in lst:
        if lst[x] == elem:
            return x
    else:
        return None


lst = [randint(-10, 10) for i in range(20)]
print("List: ", lst)
elem = 0
print(index(lst, elem))