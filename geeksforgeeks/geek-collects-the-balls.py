'''
https://practice.geeksforgeeks.org/problems/geek-collects-the-balls/0
'''

from sys import stdin


def max_balls(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    i1, i2 = 0, 0
    s, s1, s2 = 0, 0, 0

    while i1 != n1 and i2 != n2:
        if arr1[i1] == arr2[i2]:
            while i1 < n1 - 1 and arr1[i1] == arr1[i1+1]:
                s1 += arr1[i1]
                i1 += 1

            while i2 < n2 - 1 and arr2[i2] == arr2[i2+1]:
                s2 += arr2[i2]
                i2 += 1

            s1 += arr1[i1]
            s2 += arr2[i2]
            s += max(s1, s2)
            s1, s2 = 0, 0
            i1 += 1; i2 += 1

        elif arr1[i1] < arr2[i2]:
            s1 += arr1[i1]
            i1 += 1
        else:
            s2 += arr2[i2]
            i2 += 1

    while i1 != n1:
        s1 += arr1[i1]
        i1 += 1

    while i2 != n2:
        s2 += arr2[i2]
        i2 += 1

    s += max(s1, s2)

    return s


tests = int(stdin.readline())

for _ in range(tests):
    n1, n2 = list(map(int, stdin.readline().split()))

    arr1 = list(map(int, stdin.readline().split()))
    arr2 = list(map(int, stdin.readline().split()))

    print(max_balls(arr1, arr2))
