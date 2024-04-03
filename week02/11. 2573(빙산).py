# 난이도 (상) : DFS

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    sea_list = []
    while queue:
        x, y = queue.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    sea += 1
                elif graph[nx][ny] > 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        if sea > 0:
            sea_list.append((x, y, sea))
    for x, y, sea in sea_list:
        graph[x][y] = max(0, graph[x][y] - sea)
    return True

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
            ice.append((i, j))

result = 0
while ice:
    visited = [[False] * m for _ in range(n)]
    del_list = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0:
            del_list.append((i, j))
    if group > 1:
        print(result)
        break
    ice = sorted(list(set(ice) - set(del_list)))
    result += 1

if group < 2:
    print(0)

