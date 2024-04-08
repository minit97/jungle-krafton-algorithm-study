# 난이도 (중) : DP

import sys

def input():
    return sys.stdin.readline().rstrip()

s1 = input()
s2 = input()

# ============================ 568ms ============================
# graph = [[0] * (len(s1) + 1) for _ in range((len(s2) + 1))]
# for i in range(1, len(s2) + 1):
#     for j in range(1, len(s1) + 1):
#         if s1[j - 1] == s2[i - 1]:
#             graph[i][j] = graph[i - 1][j - 1] + 1
#         else:
#             graph[i][j] = max(graph[i][j - 1], graph[i - 1][j])
# print(graph[-1][-1])

# ============================ 216ms ============================
# 풀이 한번 보기
result = [0] * len(s1)
for i in range(len(s2)):
    x = s2[i]
    y = 0
    for j in range(len(s1)):
        if y < result[j]:
            y = result[j]
        elif x == s1[j]:
            result[j] = y + 1
print(max(result))
