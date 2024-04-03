# 난이도 (중) : 위상정렬

import sys
from collections import deque, defaultdict

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    indegree[x] += 1

result = [[0] * (n + 1) for _ in range(n + 1)]
def topology_sort():
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        for next, cost in graph[now]:
            # 기본 부품
            if result[now].count(0) == n + 1:
                result[next][now] += cost

            # 중간 부품
            else:
                for i in range(1, n + 1):
                    result[next][i] += result[now][i] * cost

            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)

topology_sort()

for x in result[n]:
    if x[1] > 0:
        print(*x)