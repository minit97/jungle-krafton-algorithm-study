n = int(input())
temp = []

def dfs():
    if len(temp) == n:
        print(*temp)
        return
    for i in range(1, n + 1):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()

dfs()


# permutations
from itertools import permutations

n = int(input())
_list = [i for i in range(1, n + 1)]
_per = permutations(_list, n)

temp = list(_per)
for i in temp:
    for j in i:
        print(j, end=' ')
    print()