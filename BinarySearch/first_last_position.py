def Find_First_Last_Positions(arr,target):
    ans=[-1,-1]
    if not arr:
        return ans
    ans[0]=search(arr,target,True)
    if arr[0] != -1:
        ans[1]=search(arr,target,False)
    return ans
    
def search(arr,target,findFirstIndex=True):
    ans=-1
    s_idx=0
    e_idx=len(arr)-1

    while s_idx <= e_idx:
        mid=s_idx+(e_idx-s_idx)//2

        if target > arr[mid]:
            s_idx=mid+1
        elif target < arr[mid]:
            e_idx=mid-1
        else:
            ans=mid
            if findFirstIndex:
                e_idx=mid-1
            else:
                s_idx=mid+1
    return ans

arr=[1,2,3,4,4,4,4,5,6,7]
print(arr)
target=4
print(Find_First_Last_Positions(arr,target))