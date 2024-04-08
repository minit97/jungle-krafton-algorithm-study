# 난이도 (중) : DP
import sys

def input():
    return sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    coin_list = list(map(int, input().split()))
    wanted_coin = int(input())

    dp = [0] * (wanted_coin + 1)
    dp[0] = 1                                   # 0원으로 만드는 가지 수 1개
    for coin in coin_list:
        for money in range(wanted_coin + 1):
            if money >= coin:                   # 금액이 동전의 가치보다 크면
                dp[money] += dp[money - coin]   # 해당 dp는 금액 - 동전에 해당하는 dp합
    print(dp[wanted_coin])