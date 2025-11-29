def find_number(arr,target):
    if not len(arr):
        return -1
    for idx in range(len(arr)):
        if arr[idx] == target:
            return idx
    return -1
        


arr=[10,23,45,67,11,24]
target=110
ans=find_number(arr,target)
print(ans)