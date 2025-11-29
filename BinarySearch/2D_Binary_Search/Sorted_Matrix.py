"""
Here the given input matrix is sorted 
so first we are taking the 1st row and last column 
r=0
c=len(arr[r])-1
if arr[r][c]==target:
    return [r,c]
elif arr[r][c] < target:
    r +=1
    c=len(arr[r])-1
elif arr[r][c]> target:
    c-=1

"""

def search(arr, target):
    if not arr:
        return [-1,-1]
    r=0
    c=len(arr[r])-1

    while r<len(arr) and c>=0:
        if arr[r][c]==target:
            return [r,c]
        elif arr[r][c] < target:
            r +=1
            c=len(arr[r])-1 if r < len(arr) else 0
        elif arr[r][c] > target:
            c-=1
    return [-1,-1]

arr=[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
]

target=17
print(search(arr,target))
