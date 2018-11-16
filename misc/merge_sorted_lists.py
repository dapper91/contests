from heapq import heappush, heappop


def merge_sorted_lists(lists):
    result = []
    heap = []

    for idx, it in enumerate(map(iter, lists)):
        val = next(it, None)
        if val is not None:
            heappush(heap, (val, idx, it))

    while heap:
        val, idx, it = heappop(heap)
        result.append(val)

        val = next(it, None)
        if val is not None:
            heappush(heap, (val, idx, it))

    return result


lists = [
    [8,9],
    [0,1,2],
    [],
    [2,3,4,5],
    [1,1,2,3]
]

result = merge_sorted_lists(lists)

print(result)
