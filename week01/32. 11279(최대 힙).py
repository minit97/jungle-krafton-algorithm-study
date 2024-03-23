import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

heap = []
for _ in range(t):
    n = int(input())
    if n == 0:
        print(-heapq.heappop(heap) if len(heap) > 0 else 0)
    else:
        heapq.heappush(heap, -n)