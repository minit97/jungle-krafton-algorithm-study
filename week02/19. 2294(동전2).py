# 난이도 (상) : BFS

import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

dp = [10001] * (k + 1)
dp[0] = 0

for c in coin:
    for i in range(c, k + 1):
        if dp[i] > 0:
            dp[i] = min(dp[i], dp[i - c] + 1)

print(-1 if dp[k] == 10001 else dp[k])