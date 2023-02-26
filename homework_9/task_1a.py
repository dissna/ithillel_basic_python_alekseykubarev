import random

def diff_min_max(num_limit, lower_bound, upper_bound):
    nums = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    return max(nums) - min(nums)


num_limit = int(input('Enter the number of random numbers: '))
lower_bound = int(input('Enter the minimum range value: '))
upper_bound = int(input('Enter the maximum range value: '))
print('Result:', diff_min_max(num_limit, lower_bound, upper_bound))