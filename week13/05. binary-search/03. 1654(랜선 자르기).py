import sys

def input():
    return sys.stdin.readline().rstrip()

k, n = map(int, input().split())

lines = []
for _ in range(k):
    lines.append(int(input()))

start = 1
end = max(lines)

result = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for l in lines:
        count += l // mid

    if count >= n:
        result = max(mid, result)
        start = mid + 1
    elif count < n:
        end = mid - 1

print(result)
