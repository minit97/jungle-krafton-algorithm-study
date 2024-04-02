# 난이도 (중) : DFS

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -1e9
min_val = 1e9

def dfs(depth, total, add, sub, mul, div):
    global max_val, min_val
    if depth == n:
        max_val = max(total, max_val)
        min_val = min(total, min_val)
        return
    if add:
        dfs(depth + 1, total + data[depth], add - 1, sub, mul, div)
    if sub:
        dfs(depth + 1, total - data[depth], add, sub - 1, mul, div)
    if mul:
        dfs(depth + 1, total * data[depth], add, sub, mul - 1, div)
    if div:
        dfs(depth + 1, int(total / data[depth]), add, sub, mul, div - 1)


dfs(1, data[0], add, sub, mul, div)
print(max_val)
print(min_val)