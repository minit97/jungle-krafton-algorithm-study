import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
graph = []
virus_location = []
for i in range(n):
    temp_list = list(map(int, input().split()))
    for j in range(len(temp_list)):
        if temp_list[j] > 0:
            heapq.heappush(virus_location, (temp_list[j], i, j))
    graph.append(temp_list)

s, x, y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def virus_bfs(graph, virus_location):
    temp_heap = []
    while virus_location:
        cost, x, y = heapq.heappop(virus_location)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = cost
                heapq.heappush(temp_heap, (cost, nx, ny))
    return temp_heap

temp_s = 0
while temp_s != s:
    temp_s += 1
    virus_location = virus_bfs(graph, virus_location)
print(graph[x - 1][y - 1])