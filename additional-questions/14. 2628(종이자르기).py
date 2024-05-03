# 다시

import sys
def input():
    return sys.stdin.readline().rstrip()

x, y = map(int, input().split())
cut_cnt = int(input())

width = [0, x]
height = [0, y]

for _ in range(cut_cnt):
    cut_type, cut_local = map(int, input().split())
    if cut_type == 0:
        height.append(cut_local)
    else:
        width.append(cut_local)

width.sort()
height.sort()

result = 0
for i in range(1, len(width)):
    for j in range(1, len(height)):
        x = width[i] - width[i - 1]
        y = height[j] - height[j - 1]
        result = max(result, x * y)
print(result)