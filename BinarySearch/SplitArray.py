# https://leetcode.com/problems/split-array-largest-sum/description/
def Split_Array(arr,k):
    if not arr:
        return -1
    s=0
    e=0
    for ele in arr:
        e+=ele
        s=max(s,ele)

    while s <  e:
        mid=s+(e-s)//2
        sum=0
        pieces=1
        for num in arr:
            if sum+num > mid:
                sum=num
                pieces +=1
            else:
                sum +=num
        
        if pieces > k:
            s=mid+1
        else:
            e=mid
    return s # s==e so return either s or e

arr= [7,2,5,10,8]
k=2
print(Split_Array(arr,k))