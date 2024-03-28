# 다시 풀기!
# 중 : 스택

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_list = list(map(int, input().split()))

stack = []
result = []

for i in range(n):
    while stack:
        if stack[-1][0] > _list[i]:
            result.append(stack[-1][1] + 1)
            break
        else:
            stack.pop()

    if not stack:
        result.append(0)

    stack.append((_list[i], i))         # value, index

print(' '.join(map(str, result)))
# print(*result)    # 모든 요소를 공백으로 구분하여 출력