# 난이도 (중) : BFS

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

r, c = map(int, input().split())
# 비어있는 곳 '.' / 물이 차있는 지역 '*' / 돌 'X' / 비버굴 'D' / 고슴도치 'S'
graph = [list(input()) for _ in range(r)]

# 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다 = 물이 차고 고슴도치가 이동해야 한다.
visited = [[-1] * c for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

for x in range(r):
    for y in range(c):
        if graph[x][y] == '*':          # 물 좌표를 앞에 추가
            queue.appendleft((x, y))
        elif graph[x][y] == 'S':
            queue.append((x, y))        # 고슴이 좌표 추가
            visited[x][y] = 0           # 출발점에 시간 0 저장

result = -1
while queue:
    x, y = queue.popleft()
    cur = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if visited[nx][ny] != -1:                           # 방문 완료
            continue
        if graph[nx][ny] == "*" or graph[nx][ny] == "X":    # 물, 돌
            continue
        if cur == "*" and graph[nx][ny] == "D":             # 물이 비버네 갈려면 무시
            continue

        if cur == "S":
            if graph[nx][ny] == "D":
                result = visited[x][y] + 1
                break
            visited[nx][ny] = visited[x][y] + 1
        graph[nx][ny] = cur
        queue.append((nx, ny))

    if result != -1:
        break

print("KAKTUS" if result == -1 else result)