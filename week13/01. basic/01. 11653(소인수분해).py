import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

divided_list = [i for i in range(2, int(n ** 0.5) + 1)]

for i in divided_list:
    while(n % i == 0):
        n //= i
        print(i)

if (n != 1):
    print(n)