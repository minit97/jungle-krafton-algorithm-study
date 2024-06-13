n = int(input())

result = 0
for i in range(1, n + 1):
    if i // 100 > 0:
        if (i // 100 - i % 100 // 10) == (i % 100 // 10 - i % 10):
            result += 1
    else:
        result += 1
print(result)