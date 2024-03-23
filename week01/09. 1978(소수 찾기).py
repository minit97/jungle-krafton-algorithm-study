
def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
_list = list(map(int, input().split()))

result = 0
for i in _list:
    if is_prime_number(i):
        result += 1
print(result)
