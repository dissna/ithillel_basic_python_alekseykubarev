def gen_primes():
    lst = []
    for i in range(0, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


print("List with prime numbers from 0 to 100: ", gen_primes())
