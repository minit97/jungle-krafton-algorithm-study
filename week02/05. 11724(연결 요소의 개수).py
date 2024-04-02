# 난이도 (하) : 그래프 탐색 기본

import sys

def input():
    return sys.stdin.readline().rstrip()

# ======================== dfs 방식 ========================
sys.setrecursionlimit(10 ** 6)
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# ======================== bfs 방식 ========================
from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# ======================== 입력 시작!!! ========================
# 정점의 수, 간선의 수
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
result = 0

for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        result += 1

print(result)
