# 다시 풀기!
# 중 : 이분 탐색
import sys
def input():
    return sys.stdin.readline().rstrip()

n, required_h = map(int, input().split())
tree_height = list(map(int, input().split()))


# ============ 이분 탐색 : 4800ms ============
tree_height.sort()
start = 1
end = max(tree_height)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in tree_height:
        if i > mid:
            total += i - mid
    if total >= required_h:
        start = mid + 1
    else:
        end = mid - 1
print(end)

# ============ 속도 개선 - 그리디 방식인 거 같은데... : 820ms ============
tree_height.sort(reverse=True)
tree_height.append(0)

sum = 0
for i in range(n + 1):
    sum += (i + 1) * (tree_height[i] - tree_height[i + 1])
    if sum >= required_h:
        # 나무당 얻어야하는 높이 + 자르는 기준의 나무 길이
        h = (sum - required_h) / (i + 1) + tree_height[i + 1]
        h = int(h)
        print(h)
        break


