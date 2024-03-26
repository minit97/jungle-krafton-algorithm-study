# 다시 풀기!
# 중 : 우선순위 큐

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())


# ============ 시간 초과 ============
_list = []
for _ in range(n):
    num = int(input())
    _list.append(num)

    _list.sort()
    if len(_list) % 2 == 1: # 중간값
        print(_list[len(_list) // 2])
    else:   # 중간에 있는 수들 중 작은 수
        middle1 = _list[(len(_list) - 1) // 2]
        middle2 = _list[len(_list) // 2]
        print(min(middle1, middle2))

# ============ 힙 사용 ============        # 정렬을 힙이 대신해준다.
import heapq

left_heap = []      #최대힙
right_heap = []     #최소힙
for _ in range(n):
    num = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    if right_heap and right_heap[0] < -left_heap[0]:    # left의 첫번째 값이 중앙값이 된다.
        left_value = heapq.heappop(left_heap)
        right_value = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -right_value)
        heapq.heappush(right_heap, -left_value)

    print(-left_heap[0])