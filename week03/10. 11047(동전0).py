# 난이도 (하) : 그리디
import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True)

result = 0
for i in coin:
    result += k // i
    k %= i
print(result)