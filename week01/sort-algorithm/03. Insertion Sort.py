# 2번째 원소부터 시작하여 그 앞(왼쪽)의 원소들과 비교하여 삽입할 위치를 지장한 후, 원소를 뒤로 옮기고 지정된 자리에 자료를 삽입
# 시간복잡도 : 최선 O(n) / 최악 O(n^2)

def insertion_sort(_arr):
    for end in range(1, len(_arr)):
        for i in range(end, 0, -1):
            if _arr[i - 1] > _arr[i]:
                _arr[i - 1], _arr[i] = _arr[i], _arr[i - 1]