# 다시 풀기!
# 중

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

board_size = int(input())    # 보드의 크기
apple_cnt = int(input())    # 사과의 개수

graph = [[0] * board_size for _ in range(board_size)]
# 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 사과 위치 세팅
for _ in range(apple_cnt):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 2

# 뱀 회전 위치 세팅
snake_turn_cnt = int(input())
_dict = {}
for _ in range(snake_turn_cnt):
    # L : 왼쪽 90도, D : 오른쪽 90도
    second, direction = input().split()
    _dict[int(second)] = direction

# 뱀 회전 함수
def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

queue = deque()         # 뱀 몸통이 있는 곳
queue.append((0, 0))
x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0

while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    # 벗어나면 break
    if x < 0 or x >= board_size or y < 0 or y >= board_size:
        break

    if graph[x][y] == 2:    # 사과 있는 곳
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in _dict:
            turn(_dict[cnt])
    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in _dict:
            turn(_dict[cnt])
    else:   # 값이 1이면 내 몸통이 있는 곳
        break
print(cnt)