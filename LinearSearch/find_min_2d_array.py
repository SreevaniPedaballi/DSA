
def find_min(arr):
    if not arr:
        return -1
    min=arr[0][0]
    for row in range (len(arr)):
        for col in range(len(arr[row])):
            min= arr[row][col] if arr[row][col] < min else min
    return min
arr=arr=[
    [-1,22,313],
    [1,-20,32,14],
    [17,25,13,4]
]
ans=find_min(arr)
print(ans)