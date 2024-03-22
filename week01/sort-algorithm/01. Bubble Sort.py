# 서로 인접한 두 원소의 대소를 비교하고, 조건에 맞지 않다면 자리를 교환하며 정렬하는 알고리즘
# 시간복잡도 : 평균 / 최선 / 최악 O(n^2)

def bubble_sort(_arr):
    for i in range(len(_arr)):
        for j in range(1, len(_arr) - 1):
            if _arr[j - 1] > _arr[j]:
                _arr[j - 1], _arr[j] = _arr[j], _arr[j - 1]
    return _arr

