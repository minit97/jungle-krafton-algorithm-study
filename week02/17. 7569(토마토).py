# 난이도 (중) : BFS

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

m, n, h = map(int, input().split())
# 1 : 익은 토마토 / 0 : 익지 않은 토마토 / -1 : 토마토가 들어 있지 않은 칸
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()
def bfs():
    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if graph[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                    queue.append((nz, ny, nx))
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    visited[nz][ny][nx] = True

for z in range(h):
    for y in range(n):
        for x in range(m):
            if not visited[z][y][x] and graph[z][y][x] == 1:
                queue.append((z, y, x))
                visited[z][y][x] = True
bfs()

# 토마토가 익을 때까지의 기간
# 익어 있으면 0 / 익지 못하면 -1
day = 0
for i in graph:
    for j in i:
        if 0 in j:
            print(-1)
            exit(0)
        day = max(day, max(j))
print(day - 1)