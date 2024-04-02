# 난이도 (하) : BFS

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0 , 1, -1]

queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] += graph[x][y]
            queue.append((nx, ny))

print(graph[n - 1][m - 1])