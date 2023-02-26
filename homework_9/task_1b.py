import random

def diff_min_max(num_limit, lower_bound, upper_bound):
    nums = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    min_num = nums[0]
    max_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return max_num - min_num


num_limit = int(input('Enter the number of random numbers: '))
lower_bound = int(input('Enter the minimum range value: '))
upper_bound = int(input('Enter the maximum range value: '))
print('Result:', diff_min_max(num_limit, lower_bound, upper_bound))