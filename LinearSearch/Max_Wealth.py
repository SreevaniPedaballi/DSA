def max_wealth(arr):
    if not arr:
        return -1
    max=-1
    for person in range(len(arr)):
        count=0
        for account in range(len(arr[person])):
            count += arr[person][account]
        max= count if count > max else max
    return max

"""Hear each row is a person accounts and elements/columns are their account balances.
so we need to find which person has max amount than others"""
arr=[
    [1,2,3],
    [1,2,3,1],
    [1,2,3,4]
]

ans=max_wealth(arr)
print(ans)