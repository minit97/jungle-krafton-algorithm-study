import sys
def input():
    return sys.stdin.readline().rstrip()

n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    if i < x:
        print(i, end=' ')