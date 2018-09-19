'''
https://practice.geeksforgeeks.org/problems/similar-expressions/0
'''

from sys import stdin
from collections import defaultdict


def count(s):
    stack = []
    minuses = 0
    vars_dict = defaultdict(int)

    for c in s:
        if c == '+':
            pass
        elif c == '-':
            stack.append(c)
            minuses += 1
        elif c == '(':
            stack.append(c)
        elif c == ')':
            stack.pop()
            while stack and stack[-1] == '-':
                stack.pop()
                minuses -= 1
        else:
            vars_dict[c] += -1 if minuses % 2 else 1
            if vars_dict[c] == 0:
                del vars_dict[c]

            while stack and stack[-1] == '-':
                stack.pop()
                minuses -= 1

    return vars_dict

def is_equal(s1, s2):
    return count(s1) == count(s2)


tests = int(stdin.readline())

for _ in range(tests):
    s1 = stdin.readline().strip()
    s2 = stdin.readline().strip()

    if is_equal(s1, s2):
        print("YES")
    else:
        print("NO")
