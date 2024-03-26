# 다시 풀기!
# 중 : 완탐 문제

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
travel_cost = [list(map(int, input().split())) for _ in range(n)]

# ===================== 백트래킹 : 356ms =====================
min_value = sys.maxsize
visited = [False] * n
def dfs_backtracking(start, next, value):
    global min_value

    if sum(visited) == n and travel_cost[next][start] != 0:
        min_value = min(min_value, value + travel_cost[next][start])
        return
    for i in range(n):
        # 1. 도시 비용 0 x
        # 2. 이미 방문 x
        # 3. 저장되어 있는 최소값보다 작다면
        if travel_cost[next][i] != 0 and not visited[i] and value < min_value:
            visited[i] = True
            dfs_backtracking(start, i, value + travel_cost[next][i])
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs_backtracking(i, i, 0)
    visited[i] = False
print(min_value)