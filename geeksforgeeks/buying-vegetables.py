'''
https://practice.geeksforgeeks.org/problems/buying-vegetables/0
'''

from sys import stdin

def find_optimal_purchase(sellers):
    dp = [[0, 0, 0] for _ in range(len(sellers) + 1)]

    for i, seller in enumerate(sellers, 1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + seller[0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + seller[1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + seller[2]

    print(dp)

    return min(dp[len(sellers)])


tests = int(stdin.readline())

for _ in range(tests):
    n = int(stdin.readline())

    sellers = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

    print(find_optimal_purchase(sellers))
