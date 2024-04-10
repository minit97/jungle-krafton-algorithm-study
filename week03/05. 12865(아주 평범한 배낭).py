# 난이도 (중) : DP

import sys

def input():
    return sys.stdin.readline().rstrip()


# ========================= 6000ms : 바텀업 =========================
# 물건 수/ 버틸 수 있는 무게
n, k = map(int, input().split())
bag = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= bag[i - 1][0]:  # 버틸 수 있는 무게 >= 가방의 무게
            # 기존 dp에서 + 현재 가방 가치 / 왼쪽 dp 가치
            dp[i][j] = max(bag[i - 1][1] + dp[i - 1][j - bag[i - 1][0]], dp[i - 1][j])
        else:
            # 왼쪽 dp 가치
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])

# ========================= 3000ms : 탑다운 =========================
N, K = map(int, input().split())
knapsack = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for w, v in knapsack:
    for j in range(K, w - 1, -1):   # 버틸 수 있는 무게 ~ 현재 가방의 무게 까지?
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[K])