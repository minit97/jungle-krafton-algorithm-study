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


# ======================================================================
def get(current_index, sum):
    global count
    # 종료조건 : 인덱스를 넘어갔을 때
    if current_index >= n:
        return 0

    # 우선 현 인덱스 값을 더해주고 나중에 현 인덱스 값을 포함하지 않을 거면 그떄 뺀다
    # 이걸 안 하니깐 정답값이 0일 때 무조건 if문 조건에 걸려서 count가 증가
    sum += arr[current_index]
    if sum == s:
        count += 1

    # 현 인덱스를 포함한다.
    get(current_index + 1, sum)
    # 현 인덱스 값을 포함하지 않는다.
    get(current_index + 1, sum - arr[current_index])


if __name__ == "__main__":
    values = sys.stdin.readline().rstrip().split(" ")
    n = int(values[0])
    s = int(values[1])
    arr = []

    numbers = sys.stdin.readline().rstrip().split(" ")
    for i in range(n):
        arr.append(int(numbers[i]))

    count = 0
    get(0, 0)

    print(count)