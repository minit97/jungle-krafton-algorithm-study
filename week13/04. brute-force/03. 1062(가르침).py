import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
visited = [False for _ in range(26)]
words = [input().rstrip() for _ in range(n)]

result = 0

def check():
    cnt = 0
    for word in words:
        flag = True
        for s in word:
            if not visited[ord(s) - ord('a')]:
                flag = False
                break
        if flag:
            cnt += 1
    return cnt

def dfs(start, alpha_cnt):
    global result

    if alpha_cnt == k:
        result = max(result, check())
        return

    for i in range(start, 26):
        if not visited[i]:
            visited[i] = True
            dfs(i, alpha_cnt + 1)
            visited[i] = False

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    for c in ('a', 'c', 'i', 'n', 't'):
        visited[ord(c) - ord('a')] = True
    dfs(0, 5)
    print(result)