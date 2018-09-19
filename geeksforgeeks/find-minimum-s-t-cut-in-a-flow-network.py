'''
https://practice.geeksforgeeks.org/problems/find-minimum-s-t-cut-in-a-flow-network/0
'''

from sys import stdin
from copy import deepcopy


def dfs_path(graph, src, dst, visited=None):
    if visited is None:
        visited = [False] * len(graph)

    if src == dst:
        return [src]

    path = None
    visited[src] = True
    for v, cost in enumerate(graph[src]):
        if cost > 0 and not visited[v]:
            subpath = dfs_path(graph, v, dst, visited)
            if subpath is not None:
                path = [src] + subpath
                break

    return path

def max_flow(graph, path):
    return min([graph[v1][v2] for v1, v2 in zip(path, path[1:])])

def dfs(graph, src, visited=None):
    if visited is None:
        visited = [False] * len(graph)

    visited[src] = True
    for v, cost in enumerate(graph[src]):
        if cost > 0 and not visited[v]:
            dfs(graph, v, visited)

    return {v for v, f in enumerate(visited) if f}

def min_cut(graph, src, dst):
    residual_graph = deepcopy(graph)

    while True:
        cur_path = dfs_path(residual_graph, src, dst)
        if cur_path is not None:
            cur_flow = max_flow(residual_graph, cur_path)
            for v1, v2 in zip(cur_path, cur_path[1:]):
                residual_graph[v1][v2] -= cur_flow
                residual_graph[v2][v1] += cur_flow
        else:
            break

    result = []
    set1 = dfs(residual_graph, src)

    for v1 in set1:
        for v2, cost in enumerate(graph[v1]):
            if cost > 0 and v2 not in set1:
                result.append((v1, v2))

    return result


tests = int(stdin.readline())

for _ in range(tests):
    n = int(stdin.readline())

    arr = []
    while len(arr) != n * n:
        arr.extend(list(map(int, stdin.readline().split())))

    graph = [arr[n*i:n*i+n] for i in range(n)]
    src, dst = map(int, stdin.readline().split())

    cut = min_cut(graph, src, dst)
    if cut:
        print(" ".join("{} {}".format(*edge) for edge in cut))
    else:
        print(-1)
