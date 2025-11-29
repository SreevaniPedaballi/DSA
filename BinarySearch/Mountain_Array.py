
def mountain_Array_search(arr):
    if not arr:
        return -1
    s=0
    e=len(arr)-1
    # when peak element is reached then index start and end both ate same/equal
    while s < e:
        m=s+(e-s)//2
        if arr[m] < arr[m+1]:
            s=m+1
        elif arr[m] > arr[m+1]:
            e=m #here m is > m+1 so m is also one of the possible answer so we are considering e=m

    return s

arr=[1,4,6,7,8,9,10,5]
print(arr)
print(mountain_Array_search(arr))