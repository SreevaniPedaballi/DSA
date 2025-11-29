def BinarySearch(arr,target):
    if not arr:
        return -1
    s_idx=0
    e_idx=len(arr)-1
    while s_idx<=e_idx:
        middle= s_idx+(e_idx-s_idx)//2

        if arr[middle] == target:
            return middle
        elif target < arr[middle]:
            e_idx=middle-1
        elif target > arr[middle]:
            s_idx=middle+1
    return -1

        
arr=[1,12,13,34,45,56]
target=12
ans=BinarySearch(arr,target)
print(ans)