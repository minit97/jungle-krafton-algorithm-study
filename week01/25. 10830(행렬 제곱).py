# 다시 풀기!
# 상 : 분할 정복

import sys
def input():
    return sys.stdin.readline().rstrip()

n, b = map(int, input().split())


# ===================== 시간 초과 =====================
# row_matrix = []
# col_matrix = [[0] * n for _ in range(n)]
# for i in range(n):
#     _temp = list(map(int, input().split()))
#     row_matrix.append(_temp)
#     for j in range(len(_temp)):
#         col_matrix[j][i] = _temp[j]
#
# if b != 0:
#     for _ in range(b - 1):
#         temp_matrix = [[0] * n for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 temp_matrix[i][j] = sum([x * y for x, y in zip(row_matrix[i], col_matrix[j])]) % 1000
#         row_matrix = temp_matrix
#
# for i in row_matrix:
#     print(*i)

# ===================== 속도 개선 =====================
_matrix = [list(map(int, input().split())) for _ in range(n)]

def mul_matrix(matrix1, matrix2):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += matrix1[i][k] * matrix2[k][j] % 1000
    return res

def square(arr, square_cnt):
    if square_cnt == 1:
        return arr
    else:
        temp = square(arr, square_cnt // 2)
        if square_cnt % 2 == 0:
            return mul_matrix(temp, temp)
        else:
            return mul_matrix(mul_matrix(temp, temp), arr)

result = square(_matrix, b)
for i in range(n):
    for j in range(n):
        result[i][j] %= 1000

for i in result:
    print(*i)