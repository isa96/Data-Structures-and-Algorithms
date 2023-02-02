def quick_sort(arr):
    if len(arr) < 2:
        return arr

    left, pivot, right = [], [], []
    pivot.append(arr[0])

    for i in arr[1:]:
        if i > pivot[0]:
            right.append(i)
        elif i < pivot[0]:
            left.append(i)
        else:
            pivot.append(i)

    return quick_sort(left) + pivot + quick_sort(right)


if __name__ == "__main__":
    from time_counter import timeit

    arr = [3, 2, 5, 4, 3, 12, 32, -2, 34, -54, 22]
    sorted_arr = quick_sort(arr)
    print(sorted_arr)

    timeit(quick_sort)
