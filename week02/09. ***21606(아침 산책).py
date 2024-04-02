# 난이도 (중) : DFS
import sys

sys.setrecursionlimit(10**9)
def input():
    return sys.stdin.readline().rstrip()

def dfs(start, cnt):
    visited[start] = True
    for i in graph[start]:
        if location[i] == 1:
            cnt += 1
        elif not visited[i] and location[i] == 0:
            cnt = dfs(i, cnt)
    return cnt

n = int(input())
location = [0] + list(map(int, input()))

result = 0
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    if location[a] == 1 and location[b] == 1:
        result += 2

sum_value = 0
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i] and location[i] == 0:
        temp = dfs(i, 0)
        sum_value += temp * (temp - 1)
print(sum_value + result)