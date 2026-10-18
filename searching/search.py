"""Linear and binary search.

Both return the index of the target, or -1 if it isn't there.
Binary search needs the list to be sorted first.
"""


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    return binary_search_recursive(arr, target, low, mid - 1)


if __name__ == "__main__":
    nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("linear search for 23:", linear_search(nums, 23))
    print("binary search for 23:", binary_search(nums, 23))
    print("binary search for 7 :", binary_search(nums, 7))
