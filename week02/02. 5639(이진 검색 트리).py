# 난이도 (하) : 그래프 탐색 기본


# 전위 : 루트 - 왼쪽 - 오른쪽
# 후위 : 왼쪽 - 오른쪽 - 루트
# ============================== 2156ms ==============================
import sys
sys.setrecursionlimit(10 ** 9)
def input():
    return sys.stdin.readline().rstrip()

node_list = []
while True:
    try:
        node_list.append(int(input()))
    except:
        break

def solution(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if node_list[i] > node_list[start]:
            mid = i
            break
    solution(start + 1, mid - 1)   # 왼쪽 트리
    solution(mid, end)             # 오른쪽 트리
    print(node_list[start])
solution(0, len(node_list) - 1)

# =============================== 84ms ===============================
from collections import defaultdict

def postorder(root):
    n = len(tree[root])
    if n == 2:
        postorder(tree[root][0])    # 왼쪽 노드
        postorder(tree[root][1])    # 오른쪽 노드
    elif n == 1:
        postorder(tree[root][0])    # 왼쪽 노드
    print(root)

stack = []
tree = defaultdict(list)

root_node = int(input())
stack.append(root_node)

# 트리 생성
while True:
    try:
        v = int(input())
        if v < stack[-1]:
            tree[stack[-1]].append(v)
            stack.append(v)
        else:
            xx = stack.pop()
            while stack and stack[-1] < v:
                xx = stack.pop()
            tree[xx].append(v)
            stack.append(v)
    except:
        break
postorder(root_node)
