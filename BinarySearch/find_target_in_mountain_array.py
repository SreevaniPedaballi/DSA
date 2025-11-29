def binary_search(arr,target,isAsc=True):
    s=0
    e=len(arr)-1
    while s<=e:
        m=s+(e-s)//2
        if arr[m]==target:
            return m
        if isAsc:
            if target>arr[m]:
                s=m+1
            elif target < arr[m]:
                e=m-1
        else:
            if target>arr[m]:
                e=m-1
            elif target < arr[m]:
                s=m+1
        
    return -1


def find_peak_element(arr):
    s=0
    e=len(arr)-1
    while s < e:
        m=s+(e-s)//2
        if arr[m] > arr[m+1]:
            e=m
        elif arr[m] < arr[m+1]:
            s=m+1

    return s

arr=[1,6,7,8,9,10,5,4,3,2]
print(arr)
target=4

peak_element=find_peak_element(arr)+1

ans=binary_search(arr[0:peak_element],target) 
print(ans if ans !=-1 else binary_search(arr[peak_element:len(arr)],target,False)+peak_element)
