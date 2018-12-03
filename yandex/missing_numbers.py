import heapq
from itertools import tee


def iter_missing_numbers(it):
    it1, it2 = tee(it)    
    val1, val2 = next(it1, None), next(it2, None)
    
    val2 = next(it2, None)

    while val1 is not None and val2 is not None:
        yield from range(val1 + 1, val2)
        val1, val2 = next(it1, None), next(it2, None)

def missing_numbers(*iters):
    yield from iter_missing_numbers(heapq.merge(*iters))

lists = [18], [1,2,4,5,7,8,11], [1,2,3,5,6,15], [16,18], []

for val in missing_numbers(*lists):
    print(val)
