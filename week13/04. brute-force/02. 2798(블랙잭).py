import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
card_list = list(map(int, input().split()))

result = 0
for cards in combinations(card_list, 3):
    temp_sum = sum(cards)
    if temp_sum <= m:
        result = max(result, temp_sum)
print(result)