'''
https://practice.geeksforgeeks.org/problems/maximum-index/0
'''

from sys import stdin


def bisect_left(arr, e, begin=0, end=None, key=None):
    if end is None:
        end = len(arr)

    size = end - begin

    if size == 0:
        return begin

    pivot = begin + size//2
    middle = key(arr[pivot])

    if e >= middle:
        return bisect_left(arr, e, 0, pivot, key)
    else:
        return bisect_left(arr, e, pivot + 1, end, key)


def max_index(arr):
    stack = []

    max_diff = 0

    for i, e in enumerate(arr):
        if not stack or e < stack[-1][1]:
            stack.append((i, e))
        else:
            stack_idx = bisect_left(stack, e, key=lambda x: x[1])
            min_less_idx, _ = stack[stack_idx]
            max_diff = max(max_diff, i - min_less_idx)

    return max_diff


tests = int(stdin.readline())

for _ in range(tests):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))

    print(max_index(arr))
