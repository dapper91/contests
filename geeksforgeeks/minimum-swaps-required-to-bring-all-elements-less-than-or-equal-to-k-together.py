'''
https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together/0
'''

from sys import stdin


def min_swaps(arr, k):
    cnt = 0

    for e in arr:
        if k >= e:
            cnt += 1

    i, j, cur_cnt = 0, 0, 0
    while j < cnt:
        if arr[j] <= k:
            cur_cnt += 1
        j += 1

    max_cnt = cur_cnt
    while j < len(arr):
        if arr[i] <= k:
            cur_cnt -= 1

        if arr[j] <= k:
            cur_cnt += 1

        i += 1; j += 1

        max_cnt = max(max_cnt, cur_cnt)

    return cnt - max_cnt


tests = int(stdin.readline())

for _ in range(tests):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    k = int(stdin.readline())

    print(min_swaps(arr, k))
