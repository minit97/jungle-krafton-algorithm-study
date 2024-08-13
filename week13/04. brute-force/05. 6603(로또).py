# import sys
# import itertools
#
# def input():
#     return sys.stdin.readline().rstrip()
#
#
# while 1:
#     _list = list(map(int, input().split()))
#     if _list[0] == 0:
#         break
#
#     nums = _list[1:]
#     for i in itertools.combinations(nums, 6):
#         print(' '.join(map(str, list(i))))
#     print()

# ================ dfs ================
import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(start, depth):
    if depth == 6:
        print(' '.join(map(str, result)))
        return

    for i in range(start, len(nums)):
        result.append(nums[i])
        dfs(i + 1, depth + 1)
        result.pop()

while 1:
    _list = list(map(int, input().split()))
    if _list[0] == 0:
        break

    nums = _list[1:]
    result = []
    dfs(0, 0)
    print()