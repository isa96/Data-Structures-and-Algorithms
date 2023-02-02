def insertion_sort(arr):
    for i in range(1, len(arr)):
        pivot = arr[i]

        for j in range(i-1,-1,-1):
            if arr[j] <= pivot:
                break
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = pivot

    return arr


if __name__ == "__main__":
    from time_counter import timeit

    arr = [3, 2, 5, 4, 3, 12, 32, -2, 34, -54, 22]
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)

    timeit(insertion_sort)
