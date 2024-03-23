# 리스트면 시간 초과

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

t = int(input())

queue = deque()
for _ in range(t):
    s = input()
    if 'push' in s:
        queue.append(s.split(' ')[1])
    elif s == 'pop':
        print(queue.popleft() if len(queue) > 0 else -1)
    elif s == 'size':
        print(len(queue))
    elif s == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif s == 'front':
        print(queue[0] if len(queue) > 0 else -1)
    elif s == 'back':
        print(queue[-1] if len(queue) > 0 else -1)