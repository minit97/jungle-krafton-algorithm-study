import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

n, s = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

# result = 0
# def dfs_backtracking(target, size):
#     global result
#     for com in combinations(data, size):
#         if sum(com) == target:
#             result += 1
#
# for i in range(1, n + 1):
#     dfs_backtracking(s, i)
#
# print(result)


# 위 방식은 시간 초과가 있을 가능성이 있어보임. - 근데.. 완탐이라.. 상관없을 수도?
# 라이브러리를 안 사용한 방식 고민해보기! - 모르겠음

# ==================== 라이브러리 사용X - 이해하기 좀 어렵;; ====================
_list = []
result = 0
def solution(_list ,index):
    global result

    if index >= n:  #len(data)  # n = 5임
        return
    _list.append(data[index])
    solution(_list, index + 1)

    if sum(_list) == s:
        result += 1

    _list.pop()
    solution(_list, index + 1)

if n != 0:
    solution(_list, 0)
print(result)