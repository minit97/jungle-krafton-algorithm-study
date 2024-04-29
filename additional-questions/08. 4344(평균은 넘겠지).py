import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    _list = list(map(int, input().split()))
    student = _list[0]
    score = _list[1:]

    avg = sum(score) // student
    result = 0
    for s in score:
        if s > avg:
            result += 1
    print("{:.3f}%".format((result / student) * 100))
