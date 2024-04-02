# 난이도 (중) : DFS
import sys

sys.setrecursionlimit(10 ** 9)
def input():
    return sys.stdin.readline().rstrip()

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            result[i] = v
            dfs(graph, i, visited)

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
result = [0] * (n + 1)

dfs(graph, 1, visited)
for i in range(2, n + 1):
    print(result[i])
