# 다시 풀기!
# 상 : 우선순위 큐 + 완탐?
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

location_list = []
for _ in range(n):
    h, o = map(int, input().split())
    location_list.append((min(h, o), max(h, o)))
location_list.sort(key=lambda x: (x[1], x[0]))

railway_len = int(input())

heap = []
max_cnt = 0

for location in location_list:  # 모든 선을 하나씩 다 비교하는 거잖아
    start, end = location
    heapq.heappush(heap, start)
    line_start = end - railway_len
    while heap and heap[0] < line_start:
        heapq.heappop(heap)
    max_cnt = max(max_cnt, len(heap))
print(max_cnt)

