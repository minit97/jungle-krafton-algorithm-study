import sys

def input():
    return sys.stdin.readline().rstrip()

a_cnt, b_cnt = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

print(len(set(a_list) - set(b_list)) + len(set(b_list) - set(a_list)))
