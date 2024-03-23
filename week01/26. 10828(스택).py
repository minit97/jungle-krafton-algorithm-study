import sys

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

stack = []
for _ in range(t):
    s = input()
    if 'push' in s:
        num = int(s.split()[1])
        stack.append(num)
    elif s == 'pop':
        print(stack.pop() if len(stack) > 0 else -1)
    elif s == 'size':
        print(len(stack))
    elif s == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif s == 'top':
        print(stack[-1] if len(stack) > 0 else -1)