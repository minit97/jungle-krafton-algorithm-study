# 다시 풀기!
# 중 : 분할 정복
import sys
def input():
    return sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())
# ================ 시간 초과 ================
print(a**b % c)

# ================  ================
# 나머지 연산의 분배법칙 : (A X B) % N = ((A % N) X (B % N)) % N

def solution(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (solution(a, b // 2, c) ** 2) % c
    else:
        return ((solution(a, b // 2, c) ** 2) * a) % c

print(solution(a, b, c))