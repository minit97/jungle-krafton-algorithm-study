# 난이도 (하) : 위상 정렬

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())    # a가 앞에 서야한다.
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        now = queue.pop()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    return result
result_list = topology_sort()
print(*result_list)