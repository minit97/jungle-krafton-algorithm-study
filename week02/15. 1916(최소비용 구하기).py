# 난이도 (중) : BFS

import sys
import heapq

INF = int(1e9)
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

distance = [INF] * (n + 1)
def dijktra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
dijktra(start)
print(distance[end])