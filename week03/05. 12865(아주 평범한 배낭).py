# 난이도 (중) : DP

import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
bag = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    if i >= bag[i][0]:
        dp[i] = max(bag[i][1], dp[i - bag[i][0]] + bag[i][1])
    else:
        dp[i] = dp[i - 1]

print(dp[k])
