def flooring(arr,target):
    if not arr:
        return -1
    s_idx=0
    e_idx=len(arr)-1

    while s_idx <= e_idx:
        mid=s_idx+(e_idx-s_idx)//2

        if mid== target:
            return mid
        elif target > arr[mid]:
            s_idx=mid+1
        elif target < arr[mid]:
            e_idx=mid-1

    return e_idx

arr=[10,12,16,18,29,30]
target=17
print(flooring(arr,target))