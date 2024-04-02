# 난이도 (중) : DFS

def dfs(start, _check):
    global error
    if error:
        return

    visited[start] = _check
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i, -_check)
        elif visited[start] == visited[i]:
            error = True
            return

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(start, _check):
    visited[start] = _check
    queue = deque([start])
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = -1 * visited[now]
            elif visited[i] == visited[now]:
                return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (v + 1)
    for i in range(1, v + 1):
        if visited[i] == 0:
            result = bfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")
