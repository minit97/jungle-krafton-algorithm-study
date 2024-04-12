import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
# 강의 번호, 시작시간, 종료시
lecture = [tuple(map(int, input().split())) for _ in range(n)]
lecture.sort(key=lambda x: (x[1], x[2]))

heap = []
result = [0] * (n + 1)

room_num = 1
heapq.heappush(heap, (lecture[0][2], room_num))
result[lecture[0][0]] = room_num

for i in range(1, n):
    if heap[0][0] > lecture[i][1]:  # 끝나는 시간 > 시작 시간
        room_num += 1
        result[lecture[i][0]] = room_num
        heapq.heappush(heap, (lecture[i][2], room_num))
    else:
        temp = heapq.heappop(heap)
        result[lecture[i][0]] = temp[1]
        heapq.heappush(heap, (lecture[i][2], temp[1]))
print(len(heap))
for i in range(1, len(result)):
    print(result[i])