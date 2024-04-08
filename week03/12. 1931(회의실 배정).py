# 난이도 (중) : 그리디 - 회의실 문제는 끝시간 기준으로 생각하자!

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
meeting = []
for _ in range(n):
    a, b = map(int, input().split())
    meeting.append((a, b))
meeting.sort(key=lambda x:(x[1], x[0]))

result = 1
end_time = meeting[0][1]
for i in range(1, len(meeting)):
    if meeting[i][0] >= end_time:   # 미팅 시작시간이 이전 미팅 끝시간보다 클 때
        result += 1
        end_time = meeting[i][1]
print(result)