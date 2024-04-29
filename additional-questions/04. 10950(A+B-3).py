import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)