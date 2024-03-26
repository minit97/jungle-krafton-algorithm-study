# 백트래킹의 대표적인 문제
# 어렵다 여러 번 적어보고 다시 생각해보는 과정이 필요하다!!

n = int(input())

result = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        # 1. 같은 열에 다른 퀸이 있는 경우 : row라는 배열 안에 같은 값이 있는지 없는지를 확인하면 된다.
        # 2. 왼쪽 대각선, 오른쪽 대각선에 다른 퀸이 있는 경우
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global result
    if x == n:
        result += 1
        return
    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)

n_queens(0)
print(result)
