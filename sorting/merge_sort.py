def merge_sort(arr):
    if len(arr) < 2:
        return arr

    left = arr[: len(arr) // 2]
    right = arr[len(arr) // 2 :]
    left = merge_sort(left)
    right = merge_sort(right)

    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res


if __name__ == "__main__":
    from time_counter import timeit

    arr = [3, 2, 5, 4, 3, 12, 32, -2, 34, -54, 22]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)

    timeit(merge_sort)
