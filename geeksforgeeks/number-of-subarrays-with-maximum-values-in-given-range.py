'''
https://practice.geeksforgeeks.org/problems/number-of-subarrays-with-maximum-values-in-given-range/0
'''

from sys import stdin


def subarrays(arr, l, r):
    total_counter = 0
    stash_counter = 0
    prev_counter = 0

    for i in range(len(arr)):
        val = arr[i]
        cur_counter = 0

        if val > r:
            cur_counter = 0
            stash_counter = 0
        else:
            cur_counter += prev_counter
            if val >= l:
                cur_counter += 1
                cur_counter += stash_counter
                stash_counter = 0
            else:
                stash_counter += 1

        prev_counter = cur_counter
        total_counter += cur_counter

    return total_counter


tests = int(stdin.readline())

for _ in range(tests):
    n, l, r = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))

    print(subarrays(arr, l, r))
