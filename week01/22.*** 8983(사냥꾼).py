# 다시 풀기!
# 상 : 이분탐색
import sys
def input():
    return sys.stdin.readline().rstrip()

# 사대의 수, 동물의 수, 사정거리
m, n, l = map(int, input().split())

shoot_place = list(map(int, input().split()))
shoot_place.sort()

animal_place = []
for _ in range(n):
    x, y = map(int, input().split())
    animal_place.append((x, y))

# ====================== 이진 탐색 ======================
def binary_search(arr, x_target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x_target:
            return mid
        elif arr[mid] < x_target:
            start = mid + 1
        else:
            end = mid - 1
    return end

result = 0
for x, y in animal_place:
    # 가장 가까운 사대
    shoot_idx = binary_search(shoot_place, x)

    dist = abs(x - shoot_place[shoot_idx]) + y
    # 이분 탐색의 오차로 인해, 찾은 것보다 오른쪽에 있는 사대가 더 가까운 사대일 수도 있다.
    dist_right = abs(x - shoot_place[shoot_idx + 1]) + y if shoot_idx < m-1 else float('inf')     # float('inf') : 무한대

    min_dist = min(dist, dist_right)
    if min_dist <= l:
        result += 1
print(result)


# ====================== 라이브러리 사용 ======================
from bisect import bisect_left

cnt = 0
for a in animal_place:
    x, y = a
    px = bisect_left(shoot_place, x)  # x좌표 가장 가까운 사대 x좌표

    if px == len(shoot_place):
        px -= 1
    if abs(shoot_place[px] - x) > abs(shoot_place[px - 1] - x):
        px -= 1

    if abs(x - shoot_place[px]) + y <= l:
        cnt += 1

print(cnt)
