# 처음에는 bfs를 사용해서 메모리 초과가 떴다.
# 동료가 소개한 방식은 dfs 방식... 근데 dp의 느낌이 약간 안난다고 해야할까...
# 더 좋은 방식을 찾아서 올린다.

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

direction = [(1, 0), (0, 1)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            exit(0)

        dist = board[i][j]
        if i + dist < n:
            dp[i + dist][j] += dp[i][j]
        if j + dist < n:
            dp[i][j + dist] += dp[i][j]