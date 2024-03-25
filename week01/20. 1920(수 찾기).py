# 이진 탐색

import sys
def input():
    return sys.stdin.readline().rstrip()

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n1 = int(input())
_list1 = list(map(int, input().split()))

n2 = int(input())
_list2 = list(map(int, input().split()))

_list1.sort()
for i in _list2:
    print(1 if binary_search(_list1, i, 0, len(_list1) - 1) else 0)

# =================시간 초과=================
# set(list1)으로 중복을 줄인다면 통과!
set_list1 = set(_list1)
for num in _list2:
    print(1 if num in set_list1 else 0)