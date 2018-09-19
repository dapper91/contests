'''
https://practice.geeksforgeeks.org/problems/make-matrix-beautiful/0
'''

from sys import stdin
from heapq import heappop, heappush, heapify, heapreplace


def all_equals(heap, maxv):
    return heap[0][0] == maxv

def beautify_mat(mat):
    n = len(mat)
    row_sum = [(sum([mat[r][c] for c in range(n)]), r) for r in range(n)]
    col_sum = [(sum([mat[r][c] for r in range(n)]), c) for c in range(n)]

    max_rs = max(row_sum)[0]
    max_cs = max(col_sum)[0]

    heapify(row_sum)
    heapify(col_sum)

    ops = 0
    while not all_equals(row_sum, max_rs) or not all_equals(col_sum, max_cs):
        rv, ri = row_sum[0]
        cv, ci = col_sum[0]

        diff = min(max_rs - rv, max_cs - cv) or 1

        max_rs = max(max_rs, rv+diff)
        max_cs = max(max_cs, cv+diff)

        heapreplace(row_sum, (rv+diff, ri))
        heapreplace(col_sum, (cv+diff, ci))

        mat[ri][ci] += diff
        ops += diff

    return ops


tests = int(stdin.readline())

for _ in range(tests):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))

    mat = [arr[i*n:i*n+n] for i in range(len(arr)//n)]

    print(beautify_mat(mat))
