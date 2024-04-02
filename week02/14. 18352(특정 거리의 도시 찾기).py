# 난이도 (하) : BFS
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

def dijkstra(start):
    distance[start] = 0

    _heap = []
    heapq.heappush(_heap, (0, start))
    while _heap:
        dist, now = heapq.heappop(_heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(_heap, (cost, i[0]))

INF = int(1e9)

n, m, k, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

distance = [INF] * (n + 1)

dijkstra(start)

find = False
for i in range(1, n + 1):
    if k == distance[i]:
        print(i)
        find = True

if not find:
    print(-1)
