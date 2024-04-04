import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(graph, start_x, start_y, visited):
    visited[start_x][start_y] = True
    queue = deque()
    queue.append((start_x, start_y))

    result = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                result += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return result

visited = [[False] * n for _ in range(n)]
result_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result_list.append(bfs(graph, i, j, visited))
result_list.sort()

print(len(result_list))
for i in result_list:
    print(i)