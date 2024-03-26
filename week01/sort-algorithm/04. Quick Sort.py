# 재귀(분할 정복)
# 시간복잡도 : 평균 O(nlog n) / 최선 O(nlog n) / 최악 O(n^2)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

# ============================================================
# ============Do it! 자료구조와 함께 배우는 알고리즘 입문===============
def qsort(arr, start, end):
    pl = start
    pr = end

    pivot = arr[(start + end) // 2]

    while pl <= pr:
        while arr[pl] < pivot:
            pl += 1     # 1
        while arr[pr] > pivot:
            pr -= 1     # 6
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1

    if start < pr:
        qsort(arr, start, pr)
    if pl < end:
        qsort(arr, pl, end)

ex_data = [5, 8, 4, 2, 6, 1, 3, 9, 7]
qsort(ex_data, 0, len(ex_data) - 1)

# ============================================================
# =======================Algorithm 책==========================
def quick_sort2(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort2(arr, p, q - 1)
        quick_sort2(arr, q + 1, r)

def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r - 1):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1