import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    s = input()

    temp = 0
    result = 0
    for i in s:
        if i == 'O':
            temp += 1
            result += temp
        else:
            temp = 0
    print(result)