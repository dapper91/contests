'''
https://practice.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k/0
'''

from sys import stdin


def subarr_count(arr, k):
    result = 0
    cur_prod = 1
    i, j = 0, 0

    for j in range(len(arr)):
        cur_prod *= arr[j]

        while i <= j and cur_prod >= k:
            cur_prod /= arr[i]
            i += 1

        if cur_prod < k:
            result += j - i + 1

    return result


tests = int(stdin.readline())

for _ in range(tests):
    n, k = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))

    print(subarr_count(arr, k))
