'''
https://practice.geeksforgeeks.org/problems/minimum-sum-partition/0
'''

from sys import stdin
from itertools import product


def find_subarrays_min_diff(arr):
    total = sum(arr)
    dp = [[0 for _ in range(total+1)] for _ in range(len(arr))]

    for i in range(len(dp)):
        dp[i][0] = 1
        dp[i][arr[i]] = 1

        for s in range(1, len(dp[0])):
            if i != 0 and dp[i-1][s]:
                dp[i][s] = 1
                dp[i][s+arr[i]] = 1


    min_diff = total
    for i in range(len(dp)):
        for s in range(len(dp[0])):
            if dp[i][s]:
                min_diff = abs(min(min_diff, abs((total - s) - s)))


    return min_diff


tests = int(stdin.readline())

for _ in range(tests):
    n = int(stdin.readline())

    arr = list(map(int, stdin.readline().split()))

    print(find_subarrays_min_diff(arr))
