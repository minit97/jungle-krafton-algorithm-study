# 난이도 (중) : DP

import sys

def input():
    return sys.stdin.readline().rstrip()

INF = int(1e9)

n = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]            # dp[시작행렬][끝행렬] = 최소 연산 횟수

for term in range(1, n):                    # 간격
    for start in range(n):                  # 첫행렬 : start, 끝행렬: start + term
        if start + term == n:               # 범위를 벗어나면 무시
            break

        dp[start][start + term] = INF       # 지금 계산할 첫행렬과 끝행렬

        for t in range(start, start + term):
            dp[start][start + term] = min(dp[start][start + term],
                                        dp[start][t] + dp[t + 1][start + term] + matrix[start][0] * matrix[t][1] * matrix[start + term][1])
                                        # dp[1][1] = 0 + dp[2][3] = 36      + 5 x 3 x 6 = 90        == 126
                                        # dp[1][2] = 30 + dp[3][3] = 0      + 5 x 2 x 6 = 60        == 90
        print(dp)

print(dp[0][n - 1])