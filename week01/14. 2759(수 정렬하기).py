import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())

result = []
for _ in range(t):
    result.append(int(input()))

result.sort()
for i in result:
    print(i)