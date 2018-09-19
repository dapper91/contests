'''
https://practice.geeksforgeeks.org/problems/queries-on-a-matrix/0
'''

from sys import stdin


def print_mat(m):
    for row in m:
        print(" ".join([str(e) for e in row]))

def modify_mat(n, queries):
    pos_mat = [[0 for _ in range(n)] for _ in range(n)]

    for x1, y1, x2, y2 in queries:
        pos_mat[x1][y1] += 1
        if x2 != n-1 and y2 != n-1:
            pos_mat[x2+1][y2+1] += 1

    for r in range(n):
        for c in range(n):
            pos_mat[r][c] = (pos_mat[r-1][c] if r else 0) + (pos_mat[r][c-1] if c else 0) - (pos_mat[r-1][c-1] if r and c else 0) + pos_mat[r][c]


    neg_mat = [[0 for _ in range(n)] for _ in range(n)]

    for x1, y1, x2, y2 in queries:
        if y2 != n-1:
            neg_mat[x1][y2+1] -= 1
        if x2 != n-1:
            neg_mat[x2+1][y1] -= 1

    for r in range(n):
        for c in range(n):
            neg_mat[r][c] = (neg_mat[r-1][c] if r else 0) + (neg_mat[r][c-1] if c else 0) - (neg_mat[r-1][c-1] if r and c else 0) + neg_mat[r][c]


    mat = pos_mat

    for r in range(n):
        for c in range(n):
            mat[r][c] = pos_mat[r][c] + neg_mat[r][c]

    return mat


tests = int(stdin.readline())

for _ in range(tests):
    n, q = map(int, stdin.readline().split())
    queries = [tuple(map(int, stdin.readline().split())) for _ in range(q)]

    print_mat(modify_mat(n, queries))
