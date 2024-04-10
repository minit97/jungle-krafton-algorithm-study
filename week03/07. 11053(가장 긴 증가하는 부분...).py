# 난이도 (중) : DP

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))