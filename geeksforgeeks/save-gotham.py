'''
https://practice.geeksforgeeks.org/problems/save-gotham/0
'''

from sys import stdin


def heights_sum(towers):
    stack = []
    hsum = 0

    for height in reversed(towers):
        while stack and height >= stack[-1]:
            stack.pop()

        if stack:
            hsum = (hsum + stack[-1]) % 1000000001
        stack.append(height)

    return hsum


tests = int(stdin.readline())

for _ in range(tests):
    n = int(stdin.readline())
    towers = list(map(int, stdin.readline().split()))

    print(heights_sum(towers))
