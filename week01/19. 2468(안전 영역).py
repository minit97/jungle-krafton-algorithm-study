# 다시 풀기!
# 상 : 완전탐색
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_local = []
max_height = -1e10
for _ in range(n):
    _local.append(list(map(int, input().split())))
    max_height = max(max_height, max(_local[-1]))

# 상 하 좌 우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# =================== dfs : 1500ms ===================
sys.setrecursionlimit(100000)       # 최대 재귀 깊이를 인위적으로 늘림
def dfs_sink(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n) and not _sink[nx][ny] and _local[nx][ny] > h:
            _sink[nx][ny] = True
            dfs_sink(nx, ny, h)

result = 1
for k in range(max_height):
    count = 0
    _sink = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if _local[i][j] > k and not _sink[i][j]:
                count += 1
                _sink[i][j] = True
                dfs_sink(i, j, k)
    result = max(result, count)
print(result)

# =================== bfs : 804ms ===================
from collections import deque

def bfs_sink(x, y, h):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n) and _sink[nx][ny] == 0 and _local[nx][ny] > h:
                queue.append((nx, ny))
                visited[nx][ny] = 1

result = 0
for h in range(max_height):
    count = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if _local[i][j] > h and visited[i][j] == 0:
                bfs_sink(i, j, h)
                count += 1
    result = max(result, count)
print(result)

