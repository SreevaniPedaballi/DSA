def find_pivot_in_duplicate_arr(arr):
    s=0
    e=len(arr)-1
    while s < e:
        m=s+(e-s)//2
        if arr[m] >arr[m+1]:
            return m
        elif arr[m]<arr[m-1]:
            return m-1
        elif (arr[s]<arr[m] or (arr[m]==arr[s] and arr[m]>arr[e])):
            s=m+1
        else:
            e=m-1
    return -1

def find_pivot(arr):
    s=0
    e=len(arr)-1
    while s <e:
        m=s+(e-s)//2
        if arr[m] > arr[m+1]:
            return m
        if arr[m] < arr[m-1]:
            return m-1
        if arr[s]>=arr[m]:
            e=m-1
        else:
            s=m+1
    return -1
def find_rotations(arr,hasDuplicates=False):
    if not arr:
        return 0
    if hasDuplicates:
        pivot=find_pivot_in_duplicate_arr(arr)
    else:
        pivot=find_pivot(arr)
    return len(arr[0:pivot+1])

arr=[3,4,5,6,1,2,3]
print(arr)
print(find_rotations(arr,True))

arr=[4,5,6,7,8,1,2,3]
print(arr)
print(find_rotations(arr,False))