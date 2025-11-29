def find_num_in_range(arr,target,start,end):
    if not arr:
        return -1
    for idx in range(start,end):
        if arr[idx]==target:
            return idx
    return -1

arr=[10,22,64,56,34]
target=34
start=1
end=3
res=find_num_in_range(arr,target,start,end)
print(res)