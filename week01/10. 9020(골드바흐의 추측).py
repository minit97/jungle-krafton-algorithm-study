t = int(input())

def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

for _ in range(t):
    num = int(input())
    a = num // 2
    b = num // 2
    for _ in range(num // 2):
        if is_prime_number(a) and is_prime_number(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1