def binary_search(arr,target,s,e):
    if s>e:
        return -1
    m=s+(e-s)//2
    if arr[m]==target:
        return m
    if(target>arr[m]):
     return binary_search(arr,target,m+1,e)
    return binary_search(arr,target,s,m-1)
    
arr=[1,3,5,7,10,12,13,15]
target=13
ans=binary_search(arr,target,0,len(arr)-1)
print(ans)