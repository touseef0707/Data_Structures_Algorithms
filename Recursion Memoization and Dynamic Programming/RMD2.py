""""""
""" 
KNAPSACK PROBLEM

Problem Statement:
--> You're in charge of selecting a football team from a large pool of players.
Each player has a cost, and a rating. You have a limited budget. What is the highest
total rating of a team that fits within your budget. Assume that there is no minimum
or maximum team size.

General Problem statement:
--> Given n elements, each of which has a weight and a profit, determine the maximum
profit that can be obtained by selecting a subset of the elements weighing no more than
w. 

        Profit  [2, 3, 1, 5, 4, 7]
        Weight  [4, 5, 1, 3, 2, 5]
        capacity  15

"""
from jovian.pythondsa import evaluate_test_cases

test0 = {
    'input':{
        'weights':[23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits':[92, 57, 49, 68, 60, 43, 67, 84, 87, 72,],
        'capacity': 165
    },
    'output' : 309
}
test1 = {
    'input':{
        'weights':[4, 5, 6],
        'profits':[1, 2, 3],
        'capacity': 3
    },
    'output' : 0
}
test2 = {
    'input':{
        'weights':[4, 5, 1],
        'profits':[1, 2, 3],
        'capacity': 4
    },
    'output' : 3
}
test3 = {
    'input':{
        'weights':[41, 50, 49, 59, 55, 57, 60],
        'profits':[442, 525, 511, 593, 546, 564, 617],
        'capacity': 170
    },
    'output' : 1735
}
test4 = {
    'input':{
        'weights':[4, 5, 6],
        'profits':[1, 2, 3],
        'capacity':15
    },
    'output' :6
}
test5 = {
    'input':{
        'weights':[4, 5, 1, 3, 2, 5],
        'profits':[2, 3, 1, 5, 4, 7],
        'capacity':15
    },
    'output' :19
}
tests = [test0, test1, test2, test3, test4, test5]

def max_profit_recursive(weights, profits, capacity, idx=0):

    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx+1)
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx] + max_profit_recursive(weights, profits,
                                                      capacity-weights[idx],
                                                      idx+1)
        return max(option1, option2)

# result = evaluate_test_cases(max_profit_recursive, tests)
memo={}
def max_profit_memoized(weights, profits, capacity, idx=0, memo ={}):
    def recurse(c, i):
        key = (c, i)
        if key in memo:
            pass
        elif i == len(weights) or c == 0:
            memo[key] = 0
        elif weights[i] > c:
            memo[key] = recurse(c, i+1)
        else:
            memo[key] = max(recurse(c, i+1), profits[i] + recurse(c-weights[i], i+1))
        return memo[key]
    return recurse(capacity, idx)

# result = evaluate_test_cases(max_profit_memoized, tests)

def max_profit_dynamic(weights, profits, capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n+1)]
    for i in range(n):
        for c in range(1, capacity+1):
            if weights[i]>c:
                table[i+1][c] = table[i][c]
            else:
                option1 = table[i][c]
                option2 = profits[i] + table[i][c-weights[i]]
                table[i+1][c] = max(option1, option2)
    return table[-1][-1]

# result = evaluate_test_cases(max_profit_dynamic, tests)
