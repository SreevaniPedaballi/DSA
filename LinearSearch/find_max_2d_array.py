def find_max(arr):
    if not arr:
        return -1
    max=arr[0][0]
    for row in range (len(arr)):
        for col in range(len(arr[row])):
            max= arr[row][col] if arr[row][col] > max else max
    return max
arr=arr=[
    [1,22,313],
    [1,20,32,14],
    [17,25,13,4]
]
ans=find_max(arr)
print(ans)