def rotated_binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = start + (end - start) // 2

    if arr[mid] == target:
        return mid

    # Case 1: Left half is sorted
    if arr[start] <= arr[mid]:
        if arr[start] <= target <= arr[mid]:
            return rotated_binary_search(arr, target, start, mid - 1)
        else:
            return rotated_binary_search(arr, target, mid + 1, end)

    # Case 2: Right half is sorted
    else:
        if arr[mid] <= target <= arr[end]:
            return rotated_binary_search(arr, target, mid + 1, end)
        else:
            return rotated_binary_search(arr, target, start, mid - 1)
arr = [4,5,6,7,0,1,2]
target = 0

index = rotated_binary_search(arr, target, 0, len(arr)-1)
print(index)
