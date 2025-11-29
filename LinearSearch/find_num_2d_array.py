def find_num(arr,target):
    if not arr:
        return -1
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == target:
                return [row,col]
    return -1

# arr=list(map(int,input("Please enter listof numbers:").split(" ")))
# target=int(input("Please enter target:"))
arr=arr=[
    [1,22,313],
    [1,20,32,14],
    [17,25,13,4]
]
target=13
ans=find_num(arr,target)
print(ans)