a, b, v = map(int, input().split())

result = (v - b) // (a - b)
if (v - b) % (a - b) != 0:
    result += 1
print(result)