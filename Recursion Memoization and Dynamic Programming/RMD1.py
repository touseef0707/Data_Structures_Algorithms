""""""
"""
RECURSION MEMOIZATION AND DYNAMIC PROGRAMMING

Problem Statement:
--> Write a function to find the length of the **longest common subsequence** 
between two sequences. Eg. Given the strings "serendipitous" and "precipitation", 
the longest common subsequence is "reipito" and its length is 7.

A subsequence is a sequence obtained by deleting zero or more elements from another
sequence. For example, "edpt" is a subsequence of "serendipitous".
"""

from jovian.pythondsa import evaluate_test_cases

test0 = {
    'input':{'seq1': 'serendipitous', 'seq2': 'precipitation'},
    'output' : 7
}
test1 = {
    'input':{'seq1': 'seren', 'seq2': 'dipitou'},
    'output' : 0
}
test2 = {
    'input':{'seq1': 'serendipitous', 'seq2': ''},
    'output' : 0
}
test3 = {
    'input':{'seq1': 'longest', 'seq2': 'stone'},
    'output' : 3
}
test4 = {
    'input':{'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3], 'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]},
    'output' : 5
}
test5 = {
    'input':{'seq1': 'dense', 'seq2': 'condensed'},
    'output' : 5
}
test6 = {
    'input':{'seq1': '', 'seq2': ''},
    'output' : 0
}
test7 = {
    'input':{'seq1': 'abcdef', 'seq2': 'badcfe'},
    'output' :3
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]


def lcs(seq1, seq2):
    pass
def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):     # base case
        return 0
    elif seq1[idx1] == seq2[idx2]:                 # match condition
        return 1 + lcs_recursive(seq1, seq2, idx1+1, idx2+1)
    else:
        option1 = lcs_recursive(seq1, seq2, idx1+1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2+1)
        return max(option1, option2)

# results = evaluate_test_cases(lcs_recursive, tests)

def lcs_memo(seq1, seq2, memo = {}):
    def recurse(idx1, idx2):
        # Create a tuple (idx1, idx2) as the key for the memo dictionary
        key = (idx1, idx2)

        # Check if the result for this subproblem is already computed and stored in the local memo dictionary
        if key in memo:
            return memo[key]

        if idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1 + 1, idx2 + 1)
        else:
            memo[key] = max(recurse(idx1 + 1, idx2), recurse(idx1, idx2 + 1))

        # Return the result stored in the local memo dictionary
        return memo[key]
    # Start the recursive calculation
    return recurse(0, 0)

# results = evaluate_test_cases(lcs_memo, tests)

def lcs_dynamic(seq1, seq2):
    # Create a table to store the lengths of LCS for subproblems
    m = len(seq1)
    n = len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill in the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of the LCS is stored in dp[m][n]
    return dp[m][n]

# results = evaluate_test_cases(lcs_dynamic, tests)

def lcs_dynamic2(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[0 for x in range(n+1)] for j in range(m+1)]

    for i in range(m):
        for j in range(n):
            if seq1[i]==seq2[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[-1][-1]

results = evaluate_test_cases(lcs_dynamic2, tests)
