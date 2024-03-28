n = int(input())

temp = n
result = 0
while True:
    result += 1
    right = temp // 10 + temp % 10
    temp = (temp % 10) * 10 + (right % 10)
    if temp == n:
        break
print(result)