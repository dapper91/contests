'''
https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0
'''

from sys import stdin
from heapq import heappop, heappush


class StreamAnalyzer(object):
    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def put(self, val):
        if len(self.left_heap) == len(self.right_heap):
            if self.right_heap and val > self.right_heap[0]:
                heappush(self.right_heap, val)
                val = heappop(self.right_heap)

            heappush(self.left_heap, -val)

        else:
            heappush(self.right_heap, val)
            if -self.left_heap[0] > self.right_heap[0]:
                val1 = -heappop(self.left_heap)
                val2 = heappop(self.right_heap)

                heappush(self.left_heap, -val2)
                heappush(self.right_heap, val1)

    def get_median(self):
        if len(self.left_heap) == 0:
            return None

        if len(self.left_heap) == len(self.right_heap):
            return (-self.left_heap[0] + self.right_heap[0]) // 2
        else:
            return -self.left_heap[0]


sa = StreamAnalyzer()

n = int(stdin.readline())

for _ in range(n):
    sa.put(int(stdin.readline()))
    print(sa.get_median())
