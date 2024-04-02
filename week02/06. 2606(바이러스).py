# 난이도 (하) : 그래프 탐색 기본

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


v = int(input())
e = int(input())

visited = [False] * (v + 1)
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited)
print(sum(visited) - 1)