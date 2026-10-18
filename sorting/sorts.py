"""Sorting algorithms from the DSA unit.

Each function returns a new sorted list and leaves the input alone.
"""


def bubble_sort(items):
    arr = list(items)
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # already sorted, stop early
            break
    return arr


def selection_sort(items):
    arr = list(items)
    n = len(arr)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr


def insertion_sort(items):
    arr = list(items)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(items):
    arr = list(items)
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(items):
    arr = list(items)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    bigger = [x for x in arr if x > pivot]
    return quick_sort(smaller) + equal + quick_sort(bigger)


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("original :", data)
    for fn in (bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort):
        print(f"{fn.__name__:15}: {fn(data)}")
