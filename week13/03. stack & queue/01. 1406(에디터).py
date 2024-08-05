import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

s = list(map(str, input()))
t = int(input())

cusor = len(s)

queue = deque(s)
for _ in range(t):
    c = input()
    if c == 'L':
        queue.rotate(-1)
    elif c == 'D':
        queue.rotate(1)
    elif c == 'B':
        queue.pop()
    else:
        a, b = c.split()
        queue.appendleft(b)
print(''.join(map(str, queue)))

