
"""
Here Matrix have rows and columns sorted.
so logic to find target element is as follows,
forst take lower bound and upper bound
lower bound=each row 1st element
upper bound=each row last element

match target with last element 
if last element == target
return
elif last element < target
skip that current row and move to next row
else
skip current column and go to before column


"""
def search(arr,target):
    if not arr:
        return [-1,-1]
    r=0
    c=len(arr[0])-1

    while r< len(arr) and c >=0:
        if arr[r][c] == target:
            return [r,c]
        elif arr[r][c] < target:
            r+=1
            c=len(arr[r])-1 if r < len(arr) else 0
        else:
            c-=1
    return [-1,-1]

arr=[
    [1,2,13],
    [12,15,26],
    [17,28,39]
]
target=15
print(search(arr,target))