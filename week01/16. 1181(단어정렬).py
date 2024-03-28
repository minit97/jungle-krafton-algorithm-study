import sys

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

result = [input() for _ in range(t)]
result = list(set(result))
result.sort(key=lambda x: (len(x), x))

for i in result:
    print(i)