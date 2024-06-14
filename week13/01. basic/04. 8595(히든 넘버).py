
n = int(input())
s = input()

result = 0
temp = ''
for i in s:
    if i.isalpha() and temp != '':
        result += int(temp)
        temp = ''
    elif i.isdigit():
        temp += i

# 끝에 숫자가 있을 경우에 더하기 해주기!
if temp != '':
    result += int(temp)
print(result)