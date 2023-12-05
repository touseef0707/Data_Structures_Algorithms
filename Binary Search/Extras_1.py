""""""
"""Given an array of integers nums sorted in ascending order, find the 
starting and ending position of a given number."""

from jovian.pythondsa import evaluate_test_cases

test1={'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                  'query': 6},
        'output': (2,7)}
test2={'input': {'cards': [8, 8],
                  'query': 8},
        'output': (0,1)}
test3={'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                  'query': 5},
        'output': (-1,-1)}
test4={'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                  'query': 3},
        'output': (8,8)}
test5={'input': {'cards': [],
                  'query': 3},
        'output': (-1,-1)}
test6={'input': {'cards': [8],
                  'query': 8},
        'output': (0,0)}
test7={'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                  'query': 3},
        'output': (8,8)}
test8={'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0],
                  'query': 3},
        'output': (5,5)}
tests = [test1, test2, test3, test4, test5, test6, test7, test8]

def binary_search(lo, hi, condition):
    while lo<=hi:
        mid = (lo + hi)//2
        result = condition(mid)
        print(lo, mid, hi, result)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        else:
            lo = mid+1
    return -1

def locations(cards, query):
    def S_condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    def L_condition(mid):
        if cards[mid] == query:
            if mid < len(cards)-1 and cards[mid+1]==query:
                return 'right'
            else:
                return 'found'
        elif cards[mid]<query:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(cards) - 1, S_condition), binary_search(0, len(cards) - 1, L_condition)

evaluate_test_cases(locations, tests)


