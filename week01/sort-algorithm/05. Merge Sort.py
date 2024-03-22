# 요소를 쪼갠 후, 다시 합병시키면서 정렬해나가는 방식으로, 쪼개는 방식이 퀵정렬과 유사
# 시간복잡도 : 평균 O(nlog n) / 최선 O(nlog n) / 최악 O(nlog n)

# 간결한 코드
def merge_sort_simple(_arr):
    if len(_arr) < 2:
        return _arr

    mid = len(_arr) // 2
    low_arr = merge_sort_simple(_arr[:mid])
    high_arr = merge_sort_simple(_arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

def merge_sort(_arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, high

        while l < mid and h < high:
            if _arr[l] < _arr[h]:
                temp.append(_arr[l])
                l += 1
            else:
                temp.append(_arr[h])
                h += 1

        while l < mid:
            temp.append(_arr[l])
            l += 1
        while h < high:
            temp.append(_arr[h])
            h += 1

        for i in range(low, high):
            _arr[i] = temp[i - low]

    return sort(0, len(_arr))
