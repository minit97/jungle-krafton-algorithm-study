# 난이도 (하) : 그래프 탐색 기본
# 최소 신장 트리 문제

import sys

def input():
    return sys.stdin.readline().rstrip()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a_val = find_parent(parent, a)
    b_val = find_parent(parent, b)
    if a_val < b_val:
        parent[b_val] = a_val
    else:
        parent[a_val] = b_val

v, e = map(int, input().split())

parent = [i for i in range(v + 1)]


edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)



