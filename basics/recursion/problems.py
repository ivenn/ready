def reverse_string_recursively(s):

    def reverse(arr, i, j):
        if i > j:
            return
        arr[i], arr[j] = arr[j], arr[i]
        return reverse(arr, i + 1, j - 1)

    return reverse(s, 0, len(s) - 1)


def reverse_string_iter(s):
    i, j = 0, len(s)-1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

    return s


def get_pascal_triangle_row(k):
    """
    Input: 3
    Output: [1,3,3,1]
    """
    row = [1]
    while k:
        new_row = [1] * (len(row) + 1)
        i = 1
        while i < len(new_row)/2:
            new_row[i] = new_row[-i-1] = row[i-1] + row[i]
            i += 1
        row = new_row
        k -= 1

    return row

print(get_pascal_triangle_row(1))



