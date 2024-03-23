# 각 숫자가 몇 번 등장했는지 count하고 정렬한다.
# 시간복잡도 : O(n + k)

def counting_sort(arr):
    max_value = max(arr)  # 입력 배열에서 가장 큰 값 찾기
    min_value = min(arr)  # 입력 배열에서 가장 작은 값 찾기

    # 카운트 배열 초기화
    count = [0] * (max_value - min_value + 1)

    # 각 요소의 등장 횟수 카운트
    for num in arr:
        count[num - min_value] += 1
    # 누적 합산 - 이전 요소가 몇 개 있나
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # 정렬된 배열을 담을 임시 배열 초기화
    sorted_arr = [0] * len(arr)

    # 입력 배열을 순회하며 정렬된 위치에 요소 삽입
    for num in reversed(arr):
        sorted_arr[count[num - min_value] - 1] = num
        count[num - min_value] -= 1 # 그 전 요소로 가야함

    return sorted_arr

# 예시
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("정렬된 배열:", sorted_arr)
