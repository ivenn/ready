def merge(arr, l, m, r):

    big_int = 100

    size_l = m - l + 1
    size_r = r - m

    larr = [0] * size_l
    rarr = [0] * size_r

    for i in range(size_l):
        larr[i] = arr[l + i]
    for j in range(size_r):
        rarr[j] = arr[m + j + 1]

    larr.append(big_int)
    rarr.append(big_int)

    i = 0
    j = 0

    for k in range(l, r + 1):
        if larr[i] <= rarr[j]:
            arr[k] = larr[i]
            i += 1
        else:
            arr[k] = rarr[j]
            j += 1


def merge_sort(arr, l, r):

    if l < r:
        m = (l + r) / 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def main():
    arr = [6, 0, 5, 1, 8, 2, 9, 4, 3, 7]
    print(arr)
    merge_sort(arr, 0, 9)
    print(arr)


if __name__ == '__main__':
    main()
