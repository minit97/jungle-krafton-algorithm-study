def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # LCS를 저장하기 위한 2차원 배열 생성 및 초기화
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # LCS 길이 계산
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS를 역추적하여 구하기
    lcs_seq = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_seq = X[i - 1] + lcs_seq
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_seq

# 두 문자열 입력
X = input("첫 번째 문자열 입력: ")
Y = input("두 번째 문자열 입력: ")

# LCS 계산 및 출력
result = lcs(X, Y)
print("최장 공통 부분 수열:", result)
