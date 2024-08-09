# ============== 시간 초과 ==============
# import sys
#
# def input():
#     return sys.stdin.readline().rstrip()
#
# n = int(input())
# my_cards = list(map(int, input().split()))
#
# m = int(input())
# check_cards = list(map(int, input().split()))
#
# for i in check_cards:
#     print(1 if i in my_cards else 0, end=' ')


# ============== 이분 탐색 적용 ==============
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
my_cards = list(map(int, input().split()))
my_cards.sort()

m = int(input())
check_cards = list(map(int, input().split()))

def binary_search(check_num):
    start = 0
    end = len(my_cards) - 1

    while start <= end:
        mid = (start + end) // 2
        if check_num == my_cards[mid]:
            return 1
        elif check_num < my_cards[mid]:
            end = mid - 1
        elif check_num > my_cards[mid]:
            start = mid + 1
    return 0

for i in check_cards:
    print(binary_search(i), end=' ')

# ============== dictionary 사용 ==============
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
my_cards = list(map(int, input().split()))

m = int(input())
check_cards = list(map(int, input().split()))

_dict = {}
for i in my_cards:
    _dict[i] = 0

for i in check_cards:
    print(1 if i in _dict else 0)