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

tests = [test0, test1, test2, test3, test4, test5, test6, test7]

def merge_sort(nums, depth=0):

    # print('  '*depth, 'merge_sort:', nums)

    # Terminating condition (list of 0 or 1 elements)
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    # Solve the problem for each half recursively
    # Combine the results of the two halves
    return merge(merge_sort(nums[:mid], depth+1),
                 merge_sort(nums[mid:], depth+1),
                 depth+1)

def merge(nums1, nums2, depth=0):

    # print('  '*depth, 'merge:', nums1, nums2)

    i, j, merged = 0, 0, []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    return merged + nums1[i:] + nums2[j:]


def shellSort(arr, n):
    gap = n // 2
    while gap > 0:
        j = gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j < n:
            i = j - gap  # This will keep help in maintain gap value

            while i >= 0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if arr[i + gap] > arr[i]:

                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]

                i = i - gap  # To check left side also
                # If the element present is greater than current element
            j += 1
        gap = gap // 2


# driver to check the code
# arr2 = [12, 34, 54, 2, 3]
# print("input array:", arr2)
#
# shellSort(arr2, len(arr2))
# print("sorted array", arr2)


results = evaluate_test_cases(merge_sort, tests)

