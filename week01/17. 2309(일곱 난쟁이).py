import sys
def input():
    return sys.stdin.readline().rstrip()

_data = []
for _ in range(9):
    _data.append(int(input()))
_data.sort()

sum_value = sum(_data)
for i in _data:
    roop_out = False
    for j in _data:
        if sum_value - i - j == 100 and i != j:
            _data.remove(i)
            _data.remove(j)
            roop_out = True
            break
    if roop_out:
        break

for result in _data:
    print(result)


# ==================================================
# 간단한 코드 - combinations 라이브러리 사용
import itertools

array = [int(input()) for _ in range(9)]

for i in itertools.combinations(array, 7):  # 해당 배열을 7명 중복없이 뽑아준다.
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break