# 재귀(분할 정복)
# 시간복잡도 : 평균 O(nlog n) / 최선 O(nlog n) / 최악 O(n^2)

def quick_sort(_arr):
    if len(_arr) <= 1:
        return _arr
    pivot = _arr[len(_arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in _arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)