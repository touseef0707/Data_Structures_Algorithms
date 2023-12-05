from jovian.pythondsa import evaluate_test_cases

test0 = {'input': {'nums': [4, 2, 6, 3, 4, 6, 2, 1]},
         'output': [1, 2, 2, 3, 4, 4, 6, 6]}

test1 = {'input': {'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]},
         'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]}

test2 = {'input': {'nums': [3, 5, 6, 8, 9, 10, 99]},
         'output': [3, 5, 6, 8, 9, 10, 99]}

test3 = {'input': {'nums': [99, 10, 9, 8, 6, 5, 3]},
         'output': [3, 5, 6, 8, 9, 10, 99]}

test4 = {'input': {'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]},
         'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]}

test5 = {'input': {'nums': []},
         'output': []}

test6 = {'input': {'nums': [23]},
         'output': [23]}

test7 = {'input': {'nums': [42, 42, 42, 42, 42, 42, 42]},
         'output': [42, 42, 42, 42, 42, 42, 42]}

import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {'input': {'nums': in_list},
         'output': out_list}

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]

"""
Here's an implementation of quicksort and partitions
"""

def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1

    # Initialize right and left pointers
    l, r = start, end - 1

    while r > l:
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1
        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1
        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end


def quicksort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot - 1)
        quicksort(nums, pivot + 1, end)

    return nums


results = evaluate_test_cases(quicksort, tests)