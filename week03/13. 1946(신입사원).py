# 난이도 (중) : 그리디

import sys

def input():
    return sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())

    candidate = []
    for _ in range(n):
        document, interview = map(int, input().split())
        candidate.append((document, interview))
    candidate.sort()

    print(candidate)
    result = 1
    max_interview = candidate[0][1]
    for i in range(1, len(candidate)):
        if max_interview > candidate[i][1]:
            result += 1
            max_interview = candidate[i][1]

    print(result)