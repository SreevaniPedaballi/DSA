# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
def sort(nums:list[int])->list[int]:
    idx=0
    while idx <len(nums):
        correct_idx=nums[idx]-1
        if nums[idx]!=nums[correct_idx]:
            temp=nums[correct_idx]
            nums[correct_idx]=nums[idx]
            nums[idx]=temp
        else:
            idx +=1
    return nums

def find_missing_nums(arr:list[int])->list[int]:
    nums=sort(arr)
    print(nums)
    missing_nums=[]
    for idx in range(len(nums)):
        if idx+1!=nums[idx]:
            missing_nums.append(idx+1)
    return missing_nums
nums = [1,1]#[4,3,2,7,8,2,3,1]
print(nums)
ans=find_missing_nums(nums)
print(ans)
    

