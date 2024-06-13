# 난이도 (상) : DP

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
travel_cost = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
dp = [[INF] * (1 << n) for _ in range(n)]


def dfs(x, visited):
    if visited == (1 << n) - 1:     # 모든 도시를 방문했다면
        if dp[x][0]:                # 출발점으로 가는 경로가 있을 때
            return dp[x][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return INF

    if dp[x][visited] != INF:       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    for i in range(1, n):           # 모든 도시를 탐방
        if not dp[x][i]:            # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip
            continue

        # 점화식 부분(위 설명 참고)
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + dp[x][i])
    return dp[x][visited]


print(dfs(0, 1))
