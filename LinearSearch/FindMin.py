def find_min(arr):
    if not arr:
        return 0
    min=arr[0]
    for idx in range(len(arr)):
        if  arr[idx]<min:
            min=arr[idx]
    return min

arr=[10,23,9,7,8]
ans=find_min(arr)
print(ans)