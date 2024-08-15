import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
times = list(map(int, input().split()))

# m이 분할 갯수 / 분할한 times의 합 중 최댓값

start = max(times)
end = sum(times)

while start <= end:
    mid = (start + end) // 2

    total = 0
    count = 1
    for t in times:
        if total + t > mid:
            count += 1
            total = 0
        total += t

    if count <= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)