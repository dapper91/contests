'''
https://practice.geeksforgeeks.org/problems/sum-of-xor-of-all-pairs/0
'''

from sys import stdin


def xor_sum(arr):
    n = len(arr)
    ones = [0] * 20

    for e in arr:
        for i in range(20):
            ones[i] += e & 0x1
            e >>= 1

    result = 0
    for i, e in enumerate(ones):
        result += 2 ** i * (e) * (n - e)

    return result


tests = int(stdin.readline())

for _ in range(tests):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))

    print(xor_sum(arr))
