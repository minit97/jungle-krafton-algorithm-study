# 다시
# counting sort
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

count = [0] * 10001
for _ in range(n):
    num = int(input())
    count[num] += 1

for i in range(len(count)):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)