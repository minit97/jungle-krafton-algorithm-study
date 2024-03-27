import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_square = [list(map(int, input().split())) for _ in range(n)]

white_cnt = 0
blue_cnt = 0

def one_color_square(x, y, size):
    global white_cnt, blue_cnt
    sum_value = 0

    for i in range(y, y + size):
        sum_value += sum(_square[i][x:x + size])

    if sum_value == 0:
        white_cnt += 1
    elif sum_value == size**2:
        blue_cnt += 1
    else:
        one_color_square(x, y, size//2)
        one_color_square(x, y + size//2, size//2)
        one_color_square(x + size//2, y, size//2)
        one_color_square(x + size//2, y + size//2, size//2)

one_color_square(0, 0, n)
print(white_cnt)
print(blue_cnt)


# ======================찾은 방식========================
result = []

def solution(x, y, N) :
    color = _square[x][y]
    for i in range(x, x + N) :
        for j in range(y, y + N) :
            if color != _square[i][j] :
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)


solution(0, 0, n)
print(result.count(0))
print(result.count(1))