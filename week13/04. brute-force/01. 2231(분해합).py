n = int(input())

result = 0
for i in range(1, n):
    temp = sum(map(int, str(i))) + i
    if n == temp:
        result = i
        break

print(result)

# ====================================

n = int(input())

def split_sum(num):
    answer = num
    for i in range(len(str(num)) - 1, -1, -1):
        answer += num // 10**i
        num = num % 10**i
    return answer


result = 0
for i in range(n, 1, -1):
    if n == split_sum(i):
        result = i
print(result)