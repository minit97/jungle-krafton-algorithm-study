from collections import deque

n, k = map(int, input().split())

_list = [i for i in range(1, n + 1)]
queue = deque(_list)

result = []
for _ in range(len(_list)):
    queue.rotate(-(k - 1))
    result.append(queue.popleft())

print('<', end='')
print(', '.join(map(str, result)), end='')
print('>')
