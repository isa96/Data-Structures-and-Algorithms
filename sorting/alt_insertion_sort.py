def insertion_sort(arr):
    if len(arr) < 2:
        return arr
    
    new_arr = []

    for pivot in arr:
        i = 0
        for val in new_arr:
            if val >= pivot:
                break
            i += 1
        new_arr.insert(i, pivot)

    return new_arr


if __name__ == "__main__":
    from time_counter import timeit

    arr = [3, 2, 5, 4, 3, 12, 32, -2, 34, -54, 22]
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)

    timeit(insertion_sort)
