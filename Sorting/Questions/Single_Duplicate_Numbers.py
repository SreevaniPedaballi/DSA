# https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution:
    
    def sort(self,arr):
        idx=0
        while idx <len(arr):
            correct_idx=arr[idx]-1
            if arr[idx]!=arr[correct_idx]:
                arr=self.swap(arr,idx,correct_idx)
            else:
                idx+=1
        return arr

    def swap(self,arr,first_idx,second_idx):
        temp=arr[first_idx]
        arr[first_idx]=arr[second_idx]
        arr[second_idx]=temp
        return arr

                
    def findDuplicate(self, nums: list[int]) -> int:
        arr=self.sort(nums)
        print(arr)
        for idx in range(len(arr)):
            if arr[idx]!=idx+1:
                return arr[idx]
        return -1

s = Solution()
arr=[2,1,2]
print(arr)
ans=s.findDuplicate(arr)
print(ans)