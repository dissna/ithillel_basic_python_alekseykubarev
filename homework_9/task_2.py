import random

def diff_odd_even(num_limit, lower_bound, upper_bound):
    sum_even = 0
    sum_odd = 0
    for i in range(num_limit):
        num = random.randint(lower_bound, upper_bound)
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    return sum_even - sum_odd


num_limit = int(input('Enter the number of random numbers: '))
lower_bound = int(input('Enter the minimum range value: '))
upper_bound = int(input('Enter the maximum range value: '))
print('Result:', diff_odd_even(num_limit, lower_bound, upper_bound))