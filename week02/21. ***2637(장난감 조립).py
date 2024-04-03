# 난이도 (중) : 위상정렬

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    indegree[x] += 1

result = [[0] * (n + 1) for _ in range(n + 1)]
def topology_sort():
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        for next, cost in graph[now]:
            # 기본 부품
            if result[now].count(0) == n + 1:
                result[next][now] += cost

            # 중간 부품
            else:
                for i in range(1, n + 1):
                    result[next][i] += result[now][i] * cost

            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)

topology_sort()

for index, value in enumerate(result[n]):
    if value > 0:
        print(index, value)

# 정답 관련 저장을 2차원 배열로 하는데 이 부분 좀 어려운듯
# ============================================================
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)


for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[X].append((Y, K))
    indegree[Y] += 1

result_list = [0] * (N + 1)
result_parts = []
for i in range(1, N + 1):
    if len(graph[i]) == 0:      # 진출 차수가 0이면 길이 0
        result_parts.append(i)
def topology_sort():
    q = deque()
    result = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)
        for next, cnt in graph[cur]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    return result

topology_list = topology_sort()

for i in topology_list:
    for idx, cnt in graph[i]:
        if result_list[i] == 0:
            result_list[idx] += cnt
        else:
            result_list[idx] += cnt * result_list[i]

for i in result_parts:
    print(i, result_list[i])