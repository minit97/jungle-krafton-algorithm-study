import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
num_list = list(input())

result = 0
for i in num_list:
    result += int(i)

print(result)