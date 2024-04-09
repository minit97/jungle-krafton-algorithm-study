def knapsack(weights, values, capacity):
    n = len(weights)

    # DP 배열 초기화
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # DP 배열 채우기
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # 최적해 추적
    selected_items = []
    w, v = capacity, dp[n][capacity]
    for i in range(n, 0, -1):
        if v <= 0:
            break
        if v == dp[i - 1][w]:
            continue
        else:
            selected_items.append(i - 1)
            v -= values[i - 1]
            w -= weights[i - 1]

    return dp[n][capacity], selected_items

# 입력값
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

# 0/1 배낭 문제 해결 및 결과 출력
max_value, selected_items = knapsack(weights, values, capacity)
print("최대 가치:", max_value)
print("선택된 아이템 인덱스:", selected_items)
