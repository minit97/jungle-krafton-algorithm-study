import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
stairs = [int(input()) for _ in range(n)]

dp = [0] * n
dp[0] = stairs[0]

if n > 1:
    dp[1] = stairs[0] + stairs[1]

for i in range(2, n):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[-1])