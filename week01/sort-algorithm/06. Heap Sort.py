# 완전 이진 트리를 기본으로 하는 힙(Heap) 자료구조를 기반으로한 정렬 방식
# 시간복잡도 : 평균 O(nlog n) / 최선 O(nlog n) / 최악

def heapify(unsorted, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and unsorted[right] > unsorted[largest]:
        largest = left
    if right < heap_size and unsorted[right] > unsorted[largest]:
        largest = right

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
    n = len(unsorted)

    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)

    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)

    return unsorted