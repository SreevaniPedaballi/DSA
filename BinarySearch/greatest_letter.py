def  Greatest_Letter(arr,target):
    if not arr:
        return -1
    s_idx=0
    e_idx=len(arr)-1

    while s_idx <= e_idx:
        mid=s_idx+(e_idx-s_idx)//2
        if target > arr[mid]:
            s_idx=mid+1
        elif target <= arr[mid]:
            e_idx=mid-1
    # return  arr[e_idx] if e_idx >= 0 else -1
    return e_idx

arr=['c','e','g','j','p','s','u']
target='d'
print(Greatest_Letter(arr,target))