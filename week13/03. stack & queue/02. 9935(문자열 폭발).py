import sys

def input():
    return sys.stdin.readline().rstrip()

s = input()
bomb_s = input()
bomb_len = len(bomb_s)

stack = []
for i in s:
    stack.append(i)
    if ''.join(stack[-bomb_len:]) == bomb_s:
        for _ in range(bomb_len):
            stack.pop()

print("FRULA" if len(stack) == 0 else ''.join(stack))


# 메모리 초과 (재귀)
def solve(s):
    if bomb_s in s:
        new_s = s.replace(bomb_s, "")
        return solve(new_s)
    else:
        return s

result = solve(s)
print("FRULA" if len(result) == 0 else result)