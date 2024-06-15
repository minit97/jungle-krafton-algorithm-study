import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
m_list = list(map(int, input().split()))

result = n_list + m_list
result.sort()
print(' '.join(map(str, result)))