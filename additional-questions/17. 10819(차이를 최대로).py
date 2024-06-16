import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

# 절댓값이 최대들의 합.