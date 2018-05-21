def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1

    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]

    return i + 1


def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)

        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)


def test():
    import random

    arr = list(range(10))
    random.shuffle(arr)
    arr = [7, 3, 9, 2, 0, 1, 4, 8, 5, 6]
    print(arr)
    quicksort(arr, 0, len(arr) - 1)
    print(arr)


test()
