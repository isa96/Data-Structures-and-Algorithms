def bubble_sort(arr):
    for i in range(len(arr)):
        n_swaps = 0
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                n_swaps += 1
        if n_swaps == 0:
            return arr
    return arr


if __name__ == "__main__":
    from time_counter import timeit

    arr = [3, 2, 5, 4, 3, 12, 32, -2, 34, -54, 22]
    sorted_arr = bubble_sort(arr)
    print(sorted_arr)

    timeit(bubble_sort)
