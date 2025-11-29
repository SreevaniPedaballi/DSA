def find_max(arr):
    if not arr:
        return -1
    arr_len=len(arr)
    max=arr[0]
    for idx in range(arr_len):
        if arr[idx] > max:
            max=arr[idx]
    return max

arr=[10,22,34,21,403,12,216]
ans=find_max(arr)
print(ans)