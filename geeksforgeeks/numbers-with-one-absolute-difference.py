'''
https://practice.geeksforgeeks.org/problems/numbers-with-one-absolute-difference/0
'''

from sys import stdin


def digits_count(n):
    counter = 0

    while n != 0:
        n //= 10
        counter += 1

    return counter

def find_numbers(n, digits = None):
    if digits is None:
        digits = digits_count(n)

    if digits == 1:
        return [str(i) for i in range(10)]

    result = []

    res = func(n, digits - 1)
    result.extend(res)

    for c in [str(i) for i in range(1, 10)]:
        for r in res:
            if abs(int(c) - int(r[0])) == 1 and len(r) == digits - 1:
                num = c + r
                if int(num) > n:
                    return result
                else:
                    result.append(num)

            if int(c) == 1 and len(r) == digits - 2 and int(r[0]) == 1:
                num = c + '0' + r
                if int(num) > n:
                    return result
                else:
                    result.append(num)

    return result


tests = int(stdin.readline())

for _ in range(tests):

    n = int(stdin.readline().strip())
    result = find_numbers(n)[10:]
    if result:
        print(" ".join(result))
    else:
        print(-1)
