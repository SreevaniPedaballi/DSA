def Agnostic_BinarySearch(arr,target):
    if not arr:
        return -1
    
    isAsc= arr[0] < arr[len(arr)-1]

    s_idx=0
    e_idx=len(arr)-1
    while s_idx <= e_idx:
        middle=s_idx+(e_idx-s_idx)//2
        if arr[middle]==target:
            return middle
        
        if isAsc:
            if target < arr[middle]:
                e_idx=middle-1
            else:
                s_idx=middle+1
        else:
            if target > arr[middle]:
                e_idx=middle-1
            else:
                s_idx=middle+1
    return -1

arr=[55,43,41,35,13,7,3]
target=7
print(Agnostic_BinarySearch(arr,target))

arr=[1,12,13,34,45,56]
target=45
print(Agnostic_BinarySearch(arr,target))