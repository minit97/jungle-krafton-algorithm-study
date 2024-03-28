import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())
result = [int(input()) for _ in range(t)]
result.sort()

for i in result:
    print(i)