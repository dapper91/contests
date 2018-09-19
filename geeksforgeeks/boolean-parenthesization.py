'''
https://practice.geeksforgeeks.org/problems/boolean-parenthesization/0
'''

from sys import stdin


def true_parenthesizes_count(s):
    symbols = s[0::2]
    operators = s[1::2]

    n = len(symbols)

    dpt = [[0 for _ in range(n)] for _ in range(n)]
    dpf = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dpt[i][i] += int(symbols[i] == 'T')
        dpf[i][i] += int(symbols[i] == 'F')

    for offset in range(1, n):
        for i in range(n):
            for k in range(i, i+offset):
                if i+offset < n:
                    operator = operators[k]
                    if operator == '&':
                        dpt[i][i+offset] += dpt[i][k] * dpt[k+1][i+offset]
                        dpf[i][i+offset] += dpt[i][k] * dpf[k+1][i+offset] + dpf[i][k] * dpt[k+1][i+offset] + dpf[i][k] * dpf[k+1][i+offset]

                    if operator == '|':
                        dpt[i][i+offset] += dpt[i][k] * dpt[k+1][i+offset] + dpt[i][k] * dpf[k+1][i+offset] + dpf[i][k] * dpt[k+1][i+offset]
                        dpf[i][i+offset] += dpf[i][k] * dpf[k+1][i+offset]

                    if operator == '^':
                        dpt[i][i+offset] += dpt[i][k] * dpf[k+1][i+offset] + dpf[i][k] * dpt[k+1][i+offset]
                        dpf[i][i+offset] += dpf[i][k] * dpf[k+1][i+offset] + dpt[i][k] * dpt[k+1][i+offset]

    return dpt[0][-1] % 1003

tests = int(stdin.readline())

for _ in range(tests):
    n = int(stdin.readline())
    s = stdin.readline().strip()

    print(true_parenthesizes_count(s))
