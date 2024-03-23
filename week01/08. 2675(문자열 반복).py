t = int(input())

for _ in range(t):
    num, _str = input().split()
    result = ''
    for s in _str:
        result += s * int(num)
    print(result)