# 해당 순서에 원소를 넣을 위치는 이미 정해져 있고, 어떤 원소를 넣을지 선택하는 알고리즘이다.
# 시간복잡도 : O(n^2)

def selection_sort(_arr):
    for i in range(len(_arr) - 1):
        min_idx = i
        for j in range(i + 1, len(_arr)):
            if _arr[j] < _arr[min_idx]:
                min_idx = j
        _arr[i], _arr[min_idx] = _arr[min_idx], _arr[i]
    return _arr