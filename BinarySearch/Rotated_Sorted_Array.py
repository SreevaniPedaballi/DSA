
def find_pivot(arr):
    s=0
    e=len(arr)-1

    while s < e:
        m=s+(e-s)//2

        if(arr[m]>arr[m+1]):
            return m
        elif(arr[m]<arr[m-1]):
            return m-1
        elif(arr[s]>=arr[m]):
            e=m-1
        else:
            s=m+1
    return -1
def binary_search(arr,target,s,e):
    # s=0
    # e=len(arr)-1

    while s <= e:
        m=s+(e-s)//2
        if arr[m]==target:
            return m
        elif target<arr[m]:
            e=m-1
        else:
            s=m+1
    return -1
def find_in_rotated_binary_search(arr,target):
    if not arr:
        return -1
    pivot=find_pivot(arr)
    
    if(arr[pivot]==target):
        return pivot
    elif(target>=arr[0]):
        return binary_search(arr,target,0,pivot)
    else:
        return binary_search(arr,target,pivot+1,len(arr)-1)

arr=[5,7,10,11,2,3,4]
target=5
print(find_in_rotated_binary_search(arr,target))


