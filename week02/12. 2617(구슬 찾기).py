# 난이도 (상) : DFS

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

bigger_list = [[] for _ in range(n + 1)]    # index보다 큰 수
smaller_list = [[] for _ in range(n + 1)]   # index보다 작은 수
mid = (n + 1) / 2                           # 개수 기준 중간값

for i in range(m):
    a, b = map(int, input().split())
    bigger_list[b].append(a)
    smaller_list[a].append(b)

# ================== bfs : 72ms ==================
def bfs(graph, start, visited):
    visited[start] = True
    queue = deque()
    queue.append(start)

    cnt = 0
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                cnt += 1
                visited[i] = True
                queue.append(i)
    return cnt

result = 0
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    if bfs(bigger_list, i, visited) >= mid:
        result += 1
    if bfs(smaller_list, i, visited) >= mid:
        result += 1

print(result)

# ================== dfs : 76ms ==================
def dfs(graph, start):
    count = 0
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            count += 1
            count += dfs(graph, i)
    return count

result = 0
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    if dfs(bigger_list, i) >= mid:
        result += 1
    if dfs(smaller_list, i) >= mid:
        result += 1

print(result)