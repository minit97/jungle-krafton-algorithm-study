# 난이도 (상) : DP

# 문제 이해
# 1. 돌 번호가 증가하는 순서대로만 이동
# 2. 제일 처음에 점프하는 칸은 한 칸 / x : 이전 칸 이동, 가속 : x + 1, 감소 : x - 1
# 3. 작은 돌은 착지 불가능하다.

import sys
import math

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
not_land = [int(input()) for _ in range(m)]

dp = [[float('inf')] * (int(math.sqrt(2 * n)) + 2) for _ in range(n + 1)]       # 현재 돌까지 점프해서 올 수 있는 이전 돌의 점프 횟수를 기록할 2차원 dp배열
dp[1][0] = 0

for i in range(2, n + 1):
    if i in not_land:
        continue
    for j in range(1, int(math.sqrt(2 * i)) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

result = min(dp[n])
print(-1 if result == float('inf') else result)



