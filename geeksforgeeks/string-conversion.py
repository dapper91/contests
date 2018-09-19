'''
https://practice.geeksforgeeks.org/problems/string-conversion/0
'''

from sys import stdin


def is_string_convertable(x, y):
    xi, yi = 0, 0
    indexes = []

    while True:
        if yi == len(y):
            break

        if xi == len(x):
            if len(indexes) == 0:
                break
            else:
                xi = indexes.pop() + 1
                yi -= 1
                continue

        if x[xi].upper() == y[yi]:
            indexes.append(xi)
            xi += 1; yi += 1
        else:
            if x[xi].isupper():
                if len(indexes) == 0:
                    break
                else:
                    xi = indexes.pop() + 1
                    yi -= 1
            else:
                xi += 1

    return len(indexes) == len(y)

tests = int(stdin.readline())

for _ in range(tests):
    n1, n2 = map(int, stdin.readline().split())
    x, y = stdin.readline().split()

    if is_string_convertable(x, y):
        print("Yes")
    else:
        print("No")
