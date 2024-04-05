# 난이도 (하) : 그리디

import sys

def input():
    return sys.stdin.readline().rstrip()

sub_split = input().split("-")

result = sum(list(map(int, sub_split[0].split('+'))))
for i in range(1, len(sub_split)):
    result -= sum(list(map(int, sub_split[i].split('+'))))
print(result)

# =============================================
# minus_s = input().split('-')
#
# temp_list = [sum(list(map(int, i.split('+')))) for i in minus_s]
# result = temp_list[0]
# for i in range(1, len(temp_list)):
#     result -= temp_list[i]
# print(result)