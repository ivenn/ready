def max_heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, n, largest)


def heap_sort(arr, n):
    n = len(arr)
    
    # build max heap
    for i in range(n, -1, -1):
        max_heapify(arr, n, i)

    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


def main():
    #  arr = list(range(10))
    #  random.shuffle(arr)
    arr = [6, 0, 5, 1, 8, 2, 9, 4, 3, 7]
    print(arr)
    heap_sort(arr, 9)
    print(arr)


if __name__ == '__main__':
    main()
