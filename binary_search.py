def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        # print(low, high, mid, arr[mid])
        if arr[mid] == target:
            print(f"Found target! (on index: {mid})")
            return
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    print("Target not in array")


def binary_search_recursive(arr, target):

    def _binary_search_recursive(arr, target):

        low = 0
        high = len(arr) - 1
        mid = low + (high - low) // 2
        # print(low, high, mid, arr)

        if (high == 0 and arr[0] != target) or len(arr) < 1:
            print("Target not in array")
            return

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return _binary_search_recursive(arr[:mid], target)
        else:
            temp = _binary_search_recursive(arr[mid + 1 :], target)
            if temp is None:
                return
            return mid + 1 + temp

    res = _binary_search_recursive(arr, target)
    if res:
        print(f"Found target! (on index: {res})")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 3
    binary_search(arr, target)

    target = -1
    binary_search(arr, target)

    target = 100
    binary_search(arr, target)

    target = 3
    binary_search_recursive(arr, target)

    target = -1
    binary_search_recursive(arr, target)

    target = 100
    binary_search_recursive(arr, target)

    target = 7
    binary_search_recursive(arr, target)

    target = 1
    binary_search_recursive(arr, target)

    target = 1
    binary_search_recursive([], target)
