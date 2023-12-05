""""""
"""
#### Problem
> We need to write a function to sort a list of numbers in increasing order.

#### Input
1. `nums`: A list of numbers e.g. `[4, 2, 6, 3, 4, 6, 2, 1]` 

#### Output
2. `sorted_nums`: The sorted version of `nums` e.g. `[1, 2, 2, 3, 4, 4, 6, 6]`


The signature of our function would be as follows:

## 2. Come up with some example inputs & outputs. 

Here are some scenarios we may want to test out:

1. Some lists of numbers in random order.
2. A list that's already sorted.
3. A list that's sorted in descending order.
4. A list containing repeating elements.
5. An empty list. 
6. A list containing just one element.
7. A list containing one element repeated many times.
8. A really long list.

Let's create some test cases for these scenarios. We'll represent each test 
case as a dictionary for easier automated testing.
"""


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
"""
To create the final test case (a really long list), we can start with a sorted 
list created using `range` and shuffle it to create the input.
"""
import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {'input': {'nums': in_list},
         'output': out_list}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]

def bubble_sort(nums):
    length = len(nums)
    x=0
    while x<length-1:
        for i in range(length-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        x+=1
    return nums

# results = evaluate_test_cases(bubble_sort, tests)

def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums

# results = evaluate_test_cases(insertion_sort, tests)

def selection_sort(nums):
    n = len(nums)

    for i in range(n - 1):
        # Find the minimum element in the unsorted portion
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap the minimum element with the first element in the unsorted portion
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums

results = evaluate_test_cases(selection_sort, tests)