from jovian.pythondsa import evaluate_test_cases

test1={'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0],
                  'query': 1},
        'output': 6}
test2={'input': {'cards': [4, 2, 1, -1],
                  'query': 4},
        'output': 0}
test3={'input': {'cards': [3, -1, -9, -127],
                  'query': -127},
        'output': 3}
test4={'input': {'cards': [6],
                  'query': 6},
        'output': 0}
test5={'input': {'cards': [9, 7, 5, 2, -9],
                  'query': 4},
        'output': -1}
test6={'input': {'cards': [],
                  'query': 1},
        'output': -1}
test7={'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                  'query': 3},
        'output': 7}
test8={'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                  'query': 6},
        'output': 2}
test9={'input': {'cards': list(range(10000000, 0, -1)),
                  'query': 2},
        'output': 9999998}
tests = [test1, test2, test3, test4, test5, test6, test7, test8, test9]

#cards are in descending order
def locate_card_1(cards, query):
    #setting start an end
    lo, hi = 0, len(cards)-1

    #initiating loop
    while lo<=hi:
        #finding mid value
        mid = (lo + hi)//2
        mid_num = cards[mid]

        # print("lo:", lo, "hi:", hi, "mid:", mid, "mid num:", mid_num)

        # mid is the target
        if mid_num == query:
            return mid
        # query is greater than mid
        elif mid_num < query:
            hi = mid - 1
        # query is less than mid
        elif mid_num > query:
            lo = mid + 1

    return -1

# evaluate_test_cases(locate_card_1, tests)

#location tester (searches if the target is in the right or left list or the mid number itself)
def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)

    # mid number is target
    if mid_number == query:
        # if duplicate value on the left then moves the cursor to left
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    # mid number less than query
    elif mid_number < query:
        return 'left'
    # mid number less than query
    else:
        return 'right'


def locate_card_2(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

# evaluate_test_cases(locate_card_2, tests)
# evaluate_test_cases(locate_card_2, [test9])

"""
Once again, let's try to count the number of iterations in the algorithm. 
If we start out with an array of N elements, then each time the size of the 
array reduces to half for the next iteration, until we are left with just 
1 element.

Initial length - N
Iteration 1 - N/2
Iteration 2 - N/4 i.e. N/2^2
Iteration 3 - N/8 i.e. N/2^3

...

Iteration k - N/2^k
Since the final length of the array is 1, we can find the
N/2^k = 1
Rearranging the terms, we get
N = 2^k

Taking the logarithm
k = log N

Where log refers to log to the base 2. Therefore, our algorithm has the time 
complexity O(log N). This fact is often stated as: binary search runs in 
logarithmic time. You can verify that the space complexity of binary search is 
O(1).

Furthermore, as the size of the input grows larger, the difference only gets 
bigger. For a list 10 times, the size, linear search would run for 10 times 
longer, whereas binary search would only require 3 additional operations! 
(can you verify this?) That's the real difference between the complexities O(N) 
and O(log N)
"""

"""Generic Binary Search"""
def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def locate_card(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(cards) - 1, condition)

# evaluate_test_cases(locate_card, tests)


