# https://leetcode.com/problems/missing-number/description/ 
def sort(arr):
    idx=0
    while idx < len(arr):
        correct_idx=arr[idx]
        if  correct_idx < len(arr) and arr[idx] != arr[correct_idx]:
            temp=arr[idx]
            arr[idx]=arr[correct_idx]
            arr[correct_idx]=temp
        else:
            idx +=1
    return arr

def find_missing_Number(arr):
    s_arr=sort(arr)
    for idx in range(len(arr)):
        if arr[idx]!=idx:
            return idx
    return -1
arr=[9,6,4,2,3,5,7,0,1]
ans=find_missing_Number(arr)
print(f"Missing num:{ans}")
