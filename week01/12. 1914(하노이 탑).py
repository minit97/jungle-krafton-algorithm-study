
n = int(input())

def hanoi(cnt, start, end, sub):
    if cnt == 1:
        print(start, end)
        return
    hanoi(cnt - 1, start, sub, end)
    print(start, end)
    hanoi(cnt - 1, sub, end, start)

print(2 ** n - 1)
hanoi(n, 1, 3, 2)