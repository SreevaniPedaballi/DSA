def find_pivot(arr):
    s=0
    e=len(arr)-1
    while s <e:
        m=s+(e-s)//2
        if arr[m]> arr[m+1]:
            return m
        elif arr[m]<arr[m-1]:
            return m-1
        elif arr[s]==arr[m] and arr[e]==arr[m]:
            if arr[s]>arr[s+1]:
                return s
            s +=1
            if arr[e]>arr[e-1]:
                return e
            e -=1
        elif arr[s]<arr[m] or (arr[s]==arr[m] and arr[m]>arr[e]):
           s=m+1
        else:
            e=m-1
    return -1


    

def binary_search(arr,target,s,e):
    while s <=e:
        m=s+(e-s)//2
        if arr[m]==target:
            return m
        elif target > arr[m]:
            s=m+1
        else:
            e=m-1
    return -1
     

def find_duplicate_rotated_binary_search(arr,target):
    if not arr:
        return -1
    pivot=find_pivot(arr)
    if target>=arr[0]:
        return binary_search(arr,target,0,pivot)
    else:
        return binary_search(arr,target,pivot+1,len(arr)-1)

arr=[3,4,5,6,1,2,3]
print(arr)
target=2
print(f"target:{target}")
print(find_duplicate_rotated_binary_search(arr,target))