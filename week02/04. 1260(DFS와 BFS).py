# 난이도 (하) : 그래프 탐색 기본

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs_result = []
def dfs(graph, start, dfs_visited):
    dfs_visited[start] = True
    dfs_result.append(start)

    for i in sorted(graph[start]):
        if not dfs_visited[i]:
            dfs(graph, i, dfs_visited)


bfs_result = []
def bfs(graph, start, bfs_visited):
    queue = deque([start])
    bfs_visited[start] = True

    while queue:
        now = queue.popleft()
        bfs_result.append(now)

        for i in sorted(graph[now]):
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = True


visited = [False] * (n + 1)
dfs(graph, v, visited)
visited = [False] * (n + 1)
bfs(graph, v, visited)

print(*dfs_result)
print(*bfs_result)