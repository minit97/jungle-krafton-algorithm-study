from collections import deque

n, k = map(int, input().split())

_list = [i for i in range(1, n + 1)]
queue = deque(_list)

result = []
for _ in range(len(_list)):
    queue.rotate(-(k - 1))  # - 가 맨앞 요소를 맨 뒤로 이동 시킴
    result.append(queue.popleft())

print('<', end='')
print(', '.join(map(str, result)), end='')
print('>')
