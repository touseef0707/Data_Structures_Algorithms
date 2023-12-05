def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        # print("lo:", lo, "mid:",mid ,"hi:", hi, "result:" ,result)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return 0
from jovian.pythondsa import evaluate_test_cases


test1 = {'input': {'cards': [5, 6, 9, 0, 2, 3, 4]},
        'output': 3}
test2 = {'input': {'cards': [6, 9, 0, 2, 3, 4, 5]},
        'output': 2}
test3 = {'input': {'cards': [9, 0, 2, 3, 4, 5, 6]},
        'output': 1}
test4 = {'input': {'cards': [0, 2, 3, 4, 5, 6, 9]},
        'output': 0}
test5 = {'input': {'cards': [5, 6, 9, 10, 12, 3, 4]},
        'output': 5}
test6 = {'input': {'cards': [5, 6, 9, 10, 12, 13, 4]},
        'output': 6}
test7 = {'input': {'cards': []},
        'output': 0}
test8 = {'input': {'cards': [5]},
        'output': 0}
test9 = {'input': {'cards': [5, 6]},
        'output': 0}
test10 = {'input': {'cards': [6, 5]},
        'output': 1}
test11 = {'input': {'cards': list(range(100001,100543))+list(range(1,100000))},
        'output': 542}
test12 ={'input': {'cards': [6, 6, 6, 6, 6]},
        'output': 0}
test13 = {'input': {'cards': [6, 6, 6, 5, 5, 6]},
        'output': 3}
test14 = {'input': {'cards': [6, 6, 6, 6, 5, 6]},
        'output': 4}
test15 = {'input': {'cards': [5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7]},
        'output': 0}
test16 = {'input': {'cards': [6, 6, 6, 6, 5]},
        'output': 4}
test17 = {'input': {'cards': [6, 5]},
        'output': 1}

tests=[test1, test2, test3, test4, test5, test6, test7, test8, test9, test10,
       test11, test12, test13, test14, test15, test16, test17]

"""
STEPS
1. Take the mid value
2. Compare with first value
3. If mid value less than first value -> then rotated -> go for next mid in left
4. Elif mid value greater than last value -> go for next mid in right
5. keep going for mids untill mid value greater than the next or mid equals to len(cards)-1
"""

def countRotations(cards):
    lo, hi = 0, len(cards) - 1

    def condition(mid):
        if mid > 0 and cards[mid]<cards[mid - 1]:
            return 'found'
        elif mid >0 and cards[mid]<cards[0]:
            return 'left'
        else:
            return 'right'

    return binary_search(lo, hi, condition)
# evaluate_test_cases(countRotations, tests)


"""Extended finding target index in a sorted array"""
from BinarySearch import locate_card
def targetIndex(cards, query):

    length = len(cards)
    smallest_num = countRotations(cards)
    list_1 = list(cards[i] for i in range(0, smallest_num))
    list_2 = list(cards[i] for i in range(smallest_num, length))

    A = locate_card(list_1, query)
    B = locate_card(list_2, query)

    if A != -1:
        return A
    elif A==B==-1:
        return -1
    else:
        return B+smallest_num

# print(targetIndex([6, 6, 6, 5, 5, 6],5))

"""Leet code solution"""


def search(self, nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        # when we are in the left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        else:
            # right sorted array
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1