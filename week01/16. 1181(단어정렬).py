import sys

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

result = []
for _ in range(t):
    result.append(input())
result = list(set(result))
result.sort(key=lambda x: (len(x), x))

for i in result:
    print(i)