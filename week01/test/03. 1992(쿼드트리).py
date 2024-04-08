import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
data = [list(map(int, input())) for _ in range(n)]

result = ''
def one_color_check(x, y, size):
    global result

    sum_value = 0
    for i in range(y, y + size):
        sum_value += sum(data[i][x : x + size])

    if sum_value == 0:
        result += '0'
    elif sum_value == size**2:
        result += '1'
    else:
        result += '('
        one_color_check(x, y, size//2)
        one_color_check(x + size//2, y, size//2)
        one_color_check(x, y + size//2, size//2)
        one_color_check(x + size//2, y + size//2, size//2)
        result += ')'

one_color_check(0, 0, n)
print(result)