# 기수 정렬 : 데이터를 구성하는 기본 요소 (Radix)를 이용하여 정렬을 진행하는 방식
# 시간복잡도 : O(d * (n + b))
# d: 정렬할 숫자의 자릿수, b는 10

# 핵심 설명
# 1. 가장 낮은 자릿수부터 시작하여 가장 높은 자릿수까지 순차적으로 정렬을 수행한다.
# 2. 각 자릿수에 대해 안정적인 정렬 알고리즘(예: 카운팅 정렬)을 사용하여 정렬한다.
# 3. 모든 자릿수에 대한 정렬이 완료되면, 전체 데이터가 정렬된다.

def counting_sort(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)