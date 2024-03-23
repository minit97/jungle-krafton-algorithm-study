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
    low = high = 0
    while low < len(low_arr) and high < len(high_arr):
        if low_arr[low] < high_arr[high]:
            merged_arr.append(low_arr[low])
            low += 1
        else:
            merged_arr.append(high_arr[high])
            high += 1
    # 한쪽에서 다 빠질 경우의 수 고려

    merged_arr += low_arr[low:]
    merged_arr += high_arr[high:]
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
        temp_low, temp_high = low, high

        while temp_low < mid and temp_high < high:
            if _arr[temp_low] < _arr[temp_high]:
                temp.append(_arr[temp_low])
                temp_low += 1
            else:
                temp.append(_arr[temp_high])
                temp_high += 1

        while temp_low < mid:
            temp.append(_arr[temp_low])
            temp_low += 1
        while temp_high < high:
            temp.append(_arr[temp_high])
            temp_high += 1

        for i in range(low, high):
            _arr[i] = temp[i - low]

    return sort(0, len(_arr))
