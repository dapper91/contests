'''
https://practice.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size/0
'''

from sys import stdin


MIN_VAL = 0
MAX_VAL = 5000

def max_min_window_size(arr):
    n = len(arr)
    dp = [[MAX_VAL for _ in range(n)] for _ in range(n)]
    maxes = [MIN_VAL] * n

    for i in range(n):
        dp[i][i] = arr[i]
        maxes[0] = max(maxes[0], arr[i])

    for offset in range(1, n):
        for i in range(n):
            if i+offset < n:
                dp[i][i+offset] = min(
                    dp[i][i+offset-1] if i+offset-1 < n else MAX_VAL,
                    dp[i+offset][i+offset] if i+offset < n else MAX_VAL
                )
                maxes[offset] = max(maxes[offset], dp[i][i+offset])

    return maxes




tests = int(stdin.readline())

for _ in range(tests):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))

    print(" ".join(str(e) for e in max_min_window_size(arr)))
