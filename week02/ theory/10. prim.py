# 프림은 다익스트라와 매우 유사하다.

import heapq

def prim(graph, start, visited):
    visited[start] = True

    min_heap = []
    for next_node, weight in graph[start]:
        min_heap.append((weight, next_node))

    heapq.heapify(min_heap)
    result = 0
    while min_heap:
        weight, to_node = heapq.heappop(min_heap)
        if not visited[to_node]:
            visited[to_node] = True
            result += weight
            for next_node, next_weight in graph[to_node]:
                if not visited[next_node]:
                    heapq.heappush(min_heap, (next_weight, next_node))

    return result



# 예시 그래프
graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('C', 1), ('D', 2)],
    'C': [('A', 3), ('B', 1), ('D', 4), ('E', 6)],
    'D': [('B', 2), ('C', 4), ('E', 7)],
    'E': [('C', 6), ('D', 7)]
}
# n은 노드의 갯수
n = int(input())
visited = [False] * (n + 1)
start = 0

result = prim(start, visited)
print("Minimum Spanning Tree:", result)
