import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

def dfs(graph, start_x, start_y, visited):
    visited[start_x][start_y] = True
    if start_x >= n or start_y >= m:
        return

    if graph[start_x][start_y] == '-' and start_y < m -1 and graph[start_x][start_y + 1] == '-':
        dfs(graph, start_x, start_y + 1, visited)
    elif graph[start_x][start_y] == '|' and start_x < n - 1 and graph[start_x + 1][start_y] == '|':
        dfs(graph, start_x + 1, start_y, visited)

result = 0
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(graph, i, j, visited)
            result += 1
print(result)