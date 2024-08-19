# 문제 이해를 다시 한번 해보자!!

n = int(input())
k = int(input())

start = 1
end = k

while start <= end:
    mid = (start + end) // 2

    index = 0
    for i in range(1, n + 1):
        index += min(mid // i, n)

    if index < k:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)