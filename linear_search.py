def linear_search(arr, target):
    for index, i in enumerate(arr):
        if i == target:
            print(f"Found target! (on index: {index})")
            return
    print("Target not in array")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 3
    linear_search(arr, target)

    target = "3"
    linear_search(arr, target)
