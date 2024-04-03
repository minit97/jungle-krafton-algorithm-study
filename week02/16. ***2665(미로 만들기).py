# 난이도 (중) : BFS

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]  # 0은 검은 방, 1은 흰 방

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 1. 다익스트라 ========================================================================
import heapq

INF = int(1e9)
distance = [[INF] * n for _ in range(n)]
def dijktra(start_x, start_y):
    distance[0][0] = 0

    heap = []
    heapq.heappush(heap, (0, start_x, start_y))
    while heap:
        cost, x, y = heapq.heappop(heap)
        if x == (n - 1) and y == (n - 1):
            print(cost)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if distance[nx][ny] <= cost + 1:    # 이미 방문한 것들 걸러냄.
                continue

            if graph[nx][ny] == 0:  # 검은방
                distance[nx][ny] = min(distance[nx][ny], cost + 1)
            else:                   # 흰방
                distance[nx][ny] = min(distance[nx][ny], cost)
            heapq.heappush(heap, (distance[nx][ny], nx, ny))

dijktra(0, 0)

# 2. 큐 ========================================================================
from collections import deque

visited = [[-1] * n for _ in range(n)]
def bfs(start_x, start_y):
    visited[start_x][start_y] = 0

    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:      # 흰방
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny))
                else:                       # 검은방
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    print(visited[n - 1][n - 1])

bfs(0, 0)